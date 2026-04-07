from typing import Dict, Any

from openenv.core import EnvClient
from openenv.core.client_types import StepResult

try:
    from .models import AiTradeAction, AiTradeObservation, AiTradeState
except ImportError:
    from models import AiTradeAction, AiTradeObservation, AiTradeState


class AiTradeClient(
    EnvClient[AiTradeAction, AiTradeObservation, AiTradeState]
):
    """
    Client for the AiTrade Environment.

    This client maintains a persistent WebSocket connection to the environment server,
    enabling efficient multi-step interactions with lower latency.
    """

    def _step_payload(self, action: AiTradeAction) -> Dict[str, Any]:
        """
        Convert AiTradeAction to JSON payload for step message.
        """
        return action.model_dump()

    def _parse_result(self, payload: Dict[str, Any]) -> StepResult[AiTradeObservation]:
        """
        Parse server response into StepResult[AiTradeObservation].
        """
        obs_data = payload.get("observation", {})
        
        # In our server environment:
        # returns AiTradeObservation with text, task_id, signals, reward, done, metadata
        
        observation = AiTradeObservation(
            text=obs_data.get("text", payload.get("text", "")),
            task_id=obs_data.get("task_id", payload.get("task_id", "")),
            reward=payload.get("reward"),
            done=payload.get("done", False),
            metadata=payload.get("info", payload.get("metadata", {}))
        )

        return StepResult(
            observation=observation,
            reward=payload.get("reward"),
            done=payload.get("done", False),
        )

    def _parse_state(self, payload: Dict[str, Any]) -> AiTradeState:
        """
        Parse server response into State object.
        """
        return AiTradeState(
            task_id=payload.get("task_id", ""),
            step=payload.get("step", 0),
            max_steps=payload.get("max_steps", 0),
            history=payload.get("history", []),
            done=payload.get("done", False)
        )
