from typing import Any, Dict, Tuple
from env.models import TradingAction, TradingObservation, TradingState
from env.data_loader import MarketScenario
import math

class TradingEnvironment:
    def __init__(self, fee: float = 0.001):
        self.fee = fee
        
    def reset(self, task_id: str, seed: int = 42) -> Tuple[TradingObservation, TradingState]:
        scenario = MarketScenario(task_id, seed=seed)
        data = scenario.generate_data()
        
        state = TradingState(
            prices=data["prices"],
            portfolio_history=[100000.0],
            cash=100000.0,
            position=0.0,
            step=0,
            max_steps=len(data["prices"]),
            task_id=task_id,
            done=False
        )
        state.metadata = data 
        obs = self._generate_observation(state)
        return obs, state

    def step(self, state: TradingState, action: TradingAction) -> Tuple[TradingObservation, float, bool, TradingState]:
        current_price = state.prices[state.step]
        target_pos = action.action
        
        current_value = state.position * current_price
        nav = state.cash + current_value
        target_value = target_pos * nav
        
        trade_size = abs(target_value - current_value)
        transaction_cost = trade_size * self.fee
        
        state.cash = nav - target_value - transaction_cost
        state.position = target_value / current_price
        
        state.step += 1
        if state.step >= state.max_steps:
            state.done = True
            
        new_nav = state.cash + (state.position * state.prices[min(state.step, state.max_steps-1)])
        state.portfolio_history.append(new_nav)
        
        reward_log = math.log(new_nav / state.portfolio_history[-2])
        
        # Normalize reward to (0.01, 0.99) centered at 0.5
        # Scaling: 1% profit -> 0.5 + 0.05 = 0.55
        reward_mapped = 0.5 + (reward_log * 5.0)
        reward_clamped = max(0.01, min(0.99, reward_mapped))
        
        state.action_history.append(target_pos)
        state.reward_history.append(reward_clamped)
        
        obs = self._generate_observation(state)
        return obs, float(reward_clamped), state.done, state

    def _generate_observation(self, state: TradingState) -> TradingObservation:
        curr_idx = min(state.step, state.max_steps - 1)
        
        price = state.metadata["prices"][curr_idx]
        rsi = state.metadata["rsi"][curr_idx]
        ema = state.metadata["ema"][curr_idx]
        vol = state.metadata["volatility"][curr_idx]
        
        ema_dist = (price - ema) / ema
        EMA_BUFFER = 0.002 # 0.2%
        
        if ema_dist > EMA_BUFFER:
            trend = "bullish"
        elif ema_dist < -EMA_BUFFER:
            trend = "bearish"
        else:
            trend = "neutral"
            
        indicators = {
            "price_norm": price / state.prices[0],
            "rsi": rsi / 100.0,
            "ema_dist": ema_dist,
            "ema_buffer_applied": True,
            "trend": trend,
            "volatility": vol,
            "position": state.position / (state.cash + state.position * price) * price
        }
        
        text = (
            f"Institutional Intelligence — Task: {state.task_id.upper()}\n"
            f"Price: {price:.2f} | EMA Deviation: {ema_dist:.2%} (Trend: {trend.upper()})\n"
            f"RSI: {rsi:.0f} | Volatility: {vol:.2f}\n"
            f"Position: {state.position:.2f} units"
        )
        
        return TradingObservation(
            text=text,
            indicators=indicators,
            metadata={"price": price, "step": state.step}
        )
