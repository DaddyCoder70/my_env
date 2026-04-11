# tasks/graders.py
# Reward functions for each task.
# ALL rewards are strictly in the open interval (0.01, 0.99) as required by OpenEnv.
# No grader function may return 0.0 or 1.0 — use 0.01 and 0.99 as hard bounds.


def grade_action(task_id: str, action: str, signals: dict) -> float:
    """
    Score a single trading action for a given task and market signal state.

    Reward contract:
      - Correct action in ideal conditions → up to 0.99
      - Partially correct action           → 0.30 – 0.70 depending on context
      - Wrong action in extreme conditions → as low as 0.01

    Returns:
        float strictly in (0.01, 0.99)
    """
    action = action.lower().strip()

    # Normalise variant spellings the LLM might emit (e.g. "buying", "BUY NOW")
    if action not in ("buy", "sell", "hold"):
        for a in ("buy", "sell", "hold"):
            if a in action:
                action = a
                break
        else:
            # Completely unrecognised — give minimal score, don't crash
            return 0.05

    raw_score = 0.5
    if task_id == "trend_following":
        raw_score = _grade_trend_following(action, signals)
    elif task_id == "bear_defense":
        raw_score = _grade_bear_defense(action, signals)
    elif task_id == "range_trading":
        raw_score = _grade_range_trading(action, signals)
    elif task_id == "macro_risk_filter":
        raw_score = _grade_macro_risk(action, signals)
    elif task_id == "breakout_momentum":
        raw_score = _grade_breakout_momentum(action, signals)
    elif task_id == "volatile_range":
        raw_score = _grade_volatile_range(action, signals)
    elif task_id == "recovery_play":
        raw_score = _grade_recovery_play(action, signals)
    elif task_id == "sector_rotation":
        raw_score = _grade_sector_rotation(action, signals)

    # Hard clamp: strictly in (0.01, 0.99) as required by OpenEnv spec
    return round(min(max(raw_score, 0.01), 0.99), 4)


# ---------------------------------------------------------------------------
# Original 4 task graders — fixed to remove 0.0 returns
# ---------------------------------------------------------------------------

def _grade_trend_following(action: str, signals: dict) -> float:
    """
    Bull market: strong momentum + trend + supportive macro.
    Correct action: BUY.
    HOLD is mildly penalised (missed opportunity).
    SELL is strongly penalised (wrong direction).
    """
    momentum = signals.get("momentum", 0.5)
    trend = signals.get("trend", 0.5)
    macro = signals.get("macro", 0.5)
    signal_strength = 0.4 * momentum + 0.4 * trend + 0.2 * macro

    if action == "buy":
        return min(0.60 + signal_strength * 0.39, 0.99)
    elif action == "hold":
        # Missed the move — partial credit proportional to signal weakness
        return min(0.10 + (1 - signal_strength) * 0.20, 0.35)
    else:  # sell — wrong direction in a bull market
        # Severity depends on how strong the bull signal is
        return max(0.01, 0.12 - signal_strength * 0.10)


def _grade_bear_defense(action: str, signals: dict) -> float:
    """
    Bear market: low momentum + low macro + high volatility.
    Correct action: SELL (capital protection).
    HOLD gets partial credit.
    BUY is penalised — severity scales with bear intensity.
    """
    macro = signals.get("macro", 0.5)
    momentum = signals.get("momentum", 0.5)
    bear_severity = 1.0 - (0.5 * momentum + 0.5 * macro)  # 0=mild, 1=extreme

    if action == "sell":
        return min(0.65 + 0.34 * bear_severity, 0.99)
    elif action == "hold":
        return min(0.30 + 0.20 * bear_severity, 0.60)
    else:  # buy into a bear — penalised harder the more severe the bear
        return max(0.01, 0.15 - bear_severity * 0.13)


def _grade_range_trading(action: str, signals: dict) -> float:
    """
    Sideways / uncertain market: no clear directional edge.
    Correct action: HOLD (preserve capital, avoid whipsaws).
    Acting (buy or sell) is penalised proportionally to signal neutrality.
    """
    if action == "hold":
        return 0.92

    # How far from neutral are the signals? Near-neutral = acting is very wrong.
    neutrality = 1.0 - abs(signals.get("momentum", 0.5) - 0.5) * 2
    # High neutrality (0.9) → acting earns ~0.05; low neutrality (0.1) → ~0.25
    return max(0.02, round(0.28 - neutrality * 0.25, 4))


def _grade_macro_risk(action: str, signals: dict) -> float:
    """
    Macro gate triggered (macro < 0.45): technicals may look OK but macro vetoes trading.
    Correct action: HOLD (capital preservation).
    SELL is also acceptable.
    BUY when macro gate is triggered = very wrong.
    """
    macro = signals.get("macro", 0.5)
    macro_deficit = max(0.45 - macro, 0.0)   # how far below the safety gate

    if action == "hold":
        # More reward the further below the gate == more obvious the risk
        return min(0.72 + macro_deficit * 2.8, 0.99)
    elif action == "sell":
        return min(0.50 + macro_deficit * 1.8, 0.88)
    else:  # buy when macro vetoes — wrong
        return max(0.01, 0.12 - macro_deficit * 0.20)


# ---------------------------------------------------------------------------
# 4 new task graders
# ---------------------------------------------------------------------------

def _grade_breakout_momentum(action: str, signals: dict) -> float:
    """
    Price breaking above long-term resistance with volume surge.
    Correct action: BUY (ride the breakout).
    HOLD is neutral — not wrong but misses opportunity.
    SELL into a breakout = wrong.
    """
    volume_surge = signals.get("volume_surge", 0.6)
    price_vs_resistance = signals.get("price_vs_resistance", 0.7)
    strength = 0.5 * volume_surge + 0.5 * price_vs_resistance

    if action == "buy":
        return min(0.62 + strength * 0.37, 0.99)
    elif action == "hold":
        return min(0.18 + (1 - strength) * 0.20, 0.40)
    else:  # sell into breakout
        return max(0.01, 0.12 - strength * 0.10)


def _grade_volatile_range(action: str, signals: dict) -> float:
    """
    High-volatility sideways chop: wide swings, no clear direction.
    Correct action: HOLD (avoid being whipsawed).
    Any directional bet is risky.
    """
    volatility = signals.get("volatility", 0.5)
    if action == "hold":
        return min(0.68 + volatility * 0.30, 0.99)
    elif action == "sell":
        # Slight preference for sell vs buy in choppy conditions
        return max(0.05, 0.22 - volatility * 0.15)
    else:  # buy into volatile chop
        return max(0.02, 0.15 - volatility * 0.12)


def _grade_recovery_play(action: str, signals: dict) -> float:
    """
    Stock recovering from oversold levels: RSI low but momentum turning positive.
    Correct action: BUY (early recovery, contrarian entry).
    HOLD is acceptable — conservative.
    SELL at bottom = wrong.
    """
    rsi_recovery = signals.get("rsi_recovery", 0.5)   # 1.0 = deeply oversold, recovering
    momentum_turn = signals.get("momentum_turn", 0.5)
    signal_strength = 0.6 * rsi_recovery + 0.4 * momentum_turn

    if action == "buy":
        return min(0.58 + signal_strength * 0.40, 0.99)
    elif action == "hold":
        return min(0.30 + (1 - signal_strength) * 0.25, 0.55)
    else:  # sell at bottom
        return max(0.01, 0.12 - signal_strength * 0.10)


def _grade_sector_rotation(action: str, signals: dict) -> float:
    """
    Capital rotating INTO this sector: relative strength improving,
    but technical signals just starting to confirm.
    Correct action: BUY (early rotation entry).
    HOLD = conservative but underperformance risk.
    SELL = wrong direction.
    """
    rs_improving = signals.get("relative_strength", 0.6)
    flow_score = signals.get("institutional_flow", 0.6)
    signal_strength = 0.55 * rs_improving + 0.45 * flow_score

    if action == "buy":
        return min(0.58 + signal_strength * 0.40, 0.99)
    elif action == "hold":
        return min(0.22 + (1 - signal_strength) * 0.22, 0.45)
    else:  # sell during sector inflow
        return max(0.01, 0.12 - signal_strength * 0.10)
