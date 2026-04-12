from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from openenv.core.env_server.http_server import create_app
from server.aitrade_environment import SelectionGradeEnvironment
from env.models import TradingAction, TradingObservation
from server.ui import get_terminal_html
import os

# Disable built-in Gradio mounting
os.environ["ENABLE_WEB_INTERFACE"] = "false"

# Create standard OpenEnv API app
app = create_app(
    SelectionGradeEnvironment,
    TradingAction,
    TradingObservation,
    env_name="aitrade",
    max_concurrent_envs=10,
)

@app.get("/web", response_class=HTMLResponse)
async def terminal_ui(request: Request):
    """Serves the pure HTML AiTrade terminal."""
    return get_terminal_html()

@app.get("/", include_in_schema=False)
async def root_redirect():
    """Redirect root to the terminal."""
    return RedirectResponse(url="/web")

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
