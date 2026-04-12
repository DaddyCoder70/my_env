import numpy as np
from typing import List, Dict, Any

class MarketScenario:
    def __init__(self, task_id: str, max_steps: int = 100, seed: int = 42):
        self.task_id = task_id
        self.max_steps = max_steps
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        
    def generate_data(self) -> Dict[str, Any]:
        """Generates synthetic price and indicator data based on task_id."""
        steps = self.max_steps + 20
        
        if "stable" in self.task_id:
            returns = self.rng.normal(0.001, 0.005, steps)
        elif "volatile" in self.task_id:
            returns = self.rng.normal(0.0, 0.02, steps)
        elif "crash" in self.task_id:
            returns = self.rng.normal(0.0005, 0.01, steps)
            crash_start = int(self.max_steps * 0.7)
            returns[crash_start:crash_start+5] = -0.05
        else:
            returns = self.rng.normal(0.0005, 0.01, steps)
            
        prices = 100 * np.exp(np.cumsum(returns))
        
        ema = self._calculate_ema(prices, 10)
        rsi = self._calculate_rsi(prices, 14)
        vol = self._calculate_volatility(returns, 10)
        
        return {
            "prices": prices[-self.max_steps:].tolist(),
            "returns": returns[-self.max_steps:].tolist(),
            "ema": ema[-self.max_steps:].tolist(),
            "rsi": rsi[-self.max_steps:].tolist(),
            "volatility": vol[-self.max_steps:].tolist(),
        }

    def _calculate_ema(self, arr: np.ndarray, period: int) -> np.ndarray:
        alpha = 2 / (period + 1)
        ema = [arr[0]]
        for i in range(1, len(arr)):
            ema.append(arr[i] * alpha + ema[-1] * (1 - alpha))
        return np.array(ema)

    def _calculate_rsi(self, prices: np.ndarray, period: int) -> np.ndarray:
        changes = np.diff(prices)
        gains = np.where(changes > 0, changes, 0)
        losses = np.where(changes < 0, -changes, 0)
        
        avg_gain = self._calculate_ema(gains, period)
        avg_loss = self._calculate_ema(losses, period)
        
        rs = avg_gain / (avg_loss + 1e-9)
        rsi = 100 - (100 / (1 + rs))
        return np.pad(rsi, (1, 0), mode='constant', constant_values=50)

    def _calculate_volatility(self, returns: np.ndarray, period: int) -> np.ndarray:
        vol = []
        for i in range(len(returns)):
            if i < period:
                vol.append(np.std(returns[:i+1]))
            else:
                vol.append(np.std(returns[i-period:i]))
        return np.array(vol)
