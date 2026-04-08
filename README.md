---
title: AiTrade Environment Server
emoji: 📈
colorFrom: pink
colorTo: red
sdk: docker
pinned: false
app_port: 8000
base_path: /web
tags:
  - openenv
---

# AiTrade: Financial LLM Benchmark

AiTrade is an OpenEnv-compliant environment specifically designed to benchmark the financial reasoning capabilities of Large Language Models within the context of Indian NSE equities.

## Motivation
Financial markets are non-linear and high-stakes. While most LLMs can perform basic sentiment analysis, they often struggle with:
1.  **Regime Detection**: Distinguishing between bullish momentum and overextended range-bound markets.
2.  **Risk Overrides**: Heeding macro-economic warnings (like FII outflows) even when technical signals look bullish.
3.  **Capital Preservation**: Knowing when to sit out of directionless "chop".

AiTrade provides a standardized interface to evaluate these core competencies.

---

## Environment Specification

### Observation Space
The environment provides a structured text-based market report for each step. Each report includes:
- **Technical Signals**: EMA deviations (20/50/200), momentum scores, and trend strength.
- **Market Microstructure**: DII/FII institutional flows and volume trends.
- **Macro Signals**: Geopolitical risk scores, sentiment indicators, and Forex stability.

### Action Space
Agents must issue one of three discrete actions:
- `buy`: Commit capital to a long position.
- `sell`: Exit positions or protect capital in bearish regimes.
- `hold`: Observe from the sidelines (capital preservation).

---

## Tasks and Difficulty

| Task | Difficulty | Description | Core Requirement |
| :--- | :--- | :--- | :--- |
| `trend_following` | **Easy** | Follow strong bullish momentum. | Recognition of positive EMA/Momentum alignment. |
| `range_trading` | **Intermediate** | Sideways market identification. | Avoiding over-trading in 0.45-0.55 neutral zones. |
| `macro_risk_filter` | **Intermediate** | Macro risk override. | Prioritizing `hold` when macro score drops below 0.45. |
| `bear_defense` | **Hard** | Aggressive capital protection. | Identifying bear regimes where `sell` is the only safe exit. |

---

## Baseline Benchmarks
Evaluated across 3-step episodes. Scores represent Mean Reward [0.0 - 1.0].

| Model | Trend Following | Bear Defense | Range Trading | Macro Risk | Result |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **GPT-OSS-120B** | 0.956 | **0.896** | 0.990 | 0.883 | **100%** |
| **GPT-OSS-Safeguard 20B** | 0.956 | **0.896** | 0.990 | 0.883 | **100%** |
| **Llama 4 Scout 17B** | 0.709 | 0.490 | 0.990 | 0.883 | 75% |
| **Llama 3.3 70B** | 0.956 | 0.490 | 0.990 | 0.883 | 75% |
| **Moonshot Kimi K2** | 0.956 | 0.490 | 0.990 | 0.883 | 75% |
| **Llama 3.1 8B** | 0.956 | 0.490 | 0.413 | 0.603 | 50% |

---

## Setup and Usage

### 1. Installation
Ensure the `uv` tool is installed for dependency management.
```bash
uv sync
```

### 2. Environment Configuration
Configure the environment variables by copying the template.
```bash
cp .env.example .env
```

### 3. Server Execution
Run the local development server.
```bash
uv run server
```

### 4. Benchmark Evaluation
Execute the evaluation suite against the target model.
```bash
python inference.py
```

---

## Project Structure
```
my_env/
├── tasks/           # Task definitions and reward graders
├── server/          # FastAPI + WebSocket environment logic
├── client.py        # OpenEnv client implementation
├── models.py        # Pydantic schemas for actions/observations
├── inference.py     # Benchmark execution script
└── openenv.yaml     # Environment manifest
```
