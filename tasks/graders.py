# tasks/graders.py
# Reward functions for each task. All rewards are in [0.0, 1.0].


def grade_action(task_id: str, action: str, signals: dict) -> float:
    """
    Score a single action for a given task and signal state.
    Returns a float in [0.0, 1.0].
    """
    action = action.lower().strip()
    # Normalise any variant spellings the LLM might emit
    if action not in ("buy", "sell", "hold"):
        # Try partial match
        for a in ("buy", "sell", "hold"):
            if a in action:
                action = a
                break
        else:
            return 0.1  # unrecognised action — small non-zero to avoid 0-reward crashes

    raw_score = 0.5
    if task_id == "trend_following":
        raw_score = _grade_trend_following(action, signals)
    elif task_id == "bear_defense":
        raw_score = _grade_bear_defense(action, signals)
    elif task_id == "range_trading":
        raw_score = _grade_range_trading(action, signals)
    elif task_id == "macro_risk_filter":
        raw_score = _grade_macro_risk(action, signals)

    # OpenEnv requirement: scores must be strictly in (0.0, 1.0)
    return round(min(max(raw_score, 0.01), 0.99), 3)


# ---------------------------------------------------------------------------
# Task-specific graders
# ---------------------------------------------------------------------------

def _grade_trend_following(action: str, signals: dict) -> float:
    """
    Bull market: strong momentum + trend + supportive macro.
    Correct action: BUY.
    """
    momentum = signals.get("momentum", 0.5)
    trend = signals.get("trend", 0.5)
    macro = signals.get("macro", 0.5)

    # Signal strength drives the reward magnitude for a correct BUY
    signal_strength = 0.4 * momentum + 0.4 * trend + 0.2 * macro

    if action == "buy":
        return round(min(signal_strength * 1.25, 1.0), 3)
    elif action == "hold":
        return round(signal_strength * 0.25, 3)   # very partial credit — missed the move
    else:  # sell
        return 0.0                                  # wrong direction


def _grade_bear_defense(action: str, signals: dict) -> float:
    """
    Bear market: low momentum + low macro + high volatility.
    Correct action: SELL (full marks) or HOLD (partial).
    Buying into a bear = 0.
    """
    macro = signals.get("macro", 0.5)
    momentum = signals.get("momentum", 0.5)

    # How bad is the environment?  0 = mild, 1 = extreme bear
    bear_severity = 1.0 - (0.5 * momentum + 0.5 * macro)

    if action == "sell":
        return round(min(0.65 + 0.35 * bear_severity, 1.0), 3)
    elif action == "hold":
        return round(min(0.35 + 0.20 * bear_severity, 0.65), 3)
    else:  # buy
        return 0.0


def _grade_range_trading(action: str, signals: dict) -> float:
    """
    Sideways / uncertain market: no clear edge.
    Correct action: HOLD (preserve capital, avoid chop).
    Acting (buy or sell) is penalised proportionally to how neutral the signals are.
    """
    if action == "hold":
        return 1.0

    # How far from neutral are the signals?  If truly neutral, acting is very wrong.
    neutrality = 1.0 - abs(signals.get("momentum", 0.5) - 0.5) * 2
    penalty = neutrality * 0.9   # near-neutral → near-zero reward for acting
    return round(max(0.1, 0.1 + (1 - penalty) * 0.2), 3)


def _grade_macro_risk(action: str, signals: dict) -> float:
    """
    Macro gate triggered (macro < 0.45): technicals may look OK but macro vetoes trading.
    Correct action: HOLD (capital preservation) or SELL (exit).
    Buying when macro gate is triggered = 0.
    """
    macro = signals.get("macro", 0.5)
    macro_deficit = max(0.45 - macro, 0.0)   # how far below the safety gate

    if action == "hold":
        # More reward the further below the gate we are (more obvious the risk)
        return round(min(0.75 + macro_deficit * 2.5, 1.0), 3)
    elif action == "sell":
        return round(min(0.55 + macro_deficit * 1.5, 0.90), 3)
    else:  # buy
        return 0.0
