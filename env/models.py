from typing import Dict, List, Optional, Any, Union
from pydantic import Field, field_validator
from openenv.core.env_server.types import Action, Observation, State

class TradingAction(Action):
    action: Union[float, str] = Field(
        ...,
        description=(
            "The target position size. "
            "Continuous: 1.0 = Long, -1.0 = Short, 0.0 = Neutral. "
            "Categorical: 'BUY' (1.0), 'SELL' (-1.0), 'HOLD' (0.0)."
        ),
        examples=[1.0, -0.5, "BUY"]
    )

    @field_validator("action")
    @classmethod
    def validate_action(cls, v: Any) -> Union[float, str]:
        if isinstance(v, str):
            v_upper = v.upper().strip()
            mapping = {"BUY": 1.0, "SELL": -1.0, "HOLD": 0.0}
            if v_upper in mapping:
                return mapping[v_upper]
            raise ValueError("String actions must be BUY, SELL, or HOLD")
        if isinstance(v, (int, float)):
            if not (-1.01 <= v <= 1.01):
                raise ValueError("Continuous actions must be between -1.0 and 1.0")
            return float(v)
        return v

class TradingObservation(Observation):
    text: str = Field(
        default="",
        description="Natural language summary of the current market state."
    )
    indicators: Dict[str, Any] = Field(
        default_factory=dict,
        description="Technical indicators and market state data."
    )
    reward: float = Field(
        default=0.0,
        description="The reward achieved in the current step."
    )
    done: bool = Field(
        default=False,
        description="Whether the episode has terminated."
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional debugging or visualization data."
    )

class TradingState(State):
    prices: List[float] = Field(default_factory=list)
    portfolio_history: List[float] = Field(default_factory=list)
    action_history: List[float] = Field(default_factory=list)
    reward_history: List[float] = Field(default_factory=list)
    position: float = Field(default=0.0)
    cash: float = Field(default=100000.0)
    step: int = Field(default=0)
    max_steps: int = Field(default=100)
    task_id: str = Field(default="")
    done: bool = Field(default=False)
    metadata: Dict[str, Any] = Field(default_factory=dict)
