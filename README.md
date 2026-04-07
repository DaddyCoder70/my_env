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

# AiTrade OpenEnv Environment

An OpenEnv-compliant trading agent environment for Indian NSE equities. Agents interact with a FastAPI + WebSocket server, receive market analysis observations, and issue `BUY`, `SELL`, or `HOLD` decisions evaluated by an LLM.

## Tasks

| Task | Description |
|---|---|
| `trend_following` | Bull market — reward BUY decisions |
| `bear_defense` | Bear market — reward SELL decisions |
| `range_trading` | Sideways market — reward HOLD decisions |
| `macro_risk_filter` | High macro risk — reward capital-preserving actions |

## Quick Start

```python
from my_env.client import AiTradeClient
from my_env.models import AiTradeAction

client = AiTradeClient(base_url="http://localhost:8000")

with client.sync() as env:
    result = env.reset(task_id="trend_following")
    print(result.observation.text)

    result = env.step(AiTradeAction(action="buy"))
    print(f"Reward: {result.reward}, Done: {result.done}")
```

## Running the Server

```bash
# Install dependencies
uv sync

# Start server
uv run server

# Or with hot-reload (dev)
uvicorn my_env.server.app:app --reload --host 0.0.0.0 --port 8000
```

## Running the Inference Agent

```bash
# Set environment variables
cp .env.example .env
# Edit .env with your API key

# Run all tasks
python inference.py
```

## Environment Variables

```env
API_BASE_URL=https://api.groq.com/openai/v1   # Any OpenAI-compatible endpoint
MODEL_NAME=llama-3.3-70b-versatile            # Model identifier
HF_TOKEN=your_api_key_here                    # API key
LOCAL_IMAGE_NAME=                             # Optional: Docker image name
```

## Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/reset` | POST | Reset environment for a task |
| `/step` | POST | Execute an action |
| `/state` | GET | Get current state |
| `/schema` | GET | Get action/observation schemas |
| `/ws` | WebSocket | Persistent session (low latency) |
| `/web` | GET | Interactive web UI |
| `/docs` | GET | OpenAPI documentation |

## Project Structure

```
my_env/
├── __init__.py              # Module exports
├── client.py                # AiTradeClient (WebSocket)
├── models.py                # AiTradeAction, AiTradeObservation, AiTradeState
├── inference.py             # LLM agent runner
├── openenv.yaml             # OpenEnv manifest
├── pyproject.toml           # Project metadata & dependencies
├── .env.example             # Environment variable template
├── Dockerfile               # Container image
├── validator.bash           # Submission validator
├── tasks/
│   ├── definitions.py       # Task configs & prompts
│   └── graders.py           # Reward calculation logic
└── server/
    ├── app.py               # FastAPI application
    └── aitrade_environment.py  # Core environment logic
```
