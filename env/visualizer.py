import matplotlib.pyplot as plt
import numpy as np
import os
from typing import List

def plot_benchmark_results(
    task_id: str,
    prices: List[float],
    actions: List[float],
    portfolio: List[float],
    rewards: List[float],
    output_dir: str = "outputs/plots"
):
    """Generates a research-grade 4-panel dashboard of the trading episode."""
    os.makedirs(output_dir, exist_ok=True)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12), facecolor='#f8f9fa')
    plt.subplots_adjust(hspace=0.3, wspace=0.25)
    
    steps = np.arange(len(prices))
    
    if len(portfolio) > len(prices):
        portfolio = portfolio[1:]
    
    ax1 = axes[0, 0]
    ax1.plot(steps, prices, color='#2c3e50', alpha=0.8, label="Asset Price")
    ax1_twin = ax1.twinx()
    ax1_twin.fill_between(steps, 0, actions, color='#2ecc71', alpha=0.3, label="Long Exposure")
    ax1_twin.fill_between(steps, actions, 0, where=(np.array(actions) < 0), color='#e74c3c', alpha=0.3, label="Short Exposure")
    ax1.set_title(f"Price Dynamics & Agent Positioning ({task_id})", fontweight='bold')
    ax1.set_ylabel("Price ($)")
    ax1_twin.set_ylabel("Position Size (-1 to 1)")
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    ax2 = axes[0, 1]
    ax2.plot(steps, portfolio, color='#3498db', linewidth=2.5, label="Portfolio NAV")
    ax2.axhline(y=portfolio[0], color='#95a5a6', linestyle='--', alpha=0.8, label="Initial Capital")
    ax2.set_title("Portfolio Growth (Cumulative NAV)", fontweight='bold')
    ax2.set_ylabel("Value ($)")
    ax2.fill_between(steps, portfolio[0], portfolio, where=(np.array(portfolio) > portfolio[0]), color='#2ecc71', alpha=0.1)
    ax2.fill_between(steps, portfolio[0], portfolio, where=(np.array(portfolio) < portfolio[0]), color='#e74c3c', alpha=0.1)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    ax3 = axes[1, 0]
    ax3.bar(steps, rewards, color='#9b59b6', alpha=0.6, label="Step Log-Return")
    ax3.set_title("Reward Signal Distribution", fontweight='bold')
    ax3.set_ylabel("Reward Value")
    ax3.grid(True, alpha=0.2)
    
    ax4 = axes[1, 1]
    ph = np.array(portfolio)
    drawdown = (np.maximum.accumulate(ph) - ph) / np.maximum.accumulate(ph)
    ax4.fill_between(steps, 0, drawdown * 100, color='#e74c3c', alpha=0.4, label="Drawdown %")
    ax4.set_title("Risk Exposure (Drawdown)", fontweight='bold')
    ax4.set_ylabel("Drop from Peak (%)")
    ax4.invert_yaxis()
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle(f"AiTrade Selection-Grade Benchmark — Task: {task_id.upper()}", fontsize=16, fontweight='bold', y=0.95)
    
    filename = os.path.join(output_dir, f"{task_id}_performance.png")
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return filename
