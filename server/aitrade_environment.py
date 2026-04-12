from typing import Any, Dict, List, Optional
from uuid import uuid4
from openenv.core.env_server import Environment
from env.models import TradingAction, TradingObservation, TradingState
from env.environment import TradingEnvironment
from env.graders import profit_grader, sharpe_grader, risk_adjusted_grader

class SelectionGradeEnvironment(Environment[TradingAction, TradingObservation, TradingState]):
    SUPPORTS_CONCURRENT_SESSIONS = True
    
    # Class-level registry for cross-request persistence
    SESSIONS: Dict[str, TradingState] = {}
    LAST_RESULTS: Dict[str, float] = {}
    CORE = TradingEnvironment(fee=0.001)

    def __init__(self):
        # We use the class-level registries to persist state across instances
        pass

    def reset(
        self,
        seed: Optional[int] = None,
        episode_id: Optional[str] = None,
        **kwargs: Any,
    ) -> TradingObservation:
        eid = episode_id or str(uuid4())
        task_id = kwargs.get("task_id") or "trading_stable_v1"
        
        obs, state = self.CORE.reset(task_id=task_id, seed=seed or 42)
        state.task_id = task_id
        
        self.SESSIONS[eid] = state
        return obs

    def step(
        self,
        action: TradingAction,
        episode_id: Optional[str] = None,
        **kwargs: Any,
    ) -> TradingObservation:
        # Use a more robust ID resolution
        if episode_id:
            eid = episode_id
        elif self.SESSIONS:
            eid = list(self.SESSIONS.keys())[-1]
        else:
            eid = "default"
        
        if eid not in self.SESSIONS:
            print(f"DEBUG: Session {eid} not found in {list(self.SESSIONS.keys())}. Initializing new session.")
            obs, state = self.CORE.reset(task_id="trading_stable_v1")
            self.SESSIONS[eid] = state
        
        state = self.SESSIONS[eid]
        obs, reward, done, state = self.CORE.step(state, action)
        
        # Explicitly update the registry
        self.SESSIONS[eid] = state
        
        if done:
            if "stable" in state.task_id:
                score = profit_grader(state.portfolio_history)
            elif "volatile" in state.task_id:
                score = sharpe_grader(state.portfolio_history)
            else:
                score = risk_adjusted_grader(state.portfolio_history)
            
            obs.reward = score
            obs.done = True
            self.LAST_RESULTS[eid] = score
        else:
            obs.reward = float(reward)
            obs.done = False
            
        return obs

    @property
    def state(self) -> TradingState:
        if not self.SESSIONS:
            return TradingState()
        eid = list(self.SESSIONS.keys())[-1]
        return self.SESSIONS[eid]
