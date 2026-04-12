TASKS = {
    "trend_following": {
        "description": "Identify and follow a strong uptrend in bullish momentum markets",
        "ideal_action": "buy",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — RELIANCE (NSE):\n"
                    "EMA-20 vs EMA-50: +4.2%  |  Price vs 52W High: -3.1%\n"
                    "Momentum score: 0.82  |  Trend score: 0.79\n"
                    "Volatility score: 0.71  |  Macro environment score: 0.68\n"
                    "Signal agreement: 0.77  |  FII Flows: +$320M (5-day)\n"
                    "Institutional flows: Positive  |  Sector RSI: Outperforming Nifty50"
                ),
                "signals": {
                    "momentum": 0.82, "trend": 0.79, "volatility": 0.71,
                    "macro": 0.68, "regime": "bull", "vol_regime": "low",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — TCS (NSE):\n"
                    "Price vs EMA-20: +2.1%  |  EMA-50 crossover: 8 days ago\n"
                    "Momentum score: 0.76  |  Trend score: 0.81\n"
                    "Volatility score: 0.68  |  Macro score: 0.72\n"
                    "DII flows: Positive for 7 consecutive sessions\n"
                    "Sector: IT — Outperforming Nifty50 by 3.2% YTD"
                ),
                "signals": {
                    "momentum": 0.76, "trend": 0.81, "volatility": 0.68,
                    "macro": 0.72, "regime": "bull", "vol_regime": "low",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — INFY (NSE):\n"
                    "EMA-50 vs EMA-200: +3.4%  |  MACD: Positive crossover\n"
                    "Momentum score: 0.79  |  Trend score: 0.74\n"
                    "Volatility score: 0.73  |  Macro score: 0.65\n"
                    "Bollinger Band: Price near upper band, sustained\n"
                    "Volume: 40% above 20-day average"
                ),
                "signals": {
                    "momentum": 0.79, "trend": 0.74, "volatility": 0.73,
                    "macro": 0.65, "regime": "bull", "vol_regime": "medium",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — HCLTECH (NSE):\n"
                    "Price vs EMA-20: +1.8%  |  ADX: 28 (trending)\n"
                    "Momentum score: 0.74  |  Trend score: 0.78\n"
                    "Volatility score: 0.69  |  Macro score: 0.70\n"
                    "RSI-14: 62 (overbought territory not yet reached)\n"
                    "Sector: IT — strong earnings revision cycle"
                ),
                "signals": {
                    "momentum": 0.74, "trend": 0.78, "volatility": 0.69,
                    "macro": 0.70, "regime": "bull", "vol_regime": "low",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — WIPRO (NSE):\n"
                    "EMA-20 vs EMA-50: +2.7%  |  Consecutive higher highs: 6\n"
                    "Momentum score: 0.77  |  Trend score: 0.75\n"
                    "Volatility score: 0.64  |  Macro score: 0.71\n"
                    "Signal agreement across indicators: 0.80\n"
                    "Foreign portfolio: Net buyer for 12 of last 15 sessions"
                ),
                "signals": {
                    "momentum": 0.77, "trend": 0.75, "volatility": 0.64,
                    "macro": 0.71, "regime": "bull", "vol_regime": "low",
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
                    "Market Analysis Report — ADANIENT (NSE):\n"
                    "EMA-50 vs EMA-200: -4.1%  |  Death cross: 14 days ago\n"
                    "Momentum score: 0.22  |  Trend score: 0.19\n"
                    "Volatility score: 0.31  |  Macro score: 0.41\n"
                    "FII flows: -$420M (10 sessions)  |  Sector: Underperforming"
                ),
                "signals": {
                    "momentum": 0.22, "trend": 0.19, "volatility": 0.31,
                    "macro": 0.41, "regime": "bear", "vol_regime": "high",
                    "ideal_action": "sell",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — ZOMATO (NSE):\n"
                    "Price vs Support: -1.2%  |  Support level broken: 3 sessions ago\n"
                    "Momentum score: 0.18  |  Trend score: 0.21\n"
                    "Volatility score: 0.27  |  Macro score: 0.38\n"
                    "FII Flows: Negative for 12 consecutive sessions\n"
                    "RSI-14: 32 — oversold but no bounce signal yet"
                ),
                "signals": {
                    "momentum": 0.18, "trend": 0.21, "volatility": 0.27,
                    "macro": 0.38, "regime": "bear", "vol_regime": "high",
                    "ideal_action": "sell",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — PAYTM (NSE):\n"
                    "Price vs EMA-20: -12.4%  |  52-week low: breached\n"
                    "Momentum score: 0.25  |  Trend score: 0.17\n"
                    "Volatility score: 0.29  |  Macro score: 0.35\n"
                    "Regulatory headwinds: Active  |  Short interest: Rising\n"
                    "Analyst revisions: 4 downgrades in last 30 days"
                ),
                "signals": {
                    "momentum": 0.25, "trend": 0.17, "volatility": 0.29,
                    "macro": 0.35, "regime": "bear", "vol_regime": "high",
                    "ideal_action": "sell",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — NYKAA (NSE):\n"
                    "EMA-50 vs EMA-200: -6.2%  |  MACD: Negative divergence\n"
                    "Momentum score: 0.20  |  Trend score: 0.22\n"
                    "Volatility score: 0.26  |  Macro score: 0.40\n"
                    "Consecutive lower locals: 7  |  Volume: Elevated on red days\n"
                    "Lock-in expiry overhang: High"
                ),
                "signals": {
                    "momentum": 0.20, "trend": 0.22, "volatility": 0.26,
                    "macro": 0.40, "regime": "bear", "vol_regime": "high",
                    "ideal_action": "sell",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — POLICYBZR (NSE):\n"
                    "Price vs EMA-20: -8.9%  |  Bear flag: Forming\n"
                    "Momentum score: 0.23  |  Trend score: 0.18\n"
                    "Volatility score: 0.30  |  Macro score: 0.37\n"
                    "Nifty correlation: High  |  Nifty trend: Bearish\n"
                    "Promoter holding: Decreased (latest filing)"
                ),
                "signals": {
                    "momentum": 0.23, "trend": 0.18, "volatility": 0.30,
                    "macro": 0.37, "regime": "bear", "vol_regime": "high",
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
                    "Market Analysis Report — HDFCBANK (NSE):\n"
                    "EMA-50 vs EMA-200: +0.2%  |  Bollinger Band width: Contracted\n"
                    "Momentum score: 0.51  |  Trend score: 0.48\n"
                    "Volatility score: 0.55  |  Macro score: 0.53\n"
                    "Price oscillating near mid-band for 18 sessions\n"
                    "No significant catalyst expected short-term"
                ),
                "signals": {
                    "momentum": 0.51, "trend": 0.48, "volatility": 0.55,
                    "macro": 0.53, "regime": "range", "vol_regime": "medium",
                    "uncertain": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — AXISBANK (NSE):\n"
                    "Price vs Bollinger Mid-Band: +0.1%  |  ADX: 18 (weak trend)\n"
                    "Momentum score: 0.49  |  Trend score: 0.52\n"
                    "Volatility score: 0.58  |  Macro score: 0.56\n"
                    "RSI: 51 — neutral zone  |  MACD: Near zero line\n"
                    "Sector peers: Mixed signals"
                ),
                "signals": {
                    "momentum": 0.49, "trend": 0.52, "volatility": 0.58,
                    "macro": 0.56, "regime": "range", "vol_regime": "medium",
                    "uncertain": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — ITC (NSE):\n"
                    "Price vs EMA-20: -0.3%  |  Support/Resistance: Contained\n"
                    "Momentum score: 0.53  |  Trend score: 0.47\n"
                    "Volatility score: 0.60  |  Macro score: 0.57\n"
                    "Signal agreement: 0.41  |  Volume Trend: Declining\n"
                    "Analyst consensus: Neutral"
                ),
                "signals": {
                    "momentum": 0.53, "trend": 0.47, "volatility": 0.60,
                    "macro": 0.57, "regime": "range", "vol_regime": "medium",
                    "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — TATAMOTORS (NSE):\n"
                    "EMA-50 vs EMA-200: -0.4%  |  Consecutive doji candles: 5\n"
                    "Momentum score: 0.50  |  Trend score: 0.50\n"
                    "Volatility score: 0.54  |  Macro score: 0.52\n"
                    "Volume: Below 20-day average  |  Options OI: Balanced\n"
                    "Sector headwinds and tailwinds roughly equal"
                ),
                "signals": {
                    "momentum": 0.50, "trend": 0.50, "volatility": 0.54,
                    "macro": 0.52, "regime": "range", "vol_regime": "medium",
                    "uncertain": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — MARUTI (NSE):\n"
                    "Price vs EMA-20: +0.5%  |  Resistance: Strong at current level\n"
                    "Momentum score: 0.52  |  Trend score: 0.49\n"
                    "Volatility score: 0.57  |  Macro score: 0.55\n"
                    "Bull/Bear volume ratio: 1.02 (neutral)\n"
                    "Earnings: In-line with estimates, no guidance change"
                ),
                "signals": {
                    "momentum": 0.52, "trend": 0.49, "volatility": 0.57,
                    "macro": 0.55, "regime": "range", "vol_regime": "medium",
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
                    "Market Analysis Report — TATASTEEL (NSE):\n"
                    "Momentum score: 0.61  |  Trend score: 0.58  (Technicals: Bullish)\n"
                    "Volatility score: 0.60  |  Macro score: 0.38  ⚠ BELOW GATE\n"
                    "Geopolitical risk score: 0.15  |  Forex stability: 0.25\n"
                    "FII flows: -$800M (global risk-off)  |  Crude oil: Spiking"
                ),
                "signals": {
                    "momentum": 0.61, "trend": 0.58, "volatility": 0.60,
                    "macro": 0.38, "regime": "range", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — COALINDIA (NSE):\n"
                    "Momentum score: 0.64  |  Trend score: 0.60  (Technicals: Bullish)\n"
                    "Volatility score: 0.52  |  Macro score: 0.41  ⚠ BELOW GATE\n"
                    "Government policy uncertainty score: 0.22\n"
                    "Global commodity demand: Weakening  |  Sentiment: Risk-off"
                ),
                "signals": {
                    "momentum": 0.64, "trend": 0.60, "volatility": 0.52,
                    "macro": 0.41, "regime": "bull", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — NIFTY50 INDEX:\n"
                    "Momentum score: 0.55  |  Trend score: 0.57  (Technicals: Neutral-Bullish)\n"
                    "Volatility score: 0.50  |  Macro score: 0.40  ⚠ BELOW GATE\n"
                    "International relations score: 0.20  |  Credit risk: Elevated\n"
                    "FII outflows: -$1.2B (last 5 sessions)  |  VIX: Rising"
                ),
                "signals": {
                    "momentum": 0.55, "trend": 0.57, "volatility": 0.50,
                    "macro": 0.40, "regime": "range", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — BAJFINANCE (NSE):\n"
                    "Momentum score: 0.62  |  Trend score: 0.65  (Technicals: Bullish)\n"
                    "Volatility score: 0.55  |  Macro score: 0.36  ⚠ BELOW GATE\n"
                    "Credit spreads: Widening  |  RBI policy: Uncertain\n"
                    "NBFC sector stress indicators: Elevated"
                ),
                "signals": {
                    "momentum": 0.62, "trend": 0.65, "volatility": 0.55,
                    "macro": 0.36, "regime": "bull", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — SUNPHARMA (NSE):\n"
                    "Momentum score: 0.67  |  Trend score: 0.62  (Technicals: Bullish)\n"
                    "Volatility score: 0.58  |  Macro score: 0.42  ⚠ BELOW GATE\n"
                    "USD/INR: Weak rupee headwind  |  Global risk appetite: Low\n"
                    "Regulatory overhang: WHO audit pending"
                ),
                "signals": {
                    "momentum": 0.67, "trend": 0.62, "volatility": 0.58,
                    "macro": 0.42, "regime": "bull", "vol_regime": "medium",
                    "macro_below_threshold": True, "ideal_action": "hold",
                },
            },
        ],
    },
    "breakout_momentum": {
        "description": "Identify and enter volume-confirmed price breakouts above long-term resistance",
        "ideal_action": "buy",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — DIXON (NSE):\n"
                    "Price action: Broke 52-week high on 3× average volume\n"
                    "Volume surge score: 0.88  |  Price vs resistance: +1.2%\n"
                    "Momentum score: 0.80  |  Trend score: 0.82\n"
                    "Institutional accumulation: Confirmed — block deal\n"
                    "Sector: Electronics manufacturing — strong order book"
                ),
                "signals": {
                    "volume_surge": 0.88, "price_vs_resistance": 0.82,
                    "momentum": 0.80, "trend": 0.82, "regime": "bull",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — POLYCAB (NSE):\n"
                    "Price action: Cleared 6-month consolidation range — gap up\n"
                    "Volume surge score: 0.79  |  Price vs resistance: +0.8%\n"
                    "Momentum score: 0.76  |  Trend score: 0.79\n"
                    "Relative strength vs Nifty: +4.2% (3-month)\n"
                    "Supply overhang: Cleared via large-block absorption"
                ),
                "signals": {
                    "volume_surge": 0.79, "price_vs_resistance": 0.78,
                    "momentum": 0.76, "trend": 0.79, "regime": "bull",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — KALYANKJIL (NSE):\n"
                    "Price action: Breakout from 18-month base — highest close in 2 years\n"
                    "Volume surge score: 0.85  |  Price vs resistance: +2.1%\n"
                    "Momentum score: 0.83  |  Trend score: 0.80\n"
                    "Fundamental trigger: Strong Q3 pre-release data\n"
                    "Options: Call OI buildup at next level"
                ),
                "signals": {
                    "volume_surge": 0.85, "price_vs_resistance": 0.80,
                    "momentum": 0.83, "trend": 0.80, "regime": "bull",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — CAMS (NSE):\n"
                    "Price action: Breakout — cleared 200-day EMA with strong follow-through\n"
                    "Volume surge score: 0.72  |  Price vs resistance: +1.5%\n"
                    "Momentum score: 0.75  |  Trend score: 0.77\n"
                    "MF industry tailwinds: SIP inflows at record\n"
                    "Earnings growth visibility: High"
                ),
                "signals": {
                    "volume_surge": 0.72, "price_vs_resistance": 0.75,
                    "momentum": 0.75, "trend": 0.77, "regime": "bull",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — APLAPOLLO (NSE):\n"
                    "Price action: Multi-year resistance cleared — high-volume close\n"
                    "Volume surge score: 0.81  |  Price vs resistance: +1.7%\n"
                    "Momentum score: 0.78  |  Trend score: 0.76\n"
                    "Infrastructure capex cycle: Beneficiary\n"
                    "Short covering: Significant — adds fuel to breakout"
                ),
                "signals": {
                    "volume_surge": 0.81, "price_vs_resistance": 0.77,
                    "momentum": 0.78, "trend": 0.76, "regime": "bull",
                    "ideal_action": "buy",
                },
            },
        ],
    },
    "volatile_range": {
        "description": "Navigate high-volatility choppy markets where no clear directional edge exists",
        "ideal_action": "hold",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — NIFTY BANK INDEX:\n"
                    "Day range: 1.8%  |  Weekly range: 4.3%  (Elevated)\n"
                    "Volatility score: 0.85  |  Trend score: 0.50\n"
                    "Momentum score: 0.48  |  Macro score: 0.54\n"
                    "RBI policy outcome: Uncertain  |  INR: Volatile\n"
                    "Intraday reversals: 3 in last 5 sessions"
                ),
                "signals": {
                    "volatility": 0.85, "trend": 0.50, "momentum": 0.48,
                    "macro": 0.54, "regime": "chop", "vol_regime": "extreme",
                    "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — NIFTY MIDCAP 100:\n"
                    "Intraday swings: ±2.1%  |  VIX: 22.4 (elevated)\n"
                    "Volatility score: 0.81  |  Trend score: 0.52\n"
                    "Momentum score: 0.51  |  Macro score: 0.50\n"
                    "Price: Oscillating between 200-DMA and 50-DMA\n"
                    "Breadth: Mixed — gainers-losers ratio near 1"
                ),
                "signals": {
                    "volatility": 0.81, "trend": 0.52, "momentum": 0.51,
                    "macro": 0.50, "regime": "chop", "vol_regime": "high",
                    "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — SAIL (NSE):\n"
                    "Intraday range: 3.2%  |  Close vs open: -0.1%\n"
                    "Volatility score: 0.78  |  Trend score: 0.49\n"
                    "Momentum score: 0.53  |  Macro score: 0.52\n"
                    "Commodity (steel) prices: Whipsawing on global data\n"
                    "Technical signals: Conflicting across timeframes"
                ),
                "signals": {
                    "volatility": 0.78, "trend": 0.49, "momentum": 0.53,
                    "macro": 0.52, "regime": "chop", "vol_regime": "high",
                    "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — INDIGO (NSE):\n"
                    "Week range: 6.1%  |  Gaps: 2 unfilled in last 10 sessions\n"
                    "Volatility score: 0.80  |  Trend score: 0.51\n"
                    "Momentum score: 0.49  |  Macro score: 0.53\n"
                    "Crude oil: Volatile  |  Jet fuel costs: Unpredictable\n"
                    "News flow: Mixed airline sector sentiment"
                ),
                "signals": {
                    "volatility": 0.80, "trend": 0.51, "momentum": 0.49,
                    "macro": 0.53, "regime": "chop", "vol_regime": "high",
                    "ideal_action": "hold",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — PNB (NSE):\n"
                    "Volatility score: 0.83  |  Trend score: 0.48\n"
                    "Momentum score: 0.52  |  Macro score: 0.51\n"
                    "PSU bank news: Mixed — regulatory and NPL headlines\n"
                    "10-yr yield: Volatile  |  Spread environment: Uncertain\n"
                    "Hourly chart: Multiple false breakouts and breakdowns"
                ),
                "signals": {
                    "volatility": 0.83, "trend": 0.48, "momentum": 0.52,
                    "macro": 0.51, "regime": "chop", "vol_regime": "extreme",
                    "ideal_action": "hold",
                },
            },
        ],
    },
    "recovery_play": {
        "description": "Identify and enter stocks recovering from deeply oversold conditions",
        "ideal_action": "buy",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — IRCTC (NSE):\n"
                    "RSI-14: 24 (deeply oversold)  |  Momentum reversal: Forming\n"
                    "RSI recovery score: 0.78  |  Momentum turn score: 0.65\n"
                    "Trend score: 0.38  |  Macro score: 0.58\n"
                    "Price vs 52W Low: +2.3% — bouncing off support\n"
                    "Valuation: 28% below historical median"
                ),
                "signals": {
                    "rsi_recovery": 0.78, "momentum_turn": 0.65,
                    "trend": 0.38, "macro": 0.58, "regime": "recovery",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — IDFC FIRST BANK (NSE):\n"
                    "RSI-14: 28 (oversold)  |  Hammer candle: Formed at support\n"
                    "RSI recovery score: 0.72  |  Momentum turn score: 0.60\n"
                    "Trend score: 0.35  |  Macro score: 0.62\n"
                    "Management buyback: Announced  |  Institutional re-entry: Signs"
                ),
                "signals": {
                    "rsi_recovery": 0.72, "momentum_turn": 0.60,
                    "trend": 0.35, "macro": 0.62, "regime": "recovery",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — MINDA CORP (NSE):\n"
                    "RSI-14: 22 (extremely oversold)  |  Bullish divergence: MACD\n"
                    "RSI recovery score: 0.82  |  Momentum turn score: 0.70\n"
                    "Trend score: 0.32  |  Macro score: 0.60\n"
                    "Sector catalyst: Auto sector policy tailwind announced\n"
                    "Selling pressure: Exhausted — volume declining on down-days"
                ),
                "signals": {
                    "rsi_recovery": 0.82, "momentum_turn": 0.70,
                    "trend": 0.32, "macro": 0.60, "regime": "recovery",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — NATIONALUM (NSE):\n"
                    "RSI-14: 26  |  Double bottom: Forming at key support\n"
                    "RSI recovery score: 0.75  |  Momentum turn score: 0.62\n"
                    "Trend score: 0.34  |  Macro score: 0.61\n"
                    "Global aluminium cycle: Turning  |  Demand outlook: Improving\n"
                    "FII accumulation: Emerging in last 3 sessions"
                ),
                "signals": {
                    "rsi_recovery": 0.75, "momentum_turn": 0.62,
                    "trend": 0.34, "macro": 0.61, "regime": "recovery",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — ASTER DM (NSE):\n"
                    "RSI-14: 25 (deeply oversold)  |  Mean reversion probability: High\n"
                    "RSI recovery score: 0.79  |  Momentum turn score: 0.66\n"
                    "Trend score: 0.36  |  Macro score: 0.63\n"
                    "Healthcare sector: Defensive support active\n"
                    "Insiders: Net buyers last 2 quarters"
                ),
                "signals": {
                    "rsi_recovery": 0.79, "momentum_turn": 0.66,
                    "trend": 0.36, "macro": 0.63, "regime": "recovery",
                    "ideal_action": "buy",
                },
            },
        ],
    },
    "sector_rotation": {
        "description": "Identify sector rotation opportunities where institutional capital is moving in",
        "ideal_action": "buy",
        "steps": [
            {
                "observation": (
                    "Market Analysis Report — NTPC (NSE) — Power Sector:\n"
                    "Sector vs Nifty RS: +5.2% (28-day)  |  Trend: Improving\n"
                    "Relative strength score: 0.75  |  Institutional flow: 0.72\n"
                    "Momentum score: 0.64  |  Macro score: 0.72\n"
                    "Budget allocation: ₹3.8L Cr to energy infrastructure\n"
                    "FII: Net buyers in power sector for 4 weeks"
                ),
                "signals": {
                    "relative_strength": 0.75, "institutional_flow": 0.72,
                    "momentum": 0.64, "macro": 0.72, "regime": "rotation",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — BHEL (NSE) — Capital Goods:\n"
                    "Sector vs Nifty RS: +3.9% (28-day)  |  Outperformance: Building\n"
                    "Relative strength score: 0.68  |  Institutional flow: 0.70\n"
                    "Momentum score: 0.62  |  Macro score: 0.70\n"
                    "Order book: Record high  |  Capex cycle: Early bull phase\n"
                    "DII basket: Adding capital goods exposure"
                ),
                "signals": {
                    "relative_strength": 0.68, "institutional_flow": 0.70,
                    "momentum": 0.62, "macro": 0.70, "regime": "rotation",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — COLPAL (NSE) — FMCG:\n"
                    "Sector vs Nifty RS: +2.8% (28-day)  |  Defensive rotation in play\n"
                    "Relative strength score: 0.65  |  Institutional flow: 0.68\n"
                    "Momentum score: 0.60  |  Macro score: 0.68\n"
                    "Rural demand recovery underway  |  Margin tailwind: Commodity softening\n"
                    "FPI hedging: FMCG overweight vs Nifty"
                ),
                "signals": {
                    "relative_strength": 0.65, "institutional_flow": 0.68,
                    "momentum": 0.60, "macro": 0.68, "regime": "rotation",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — HAL (NSE) — Defence:\n"
                    "Sector vs Nifty RS: +7.1% (28-day)  |  Multi-year outperformance\n"
                    "Relative strength score: 0.82  |  Institutional flow: 0.78\n"
                    "Momentum score: 0.70  |  Macro score: 0.74\n"
                    "Defence modernisation budget: Increased 15%\n"
                    "Export orders: New MoUs signed with 3 countries"
                ),
                "signals": {
                    "relative_strength": 0.82, "institutional_flow": 0.78,
                    "momentum": 0.70, "macro": 0.74, "regime": "rotation",
                    "ideal_action": "buy",
                },
            },
            {
                "observation": (
                    "Market Analysis Report — ULTRACEMCO (NSE) — Cement:\n"
                    "Sector vs Nifty RS: +4.5% (28-day)  |  Infrastructure play\n"
                    "Relative strength score: 0.70  |  Institutional flow: 0.71\n"
                    "Momentum score: 0.65  |  Macro score: 0.71\n"
                    "National highway allocation: Highest in 5 years\n"
                    "Realisations: Improving QoQ  |  Volume: Rising"
                ),
                "signals": {
                    "relative_strength": 0.70, "institutional_flow": 0.71,
                    "momentum": 0.65, "macro": 0.71, "regime": "rotation",
                    "ideal_action": "buy",
                },
            },
        ],
    },
}

TASK_NAMES = list(TASKS.keys())
