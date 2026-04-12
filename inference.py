import os
import json
import asyncio
import textwrap
import sys
from typing import List, Optional, Dict, Any, Tuple
from openai import OpenAI
from client import TradingClient
from env.tasks import TASKS

from dotenv import load_dotenv
load_dotenv()

# --- HACKATHON CONFIGURATION v1.3.0 ---
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")
BENCHMARK = "aitrade_v1"

# --- LOGGING UTILITIES ---
def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)

def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]) -> None:
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )

def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)

# --- ELITE AGENT LOGIC v8 (FINAL SUBMISSION READY) ---
def build_system_prompt() -> str:
    return textwrap.dedent(
        """
        You are a senior quantitative trader. Target: Capture trends, avoid noise, exit at exhaustion.
        
        CORE PRINCIPLES:
        - Default behavior: ACT (BUY/SELL). HOLD is rare.
        - RSI 70-85 in Bullish trend = Strength, NOT reversal. Do NOT exit.
        - RSI 15-30 in Bearish trend = Strength, NOT reversal. Do NOT exit.

        DECISION FLOW (MANDATORY):
        1. TREND DETECTION:
           - Price > EMA + 0.2% -> BULLISH (Action: BUY)
           - Price < EMA - 0.2% -> BEARISH (Action: SELL)
           - Otherwise -> NEUTRAL (Action: HOLD)
        2. EXHAUSTION OVERRIDE (CRITICAL):
           - Reverse to SELL only if [RSI > 88] AND [Price > EMA + 1.0%].
           - Reverse to BUY only if [RSI < 12] AND [Price < EMA - 1.0%].
        3. ANTI-FLIP:
           - Do not switch direction every step. Maintain direction unless exhaustion trigger is hit.
        
        OUTPUT FORMAT:
        MODE: TREND or MEAN_REVERSION
        ACTION: BUY or SELL or HOLD
        CONFIDENCE: <0 to 1>
        THESIS: <trend_state> | RSI: <val> | Reasoning: <short>
        """
    ).strip()

async def get_agent_action(client: OpenAI, obs_text: str, indicators: Dict[str, float], last_action: str) -> Tuple[str, str, str]:
    user_prompt = f"""
    {obs_text}
    Indicators: {json.dumps(indicators)}
    [Last Action]: {last_action}
    """
    
    for attempt in range(2):
        try:
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": build_system_prompt()},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.0,
                max_tokens=200,
            )
            content = completion.choices[0].message.content
            lines = content.strip().split("\n")
            mode = next((l for l in lines if l.startswith("MODE:")), "TREND")
            action_line = next((l for l in lines if l.startswith("ACTION:")), "")
            thesis = next((l for l in lines if l.startswith("THESIS:")), "Execution.")
            
            action = "HOLD"
            if "BUY" in action_line.upper(): action = "BUY"
            elif "SELL" in action_line.upper(): action = "SELL"
            
            return action, thesis.replace("THESIS:", "").strip(), mode.replace("MODE:", "").strip()
        except Exception as e:
            if attempt == 0: continue
            return ("HOLD", f"FAILURE: {str(e)}", "ERROR")
    return ("HOLD", "Fallback", "ERROR")

def institutional_nudge(indicators: Dict[str, float]) -> str:
    trend = indicators.get("trend", "neutral")
    if trend == "bullish": return "BUY"
    if trend == "bearish": return "SELL"
    return "HOLD"

async def run_task(trading_client: TradingClient, openai_client: OpenAI, task_config: Dict[str, Any]):
    task_id = task_config["id"]
    log_start(task=task_id, env=BENCHMARK, model=MODEL_NAME)
    
    rewards, steps_taken, success, score = [], 0, False, 0.0
    last_action = "HOLD"
    hold_streak = 0
    
    try:
        obs = await trading_client.reset(task_id=task_id)
        
        for step in range(1, task_config["max_steps"] + 1):
            indicators = obs["indicators"]
            trend = indicators.get("trend", "neutral")
            raw_action, thesis, mode = await get_agent_action(openai_client, obs["text"], indicators, last_action)
            
            # 1. Determine Trend-Based Default
            trend_action = "HOLD"
            if trend == "bullish": trend_action = "BUY"
            elif trend == "bearish": trend_action = "SELL"
            
            # 2. Extract Exhaustion Gates (v8 Submission Ready)
            ema_dist_raw = indicators.get("ema_dist", 0.0)
            rsi = indicators.get("rsi", 0.5) * 100
            
            bull_exhaustion = (rsi > 88) and (ema_dist_raw > 0.01)
            bear_exhaustion = (rsi < 12) and (ema_dist_raw < -0.01)
            exhaustion_flip = (bull_exhaustion and raw_action == "SELL") or (bear_exhaustion and raw_action == "BUY")
            
            # 3. Apply Soft Anti-Flip Logic (Trend Persistence)
            action = raw_action
            if action != last_action and last_action != "HOLD":
                if not exhaustion_flip:
                    action = trend_action # Default back to trend unless exhaustion is triggered
            
            # 4. Mandatory Hard Constraints
            if trend == "bullish" and action == "HOLD":
                action = "BUY"
            elif trend == "bearish" and action == "HOLD":
                action = "SELL"
            
            # --- INSTITUTIONAL NUDGE ---
            if action == "HOLD":
                hold_streak += 1
                if hold_streak >= 12:
                    action = institutional_nudge(indicators)
                    hold_streak = 0
            else:
                hold_streak = 0
            
            obs, reward, done = await trading_client.step(action)
            log_step(step, action, reward, done, error=None)
            
            rewards.append(reward)
            steps_taken, last_action = step, action
            if done: break
        
        # 4. Scoring Logic (Resilient to early termination or partial runs)
        if rewards:
            # Reconstruct cumulative log-return: reward = 0.5 + (log_return * 5.0)
            log_returns = [(r - 0.5) / 5.0 for r in rewards]
            cumulative_log_return = sum(log_returns)
            
            # Map total return to score using standard profit_grader logic: 0.5 + (return * 2.5)
            # This ensures the local proxy matches the official grader.
            score = 0.5 + (cumulative_log_return * 2.5)
        
        # If the task completed naturally, use the environment's official grader score
        if done:
            score = obs.get("reward", score)
        
        # Strict hackathon clamping (0.01, 0.99)
        score = min(max(float(score), 0.01), 0.99)
        success = score >= 0.70
        
    except Exception as e:
        if not isinstance(e, asyncio.CancelledError):
            print(f"--- FATAL RUNTIME ERROR: {str(e)} ---", file=sys.stderr)
    finally:
        log_end(success=success, steps=steps_taken, score=score, rewards=rewards)

async def main():
    if not API_KEY:
        print("[ERROR] HF_TOKEN / API_KEY missing.")
        return

    openai_client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
    trading_client = TradingClient(base_url="http://localhost:8000")
    
    for task in TASKS:
        await run_task(trading_client, openai_client, task)
        
    await trading_client.close()

if __name__ == "__main__":
    asyncio.run(main())
