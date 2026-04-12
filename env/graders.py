import numpy as np
from typing import List, Dict, Any

def calculate_drawdown(portfolio_history: List[float]) -> float:
    ph = np.array(portfolio_history)
    drawdowns = (np.maximum.accumulate(ph) - ph) / np.maximum.accumulate(ph)
    return float(np.max(drawdowns))

def profit_grader(portfolio_history: List[float]) -> float:
    """Grades based strictly on total return."""
    initial = portfolio_history[0]
    final = portfolio_history[-1]
    total_return = (final - initial) / initial
    
    score = 0.5 + (total_return * 2.5) 
    return float(np.clip(score, 0.01, 0.99))

def sharpe_grader(portfolio_history: List[float]) -> float:
    """Grades based on risk-adjusted returns (Sharpe Ratio)."""
    ph = np.array(portfolio_history)
    returns = np.diff(ph) / ph[:-1]
    
    if len(returns) < 2 or np.std(returns) == 0:
        return 0.5
        
    sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252)
    
    score = 0.5 + (sharpe / 6.0)
    return float(np.clip(score, 0.01, 0.99))

def risk_adjusted_grader(portfolio_history: List[float]) -> float:
    """Combines profit and drawdown penalty."""
    p_score = profit_grader(portfolio_history)
    max_dd = calculate_drawdown(portfolio_history)
    
    final_score = p_score - (max_dd * 5.0)
    return float(np.clip(final_score, 0.01, 0.99))
