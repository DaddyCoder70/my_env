from typing import Dict, Callable, Any

GRADER_REGISTRY: Dict[str, Callable[[str, dict], float]] = {}

def register_grader(task_id: str):
    def decorator(func: Callable[[str, dict], float]):
        GRADER_REGISTRY[task_id] = func
        return func
    return decorator

def grade_action(task_id: str, action: str, signals: dict) -> float:
    action = action.lower().strip()
    
    if action not in ("buy", "sell", "hold"):
        for a in ("buy", "sell", "hold"):
            if a in action:
                action = a
                break
        else:
            return 0.05

    grader_func = GRADER_REGISTRY.get(task_id)
    if not grader_func:
        return 0.5

    raw_score = grader_func(action, signals)
    return round(min(max(raw_score, 0.01), 0.99), 4)

@register_grader("trend_following")
def _grade_trend_following(action: str, signals: dict) -> float:
    momentum = signals.get("momentum", 0.5)
    trend = signals.get("trend", 0.5)
    macro = signals.get("macro", 0.5)
    signal_strength = 0.4 * momentum + 0.4 * trend + 0.2 * macro
    if action == "buy":
        return min(0.60 + signal_strength * 0.39, 0.99)
    elif action == "hold":
        return min(0.10 + (1 - signal_strength) * 0.20, 0.35)
    else:
        return max(0.01, 0.12 - signal_strength * 0.10)

@register_grader("bear_defense")
def _grade_bear_defense(action: str, signals: dict) -> float:
    macro = signals.get("macro", 0.5)
    momentum = signals.get("momentum", 0.5)
    bear_severity = 1.0 - (0.5 * momentum + 0.5 * macro)
    if action == "sell":
        return min(0.65 + 0.34 * bear_severity, 0.99)
    elif action == "hold":
        return min(0.30 + 0.20 * bear_severity, 0.60)
    else:
        return max(0.01, 0.15 - bear_severity * 0.13)

@register_grader("range_trading")
def _grade_range_trading(action: str, signals: dict) -> float:
    if action == "hold":
        return 0.92
    neutrality = 1.0 - abs(signals.get("momentum", 0.5) - 0.5) * 2
    return max(0.02, 0.28 - neutrality * 0.25)

@register_grader("macro_risk_filter")
def _grade_macro_risk(action: str, signals: dict) -> float:
    macro = signals.get("macro", 0.5)
    macro_deficit = max(0.45 - macro, 0.0)
    if action == "hold":
        return min(0.72 + macro_deficit * 2.8, 0.99)
    elif action == "sell":
        return min(0.50 + macro_deficit * 1.8, 0.88)
    else:
        return max(0.01, 0.12 - macro_deficit * 0.20)

@register_grader("breakout_momentum")
def _grade_breakout_momentum(action: str, signals: dict) -> float:
    volume_surge = signals.get("volume_surge", 0.6)
    price_vs_resistance = signals.get("price_vs_resistance", 0.7)
    strength = 0.5 * volume_surge + 0.5 * price_vs_resistance
    if action == "buy":
        return min(0.62 + strength * 0.37, 0.99)
    elif action == "hold":
        return min(0.18 + (1 - strength) * 0.20, 0.40)
    else:
        return max(0.01, 0.12 - strength * 0.10)

@register_grader("volatile_range")
def _grade_volatile_range(action: str, signals: dict) -> float:
    volatility = signals.get("volatility", 0.5)
    if action == "hold":
        return min(0.68 + volatility * 0.30, 0.99)
    elif action == "sell":
        return max(0.05, 0.22 - volatility * 0.15)
    else:
        return max(0.02, 0.15 - volatility * 0.12)

@register_grader("recovery_play")
def _grade_recovery_play(action: str, signals: dict) -> float:
    rsi_recovery = signals.get("rsi_recovery", 0.5)
    momentum_turn = signals.get("momentum_turn", 0.5)
    signal_strength = 0.6 * rsi_recovery + 0.4 * momentum_turn
    if action == "buy":
        return min(0.58 + signal_strength * 0.40, 0.99)
    elif action == "hold":
        return min(0.30 + (1 - signal_strength) * 0.25, 0.55)
    else:
        return max(0.01, 0.12 - signal_strength * 0.10)

@register_grader("sector_rotation")
def _grade_sector_rotation(action: str, signals: dict) -> float:
    rs_improving = signals.get("relative_strength", 0.6)
    flow_score = signals.get("institutional_flow", 0.6)
    signal_strength = 0.55 * rs_improving + 0.45 * flow_score
    if action == "buy":
        return min(0.58 + signal_strength * 0.40, 0.99)
    elif action == "hold":
        return min(0.22 + (1 - signal_strength) * 0.22, 0.45)
    else:
        return max(0.01, 0.12 - signal_strength * 0.10)
