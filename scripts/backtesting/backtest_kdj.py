import sys
import os
import pandas as pd  # 添加 pandas 导入
from trading_strategies.kdj_factor import KDJFactor

# 设置路径，确保可以导入 trading_strategies 目录中的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# 加载数据
data = pd.read_csv('../../data/stock/processed/sample_stock_data.csv')

def backtest_kdj(data, kdj_params={'period': 9}, buy_threshold=0, sell_threshold=100):
    kdj = KDJFactor(**kdj_params)
    data = kdj.calculate_kdj(data)
    
    data['Signal'] = 0  # 0表示无操作，1表示买入，-1表示卖出
    data.loc[data['J'] < buy_threshold, 'Signal'] = 1
    data.loc[data['J'] > sell_threshold, 'Signal'] = -1
    return data[['close', 'K', 'D', 'J', 'Signal']]

# 假设已经读取了数据
if __name__ == "__main__":
    # 载入股票数据示例
    data = pd.read_csv('../../data/stock/processed/sample_stock_data.csv')
    results = backtest_kdj(data)
    results.to_csv('../../results/backtesting/kdj_backtest_results.csv')
