from typing import Any, Dict, List, Optional
import os

from openenv.core.env_server import Environment
try:
    from ..models import AiTradeAction, AiTradeObservation, AiTradeState
    from ..tasks.definitions import TASKS, TASK_NAMES
    from ..tasks.graders import grade_action
except ImportError:
    from models import AiTradeAction, AiTradeObservation, AiTradeState
    from tasks.definitions import TASKS, TASK_NAMES
    from tasks.graders import grade_action

class AiTradeEnvironment(Environment[AiTradeAction, AiTradeObservation, AiTradeState]):
    SUPPORTS_CONCURRENT_SESSIONS = True

    def __init__(self):
        self._task_id: Optional[str] = None
        self._step_idx: int = 0
        self._done: bool = False
        self._rewards: List[float] = []
        self._task_def: Any = None

    def reset(self, seed: Optional[int] = None, episode_id: Optional[str] = None, **kwargs: Any) -> AiTradeObservation:
        """Reset the environment to the start of a task."""
        self._task_id = kwargs.get("task_id") or kwargs.get("task") or "trend_following"
        
        if self._task_id not in TASKS:

            self._task_id = "trend_following"
            
        self._task_def = TASKS[self._task_id]
        self._step_idx = 0
        self._done = False
        self._rewards = []
        
        first_step = self._task_def["steps"][0]
        return AiTradeObservation(
            text=first_step["observation"],
            task_id=self._task_id
        )

    def step(self, action: AiTradeAction) -> AiTradeObservation:
        """Apply an action and transition to the next state."""
        if self._task_id is None:
            raise RuntimeError("Call reset() before step()")
        if self._done:
            raise RuntimeError("Episode is finished")

        step_data = self._task_def["steps"][self._step_idx]
        

        reward = grade_action(self._task_id, action.action, step_data["signals"])
        self._rewards.append(reward)
        self._step_idx += 1
        
        self._done = self._step_idx >= len(self._task_def["steps"])
        
        next_obs_text = ""
        if not self._done:
            next_obs_text = self._task_def["steps"][self._step_idx]["observation"]
            
        info = {
            "step": self._step_idx,
            "task_id": self._task_id,
            "rewards_so_far": self._rewards
        }

        return AiTradeObservation(
            text=next_obs_text,
            task_id=self._task_id,
            reward=reward,
            done=self._done,
            metadata=info
        )

    @property
    def state(self) -> AiTradeState:
        """Return the current comprehensive state."""
        return AiTradeState(
            task_id=self._task_id or "",
            step=self._step_idx,
            max_steps=len(self._task_def["steps"]) if self._task_def else 0,
            history=[str(r) for r in self._rewards],
            done=self._done
        )
