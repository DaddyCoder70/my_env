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
                    "EMA-20 vs EMA-50: +4.2%\n"
                    "Momentum score: 0.82\n"
                    "Trend score: 0.79\n"
                    "Volatility score: 0.71\n"
                    "Macro environment score: 0.68\n"
                    "Signal agreement: 0.77\n"
                    "Institutional flows: Positive\n"
                    "Sector Relative Strength: Positive\n"
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
                    "Price vs EMA-20: +2.1%\n"
                    "Momentum score: 0.76\n"
                    "Trend score: 0.81\n"
                    "Volatility score: 0.68\n"
                    "Macro score: 0.72\n"
                    "DII flows: Positive\n"
                    "Sector Relative Strength: Outperforming\n"
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
                    "EMA-50 vs EMA-200: +3.4%\n"
                    "Momentum score: 0.79\n"
                    "Trend score: 0.74\n"
                    "Volatility score: 0.73\n"
                    "Macro score: 0.65\n"
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
                    "EMA-50 vs EMA-200: -4.1%\n"
                    "Momentum score: 0.22\n"
                    "Trend score: 0.19\n"
                    "Volatility score: 0.31\n"
                    "Macro score: 0.41\n"
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
                    "Price vs Support: -1.2%\n"
                    "Momentum score: 0.18\n"
                    "Trend score: 0.21\n"
                    "Volatility score: 0.27\n"
                    "Macro score: 0.38\n"
                    "FII Flows: Negative for 12 sessions\n"
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
                    "Price vs EMA-20: -12.4%\n"
                    "Momentum score: 0.25\n"
                    "Trend score: 0.17\n"
                    "Volatility score: 0.29\n"
                    "Macro score: 0.35\n"
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
                    "EMA-50 vs EMA-200: +0.2%\n"
                    "Momentum score: 0.51\n"
                    "Trend score: 0.48\n"
                    "Volatility score: 0.55\n"
                    "Macro score: 0.53\n"
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
                    "Price vs Bollinger Mid-Band: +0.1%\n"
                    "Momentum score: 0.49\n"
                    "Trend score: 0.52\n"
                    "Volatility score: 0.58\n"
                    "Macro score: 0.56\n"
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
                    "Price vs EMA-20: -0.3%\n"
                    "Momentum score: 0.53\n"
                    "Trend score: 0.47\n"
                    "Volatility score: 0.60\n"
                    "Macro score: 0.57\n"
                    "Signal agreement: 0.41\n"
                    "Volume Trend: Declining\n"
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
                    "Momentum score: 0.61\n"
                    "Trend score: 0.58\n"
                    "Volatility score: 0.60\n"
                    "Macro score: 0.38\n"
                    "Geopolitical score: 0.15\n"
                    "Forex score: 0.25\n"
                    "FII flows: -$800M\n"
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
                    "Momentum score: 0.64\n"
                    "Trend score: 0.60\n"
                    "Volatility score: 0.52\n"
                    "Macro score: 0.41\n"
                    "Govt Policy score: 0.22\n"
                    "Sentiment score: 0.30\n"
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
                    "Momentum score: 0.55\n"
                    "Trend score: 0.57\n"
                    "Volatility score: 0.50\n"
                    "Macro score: 0.40\n"
                    "Int'l Relations score: 0.20\n"
                    "Economic Strength score: 0.45\n"
                    "FII outflows: -$1.2B\n"
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
