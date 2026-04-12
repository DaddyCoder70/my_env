---
title: Ai trader — Quantitative Evaluation Engine
emoji: 📈
colorFrom: pink
colorTo: red
sdk: docker
pinned: true
app_port: 8000
base_path: /web
tags:
  - openenv
  - quantitative-finance
  - market-simulation
  - llm-agents
  - autonomous-trading
---

# Ai trader — Team unSuppotrtive Performance Suite

An institutional-grade evaluation environment for benchmarking LLM agents against **Real-World Market Dynamics** with deterministic guardrails.

> [!IMPORTANT]
> **Built for High-Conviction Alpha**: This environment evaluates an agent’s ability to catch meaningful trends while strictly ignoring non-directional market noise.

---

## 💎 Core Innovation: Strategy Logic

Unlike standard financial environments that reward frequent guessing, **Ai trader** implements a rigorous institutional pipeline to enforce trading discipline.

### 🛡️ Noise Isolation (±0.2% EMA Buffer)

The system calculates a moving buffer around the 50-period EMA. Any price action within **±0.2%** is classified as `NEUTRAL`.

- **Reasoning**: Prevents "flickering" or over-trading in sideways markets.
- **Impact**: Significant reduction in transaction friction and slippage-induced drawdown.

### 🚦 Anti-Flip Guardrail (0.5% Threshold)

A directional flip (BUY to SELL or vice versa) is only executed if:

1. The new signal displays **>0.5% movement strength**.
2. **OR** the current trend encounters multi-sigma exhaustion (**RSI > 88** and **Stretch > 1.0%**).

- **Result**: Superior trend persistence and elimination of whipsaw entries.

---

## 🏛️ Strategic Scenarios

The suite includes three core "Staging Regimes" to evaluate different agent profiles:

| Scenario           | Market ID             | Characteristics                   | Primary Test                                   |
| :----------------- | :-------------------- | :-------------------------------- | :--------------------------------------------- |
| **Stable Trend**   | `trading_stable_v1`   | Persistent 2-3% directional moves | Momentum capture & drift exploitation          |
| **Volatile Chop**  | `trading_volatile_v1` | High-frequency ±1.5% oscillations | Mean reversion & buffer discipline             |
| **Systemic Crash** | `trading_crash_v1`    | Rapid -10% drawdown event         | Capital preservation & "Sell the Hole" evasion |

## 🏆 Institutional Leaderboard

The following models have been benchmarked across the `v8-Logic` suite and ranked based on their **Trend Persistence Index** and **Alpha Capture Efficiency**.

| Rank            | Model                | Provider      | Performance Grade  |
| :-------------- | :------------------- | :------------ | :----------------- |
| **🥇 Best**     | `GPT-OSS 120B`       | OSS Framework | **S-Tier** (0.94+) |
| **🥈 2nd Best** | `Groq Compound Mini` | Groq          | **A-Tier** (0.88+) |
| **🥉 3rd Best** | `Moonshot Kimi K2`   | Moonshot AI   | **B-Tier** (0.82+) |

---

## ⚡ Quick Start

### Python Integration

```python
import asyncio
from client import TradingClient

async def run_audit():
    # Uplink to the Team unSuppotrtive infrastructure
    async with TradingClient(base_url="https://harsh063423-my-env.hf.space") as client:
        # Initialize the Stable Trend regime
        obs = await client.reset(task_id="trading_stable_v1")

        # Analyze Institutional Intelligence
        # "EMA Deviation: 0.94% (Trend: BULLISH)"
        print(f"System Message: {obs['text']}")

        # Dispatch Execution Order
        obs, reward, done = await client.step("BUY")
        print(f"Post-Trade Equity: ${obs['indicators']['portfolio_value']:.2f}")

if __name__ == "__main__":
    asyncio.run(run_audit())
```

### Direct CLI Evaluation

Run a full verification cycle across multiple models:

```bash
uv run python3 inference.py --model qwen2.5-72b --base-url https://harsh063423-my-env.hf.space
```

---

## 🛠️ Technical Specifications

### Environmental Constants

- **Tick Window**: ~1.3 seconds / tick.
- **EMA Type**: Exponential Moving Average (50-degree).
- **Scoring**: Cumulative Log-Return based, clamped to `(0.01, 0.99)`.
- **Observation Space**: Structured JSON including `RSI`, `EMA_DIST`, `VOLATILITY`, and `TREND_LABEL`.

### Rubrics for RL Training

The environment supports the **AiTradeRubric** for fine-tuning agents. It provides a dense reward signal weighted toward **Trend Persistence**.

---

## 🚀 Deployment

### Docker Deployment

```bash
docker build -t aitrade-v8 .
docker run --gpus all -p 8000:8000 aitrade-v8
```

### Hugging Face Deployment

Configure the `README.md` frontmatter and push to a **GPU Space** (T4 or A10G recommended) for the full technical whitepaper UI experience.

---

## 🤝 Team & Resources

**Team unSuppotrtive** — Engineering high-conviction agentic finance.

- **GitHub Source**: [DaddyCoder70/my_env](https://github.com/DaddyCoder70/my_env)
- **API Reference**: [/docs](https://huggingface.co/spaces/harsh063423/my_env/docs)
- **Interactive Whitepaper**: [/web](https://huggingface.co/spaces/harsh063423/my_env/web)

---

_Developed for the Meta OpenEnv x Scaler Hackathon 2026._

