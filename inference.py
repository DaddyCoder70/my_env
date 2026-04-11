#!/usr/bin/env python3
"""
inference.py — AiTrade OpenEnv Agent
=====================================
Runs an LLM agent through all 8 trading tasks and emits structured stdout logs.

Required environment variables:
    API_BASE_URL      LLM API endpoint
    MODEL_NAME        Model identifier
    HF_TOKEN          HuggingFace / API key
    LOCAL_IMAGE_NAME  (optional) Docker image to launch as env server

Stdout format (must not deviate):
    [START] task=<task> env=<benchmark> model=<model>
    [STEP]  step=<n> action=<action> reward=<0.00> done=<true|false> error=<msg|null>
    [END]   success=<true|false> steps=<n> score=<0.000> rewards=<r1,r2,...>
"""

import os
import re
import textwrap
from typing import List, Optional

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

from models import AiTradeAction
from client import AiTradeClient

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

IMAGE_NAME   = os.getenv("LOCAL_IMAGE_NAME")
API_KEY      = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME   = os.getenv("MODEL_NAME",   "Qwen/Qwen2.5-72B-Instruct")
ENV_BASE_URL = os.getenv("ENV_BASE_URL", "http://localhost:8000")
BENCHMARK    = "aitrade"

MAX_STEPS               = 1     # single-step episodes — each /reset + /step = one graded decision
SUCCESS_SCORE_THRESHOLD = 0.6
TEMPERATURE             = 0.15  # very low — force deterministic trading decisions
MAX_TOKENS              = 512   # short output required: single word

TASKS = [
    "trend_following",
    "bear_defense",
    "range_trading",
    "macro_risk_filter",
    "breakout_momentum",
    "volatile_range",
    "recovery_play",
    "sector_rotation",
]

SYSTEM_PROMPT = textwrap.dedent("""
    You are a disciplined quantitative analyst for Indian NSE equity markets.

    You will receive a market analysis report with quantitative signals.
    Based solely on the signals, choose exactly one of three actions:

      BUY  — enter/increase position (use for bullish, uptrend, breakout, or recovery scenarios)
      SELL — exit positions (use for bearish, downtrend, or capital-protection scenarios)
      HOLD — take no action (use for sideways, uncertain, high-volatility, or macro-constrained environments)

    Your decision rule:
    - If momentum + trend > 1.30 and regime is bull/breakout → BUY
    - If momentum + trend < 0.60 or regime is bear → SELL
    - If macro score < 0.45 → HOLD regardless of technical signals
    - If volatility > 0.75 and trend near 0.50 → HOLD
    - Otherwise → weigh all signals and decide

    Reply with EXACTLY ONE WORD: BUY, SELL, or HOLD.
    No explanation. No punctuation. No extra text.
""").strip()

# ---------------------------------------------------------------------------
# Logging helpers — must match the OpenEnv spec exactly
# ---------------------------------------------------------------------------

def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]) -> None:
    error_val = error if error else "null"
    done_val  = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}",
        flush=True,
    )

# ---------------------------------------------------------------------------
# LLM call
# ---------------------------------------------------------------------------

def get_model_action(
    client: OpenAI,
    observation: str,
    history: List[str],
) -> str:
    """Ask the LLM to decide BUY / SELL / HOLD and return the lowercased action."""
    history_block = "\n".join(history[-3:]) if history else "None"
    user_prompt = (
        f"Market Report:\n{observation}\n\n"
        f"Your prior decisions this episode:\n{history_block}\n\n"
        f"Trading decision (BUY / SELL / HOLD):"
    )

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_prompt},
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stream=False,
        )
        text = (completion.choices[0].message.content or "").strip().upper()

        # Strip <think>...</think> reasoning blocks (some models emit these)
        text_clean = re.sub(r'<THINK>.*?</THINK>', '', text, flags=re.DOTALL)
        text_clean = re.sub(r'<THINK>.*',          '', text_clean, flags=re.DOTALL)

        # Extract action from cleaned output
        for action in ("BUY", "SELL", "HOLD"):
            if action in text_clean:
                return action.lower()

        # Fallback: search raw output
        for action in ("BUY", "SELL", "HOLD"):
            if action in text:
                return action.lower()

        print(f"[DEBUG] Unexpected model output: {text[:120]!r} — defaulting to hold", flush=True)
        return "hold"

    except Exception as exc:
        print(f"[DEBUG] Model request failed: {exc}", flush=True)
        return "hold"   # safe capital-preserving default

# ---------------------------------------------------------------------------
# Single task runner
# ---------------------------------------------------------------------------

def run_task(client: OpenAI, task_name: str, seed: int = 42) -> None:
    """Run one full episode for the given task, emitting [START]/[STEP]/[END] logs."""

    if IMAGE_NAME:
        env_instance = AiTradeClient.from_docker_image(IMAGE_NAME, task=task_name)
    else:
        env_instance = AiTradeClient(base_url=ENV_BASE_URL)

    history:    List[str]  = []
    rewards:    List[float] = []
    steps_taken = 0
    score        = 0.0
    success      = False
    last_error: Optional[str] = None

    log_start(task=task_name, env=BENCHMARK, model=MODEL_NAME)

    try:
        with env_instance.sync() as env:
            # Pass task_id and seed for deterministic, reproducible episodes
            if not IMAGE_NAME:
                result = env.reset(task_id=task_name, seed=seed)
            else:
                result = env.reset()

            for step in range(1, MAX_STEPS + 1):
                if result.done:
                    break

                observation_text = result.observation.text
                action_str = get_model_action(client, observation_text, history)

                try:
                    result = env.step(AiTradeAction(action=action_str))
                    last_error = None
                except Exception as exc:
                    last_error = str(exc)
                    result.done = True

                reward = result.reward or 0.5  # neutral fallback if None
                done   = result.done

                rewards.append(reward)
                steps_taken = step

                log_step(step=step, action=action_str, reward=reward, done=done, error=last_error)
                history.append(f"Step {step}: {action_str} → reward {reward:.3f}")

                if done:
                    break

        score   = sum(rewards) / len(rewards) if rewards else 0.0
        # Clamp to valid open interval
        score   = max(0.01, min(score, 0.99))
        success = score >= SUCCESS_SCORE_THRESHOLD

    except Exception as exc:
        print(f"[DEBUG] Task {task_name} error: {exc}", flush=True)
        last_error = str(exc)

    finally:
        log_end(success=success, steps=steps_taken, score=score, rewards=rewards)

# ---------------------------------------------------------------------------
# Main — iterate all 8 tasks
# ---------------------------------------------------------------------------

def main() -> None:
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
    for idx, task_name in enumerate(TASKS):
        run_task(client, task_name, seed=idx * 7 + 42)


if __name__ == "__main__":
    main()
