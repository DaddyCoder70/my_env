from typing import Dict, List, Optional
from pydantic import Field
from openenv.core.env_server.types import Action, Observation, State


class AiTradeAction(Action):
    """Trading action for an Indian NSE equity."""

    action: str = Field(
        ...,
        description=(
            "The trading decision. Must be one of: 'buy', 'sell', or 'hold'. "
            "'buy' enters or adds to a position in a bullish scenario. "
            "'sell' exits positions for capital protection. "
            "'hold' preserves capital in uncertain or sideways markets."
        ),
        examples=["buy", "sell", "hold"],
    )


class AiTradeObservation(Observation):
    """Market analysis report observation returned after each reset/step."""

    text: str = Field(
        default="",
        description=(
            "Natural language market analysis report containing quantitative "
            "signals: momentum, trend, volatility, macro environment, regime "
            "classification, and institutional flow indicators."
        ),
    )
    task_id: str = Field(
        default="",
        description="Identifier of the current task scenario.",
        examples=["trend_following", "bear_defense", "range_trading"],
    )


class AiTradeState(State):
    """Complete state of an AiTrade episode."""

    task_id: str = Field(default="", description="Active task scenario identifier.")
    step: int = Field(default=0, description="Current step index (0-indexed).")
    max_steps: int = Field(default=5, description="Total steps in this episode.")
    history: List[str] = Field(
        default_factory=list,
        description="List of reward strings for completed steps.",
    )
    done: bool = Field(default=False, description="Whether the episode has terminated.")
