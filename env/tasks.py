from env.graders import profit_grader, sharpe_grader, risk_adjusted_grader

TASKS = [
    {
        "id": "trading_stable_v1",
        "description": "Maximize growth in a low-volatility stable trend scenario.",
        "max_steps": 100,
        "grader": profit_grader
    },
    {
        "id": "trading_volatile_v1",
        "description": "Achieve high Sharpe ratio in a high-volatility market.",
        "max_steps": 100,
        "grader": sharpe_grader
    },
    {
        "id": "trading_crash_v1",
        "description": "Survive and recover from a sudden mid-episode crash.",
        "max_steps": 100,
        "grader": risk_adjusted_grader
    }
]

def get_task_by_id(task_id: str):
    for task in TASKS:
        if task["id"] == task_id:
            return task
    return TASKS[0]
