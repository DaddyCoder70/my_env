# tasks/definitions.py
# Pre-computed synthetic task observations — no live API calls needed during grading.

TASKS = {
    "trend_following": {
        "description": "Identify and follow a strong uptrend in bullish momentum markets",
        "ideal_action": "buy",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — RELIANCE:\n"
                    "Current regime: Bull market. EMA-20 is significantly above EMA-50.\n"
                    "Momentum score: 0.82 (strong buying pressure over last 14 days).\n"
                    "Trend score: 0.79 (price structure clearly upward, persistence high).\n"
                    "Volatility score: 0.71 (conditions relatively calm, ATR in lower third).\n"
                    "Macro environment score: 0.68 (India GDP growth stable, FII flows positive, INR steady).\n"
                    "Signal agreement: 0.77 (technical signals broadly aligned).\n"
                    "Institutional investors are net buyers. Sector tailwinds present.\n"
                    "Confidence: 0.74. Rule-based strategy: trend_following. Trade: ALLOWED.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.82, "trend": 0.79, "volatility": 0.71,
                    "macro": 0.68, "regime": "bull", "vol_regime": "low",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — TCS:\n"
                    "Regime: Bull. Price above EMA-20 for 18 of last 20 sessions.\n"
                    "Momentum score: 0.76 (RSI elevated, buyers clearly in control).\n"
                    "Trend score: 0.81 (strong slope, EMA alignment fully confirmed).\n"
                    "Volatility score: 0.68 (ATR percentile in lower third, clean price action).\n"
                    "Macro score: 0.72 (strong quarterly results, EPS trajectory positive).\n"
                    "DII flows: net buying. IT sector outperforming the index.\n"
                    "Confidence: 0.78. Strategy: trend_following. Trade: ALLOWED.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.76, "trend": 0.81, "volatility": 0.68,
                    "macro": 0.72, "regime": "bull", "vol_regime": "low",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — INFY:\n"
                    "Regime: Bull. EMA-50 above EMA-200 (golden cross confirmed 12 sessions ago).\n"
                    "Momentum score: 0.79 (smooth RSI trending upward for 3 weeks).\n"
                    "Trend score: 0.74 (slope positive, price above EMA-20 with 85% persistence).\n"
                    "Volatility score: 0.73 (low ATR environment, no headline noise).\n"
                    "Macro score: 0.65 (policy environment stable, US client spend recovering).\n"
                    "Confidence: 0.74. Strategy: trend_following. Trade: ALLOWED.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.79, "trend": 0.74, "volatility": 0.73,
                    "macro": 0.65, "regime": "bull", "vol_regime": "medium",
                    "ideal_action": "buy",
                },
            },
        ],
    },

    "bear_defense": {
        "description": "Protect capital during clear downtrends and bear market conditions",
        "ideal_action": "sell",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — ADANIENT:\n"
                    "Current regime: Bear market. EMA-50 crossed below EMA-200 (death cross) 8 sessions ago.\n"
                    "Momentum score: 0.22 (heavy selling pressure, RSI below 35).\n"
                    "Trend score: 0.19 (price consistently below EMA-20, negative slope confirmed).\n"
                    "Volatility score: 0.31 (ATR elevated, choppy and dangerous price action).\n"
                    "Macro score: 0.41 (geopolitical tensions elevated, FII outflows continuing).\n"
                    "Confidence: 0.28. Rule-based: no_opinion. Trade: NOT ALLOWED.\n"
                    "Macro gate breached. Capital preservation is primary objective.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.22, "trend": 0.19, "volatility": 0.31,
                    "macro": 0.41, "regime": "bear", "vol_regime": "high",
                    "ideal_action": "sell",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — ZOMATO:\n"
                    "Regime: Bear. Price broke critical support. Selling is accelerating.\n"
                    "Momentum score: 0.18 (RSI collapsing, momentum deeply negative).\n"
                    "Trend score: 0.21 (all moving average alignments bearish).\n"
                    "Volatility score: 0.27 (ATR at 80th percentile — chaotic conditions).\n"
                    "Macro score: 0.38 (consumer discretionary under pressure, inflation hurting margins).\n"
                    "FII: net sellers for 12 consecutive sessions. Sentiment: extreme risk-off.\n"
                    "Trade: NOT ALLOWED. Downside risk far outweighs any potential reward.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.18, "trend": 0.21, "volatility": 0.27,
                    "macro": 0.38, "regime": "bear", "vol_regime": "high",
                    "ideal_action": "sell",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — PAYTM:\n"
                    "Regime: Bear. Persistent selling with no reversal signals visible.\n"
                    "Momentum score: 0.25 (no bounce, selling pressure dominant).\n"
                    "Trend score: 0.17 (deeply bearish structure across all timeframes).\n"
                    "Volatility score: 0.29 (high noise environment).\n"
                    "Macro score: 0.35 (regulatory risk elevated, earnings missing estimates badly).\n"
                    "Confidence: 0.21. Rule-based: no_opinion. Trade: NOT ALLOWED.\n"
                    "Holding long positions in this environment is a capital destruction risk.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.25, "trend": 0.17, "volatility": 0.29,
                    "macro": 0.35, "regime": "bear", "vol_regime": "high",
                    "ideal_action": "sell",
                },
            },
        ],
    },

    "range_trading": {
        "description": "Identify sideways, directionless markets and avoid committing capital",
        "ideal_action": "hold",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — HDFCBANK:\n"
                    "Regime: Range (sideways). EMA-50 and EMA-200 within 0.5% of each other.\n"
                    "Momentum score: 0.51 (neutral — neither buyers nor sellers dominant).\n"
                    "Trend score: 0.48 (no clear direction, slope near flat for 4 weeks).\n"
                    "Volatility score: 0.55 (medium volatility, indecisive price action).\n"
                    "Macro score: 0.53 (mixed signals — some positives offset by external risks).\n"
                    "Uncertain flag: TRUE (both momentum and trend in 0.45-0.55 neutral zone).\n"
                    "Strategy: no_opinion. Confidence: 0.49 — below 0.60 threshold. Trade: NOT ALLOWED.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.51, "trend": 0.48, "volatility": 0.55,
                    "macro": 0.53, "regime": "range", "vol_regime": "medium",
                    "uncertain": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — AXISBANK:\n"
                    "Regime: Range. Stock oscillating in a tight band for 6 weeks.\n"
                    "Momentum score: 0.49 (neutral RSI, no trend establishment).\n"
                    "Trend score: 0.52 (flat alignment, price crossing EMA-20 repeatedly both ways).\n"
                    "Volatility score: 0.58 (medium noise, difficult to extract clean signal).\n"
                    "Macro score: 0.56 (broadly neutral macro backdrop).\n"
                    "Uncertain flag: TRUE. No strategy recommended.\n"
                    "Entering now has negative expected value due to chop and transaction costs.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.49, "trend": 0.52, "volatility": 0.58,
                    "macro": 0.56, "regime": "range", "vol_regime": "medium",
                    "uncertain": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — ITC:\n"
                    "Regime: Range. No sustained direction established for 30 days.\n"
                    "Momentum score: 0.53. Trend score: 0.47.\n"
                    "Macro score: 0.57 (stable but uninspiring).\n"
                    "Signal agreement: 0.41 (low — signals conflicting with each other).\n"
                    "No institutional conviction visible. Volume declining — participation dropping.\n"
                    "Strategy: no_opinion. Confidence: 0.46. Trade: NOT ALLOWED.\n"
                    "Patience is the correct response in range-bound markets.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.53, "trend": 0.47, "volatility": 0.60,
                    "macro": 0.57, "regime": "range", "vol_regime": "medium",
                    "ideal_action": "hold",
                },
            },
        ],
    },

    "macro_risk_filter": {
        "description": "Apply macro risk gate when macro score drops below 0.45, overriding technical signals",
        "ideal_action": "hold",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — TATASTEEL:\n"
                    "Technical signals appear mixed-to-positive.\n"
                    "Momentum score: 0.61. Trend score: 0.58.\n"
                    "HOWEVER — Macro environment is critically deteriorating:\n"
                    "  Macro score: 0.38 (BELOW the 0.45 safety threshold).\n"
                    "  Geopolitical Volatility: 0.15 (escalating border tensions).\n"
                    "  US Policy Impact: 0.20 (aggressive Fed, strong dollar hammering EMs).\n"
                    "  Forex: 0.25 (INR weakening sharply vs USD).\n"
                    "  FII flows: heavy outflows — $800M net sold last week.\n"
                    "Rule: macro < 0.45 → trade NOT ALLOWED, regardless of technical strength.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.61, "trend": 0.58, "volatility": 0.60,
                    "macro": 0.38, "regime": "range", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — COALINDIA:\n"
                    "Technicals: moderate positives. Momentum: 0.64. Trend: 0.60.\n"
                    "MACRO ALERT — gate triggered:\n"
                    "  Macro score: 0.41 (BELOW 0.45 gate).\n"
                    "  Natural Calamity risk elevated (monsoon failure, supply disruption).\n"
                    "  Government policy risk: 0.22 (pending regulatory review outcome).\n"
                    "  Investor Sentiment: 0.30 (fear dominant, India VIX elevated).\n"
                    "Technical signals look acceptable, but the macro gate overrides everything.\n"
                    "Capital preservation mode is mandatory when macro < 0.45.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.64, "trend": 0.60, "volatility": 0.52,
                    "macro": 0.41, "regime": "bull", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — NIFTY50:\n"
                    "India experiencing sharp FII outflows ($1.2B in 3 days). Sentiment deteriorating.\n"
                    "Momentum: 0.55 (neutral-ish). Trend: 0.57 (slight positive).\n"
                    "Macro score: 0.40 (below 0.45 gate):\n"
                    "  Banking system stress indicators rising.\n"
                    "  International Relations: 0.20 (trade war escalation risk).\n"
                    "  Economic Strength: 0.45 (slowing GDP prints, PMI softening).\n"
                    "Macro gate breached. Even with neutral-to-positive technicals,\n"
                    "the macro environment makes trading inadvisable.\n"
                    "Decide: BUY, SELL, or HOLD."
                ),
                "signals": {
                    "momentum": 0.55, "trend": 0.57, "volatility": 0.50,
                    "macro": 0.40, "regime": "range", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
        ],
    },
}

TASK_NAMES = list(TASKS.keys())
