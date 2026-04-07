from typing import List, Optional
from openenv.core.env_server.types import Action, Observation, State

class AiTradeAction(Action):
    action: str  # "buy", "sell", "hold"

class AiTradeObservation(Observation):
    text: str
    task_id: str

class AiTradeState(State):
    task_id: str
    step: int
    max_steps: int
    history: List[str]
    done: bool
