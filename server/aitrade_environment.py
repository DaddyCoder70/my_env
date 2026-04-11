"""
AiTrade Environment — OpenEnv-compliant trading decision environment.

DESIGN NOTE — Stateless HTTP Architecture
==========================================
The OpenEnv HTTP server creates a FRESH environment instance for every single
HTTP request (reset, step, state). This means in-memory state between calls is
impossible on the HTTP path.

The framework's intended stateful path is the WebSocket endpoint (/ws).

The solution used here — mirroring the reference `reasoning_gym_env` approach:

1. /reset  selects a market scenario, returns its observation text + embedded
   task_id and step_idx as part of the observation metadata.

2. /step   accepts `task_id` and `step_idx` as EXTRA body kwargs alongside
   the action. This makes step() fully self-contained. The evaluator pipeline
   echoes these context fields back when calling /step.

   StepRequest has `additionalProperties: true`, so extra fields pass through
   to our step() signature transparently.

Every reset() + step() pair is a COMPLETE, INDEPENDENTLY GRADABLE trading
decision. 40 unique market scenarios across 8 task types.
"""

from typing import Any, Dict, List, Optional
from uuid import uuid4

from openenv.core.env_server import Environment
from openenv.core.env_server.types import State

try:
    from ..models import AiTradeAction, AiTradeObservation, AiTradeState
    from ..tasks.definitions import TASKS, TASK_NAMES
    from ..tasks.graders import grade_action
except ImportError:
    from models import AiTradeAction, AiTradeObservation, AiTradeState
    from tasks.definitions import TASKS, TASK_NAMES
    from tasks.graders import grade_action


class AiTradeEnvironment(Environment[AiTradeAction, AiTradeObservation, AiTradeState]):
    """
    AiTrade: Indian NSE equity trading decision environment.

    SINGLE-STEP EPISODE DESIGN (compatible with stateless HTTP):
    - reset()  → selects a market scenario, returns observation + context metadata
    - step()   → grades BUY/SELL/HOLD, using task_id+step_idx kwargs; done=True

    The step() method accepts task_id and step_idx as extra kwargs so it can
    look up the correct signals independently, without relying on prior state.

    Rewards are strictly in the open interval (0.01, 0.99) as required by OpenEnv.
    """

    SUPPORTS_CONCURRENT_SESSIONS = True

    # Shared sequential counter for round-robin task selection
    # (class-level so it persists across instances in the same process)
    _global_step_counter: int = 0

    def __init__(self):
        self._task_id: Optional[str] = None
        self._step_idx: int = 0
        self._done: bool = False
        self._last_reward: Optional[float] = None
        self._episode_id: str = str(uuid4())

    @classmethod
    def _next_step_index(cls) -> tuple:
        """Return the next (task_id, step_idx) in round-robin order."""
        all_steps = []
        for tid, tdef in TASKS.items():
            for sidx in range(len(tdef["steps"])):
                all_steps.append((tid, sidx))
        idx = cls._global_step_counter % len(all_steps)
        cls._global_step_counter += 1
        return all_steps[idx]

    def reset(
        self,
        seed: Optional[int] = None,
        episode_id: Optional[str] = None,
        **kwargs: Any,
    ) -> AiTradeObservation:
        """
        Reset to a new single-step episode by selecting one market scenario.

        Selection priority:
          1. Explicit task_id + step_idx in kwargs
          2. seed-based deterministic selection (seed mod total scenarios)
          3. Sequential round-robin across all 40 scenarios

        The returned observation includes task_id and step_idx in the response
        so the evaluator can echo them back in the /step call.

        Args:
            seed: Selects scenario deterministically.
            episode_id: Optional episode identifier.
            **kwargs: May include task_id and step_idx for explicit selection.

        Returns:
            AiTradeObservation with market report and embedded context.
        """
        self._done = False
        self._last_reward = None
        self._episode_id = episode_id or str(uuid4())

        # Build flat list of all (task_id, step_idx) pairs
        all_steps = []
        for tid, tdef in TASKS.items():
            for sidx in range(len(tdef["steps"])):
                all_steps.append((tid, sidx))
        total = len(all_steps)

        # Select which (task, step) to present
        requested_task = kwargs.get("task_id") or kwargs.get("task")
        requested_step = kwargs.get("step_idx")

        if requested_task and requested_task in TASKS:
            self._task_id = requested_task
            self._step_idx = int(requested_step or 0)
            max_step = len(TASKS[self._task_id]["steps"]) - 1
            self._step_idx = min(self._step_idx, max_step)
        elif seed is not None:
            task_id, step_idx = all_steps[seed % total]
            self._task_id = task_id
            self._step_idx = step_idx
        else:
            task_id, step_idx = self._next_step_index()
            self._task_id = task_id
            self._step_idx = step_idx

        step_data = TASKS[self._task_id]["steps"][self._step_idx]
        obs_text = step_data["observation"]
        ideal_action = step_data["signals"].get("ideal_action",
                       TASKS[self._task_id].get("ideal_action", "unknown"))

        return AiTradeObservation(
            text=obs_text,
            task_id=self._task_id,
            reward=None,
            done=False,
            metadata={
                "task_id": self._task_id,
                "step_idx": self._step_idx,
                "total_scenarios": total,
                "ideal_action": ideal_action,
                "instructions": (
                    "Analyse the market report and respond with one of: BUY, SELL, or HOLD. "
                    "Include task_id and step_idx in your /step request body."
                ),
            },
        )

    def step(
        self,
        action: AiTradeAction,
        task_id: Optional[str] = None,
        step_idx: Optional[int] = None,
        **kwargs: Any,
    ) -> AiTradeObservation:
        """
        Grade the BUY/SELL/HOLD action for a specific market scenario.

        This method is SELF-CONTAINED: it uses task_id and step_idx (either
        passed as explicit kwargs or falling back to the last reset state)
        to look up the correct signals and grade the action.

        Args:
            action: AiTradeAction with action field ("buy", "sell", or "hold").
            task_id: Task identifier (echoed from reset() response metadata).
            step_idx: Step index within the task (echoed from reset() response).
            **kwargs: Additional kwargs (ignored).

        Returns:
            AiTradeObservation with reward, done=True, and grading metadata.
        """
        # Resolve task context — prefer explicit kwargs, fall back to instance state
        resolved_task = task_id or self._task_id
        resolved_step = step_idx if step_idx is not None else self._step_idx

        # If still no context, default to first scenario of first task
        if resolved_task is None or resolved_task not in TASKS:
            resolved_task = TASK_NAMES[0]
            resolved_step = 0

        # Clamp step index
        max_step = len(TASKS[resolved_task]["steps"]) - 1
        resolved_step = min(max(int(resolved_step), 0), max_step)

        step_data = TASKS[resolved_task]["steps"][resolved_step]
        signals = step_data["signals"]
        ideal = signals.get("ideal_action", TASKS[resolved_task].get("ideal_action", "unknown"))

        # Grade and clamp reward strictly in (0.01, 0.99)
        raw_reward = grade_action(resolved_task, action.action, signals)
        reward = round(min(max(float(raw_reward), 0.01), 0.99), 4)
        self._last_reward = reward
        self._done = True

        return AiTradeObservation(
            text="",          # episode complete — no next observation
            task_id=resolved_task,
            reward=reward,
            done=True,
            metadata={
                "task_id": resolved_task,
                "step_idx": resolved_step,
                "action_taken": action.action.lower(),
                "ideal_action": ideal,
                "correct": action.action.lower() == ideal.lower(),
                "reward": reward,
            },
        )

    @property
    def state(self) -> AiTradeState:
        """Return the current state of the episode."""
        return AiTradeState(
            task_id=self._task_id or "",
            step=1 if self._done else 0,
            max_steps=1,
            history=[str(self._last_reward)] if self._last_reward is not None else [],
            done=self._done,
        )
