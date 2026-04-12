import httpx
import asyncio
from typing import Dict, Any, List

class TradingClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=30.0)

    async def reset(self, task_id: str = "trend_following") -> Dict[str, Any]:
        resp = await self.client.post(
            f"{self.base_url}/reset",
            json={"task_id": task_id}
        )
        resp.raise_for_status()
        return resp.json()["observation"]

    async def step(self, action: str) -> tuple:
        resp = await self.client.post(
            f"{self.base_url}/step",
            json={"action": {"action": action}}
        )
        resp.raise_for_status()
        data = resp.json()
        
        # OpenEnv spec returns reward and done at the top level
        obs = data["observation"]
        reward = data.get("reward", 0.0)
        done = data.get("done", False)
        
        return obs, reward, done

    async def close(self):
        await self.client.aclose()
