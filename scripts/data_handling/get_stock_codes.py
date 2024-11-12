import tushare as ts
import os
from datetime import datetime, timedelta

# 设置Tushare的API密钥
ts.set_token("4b35a2f33e123904201a3635e0e3a160c2b7d8db8e861be875d34887")
pro = ts.pro_api()

# 定义存储股票代码的文件路径
code_file_path = "../data/stock/raw/stock_codes.txt"
last_update_file = "last_update.txt"

def get_all_stock_codes(market='主板'):
    """
    获取指定市场中所有股票的代码列表，并保存到文件。
    
    参数:
        market (str): 市场类别，例如 '主板', '创业板', '科创板'。
    
    返回:
        list: 股票代码列表
    """
    try:
        stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code, market')
        market_stocks = stocks[stocks['market'] == market]['ts_code'].tolist()

        # 将股票代码写入文件
        with open(code_file_path, 'w') as f:
            for code in market_stocks:
                f.write(f"{code}\n")
        print(f"Updated stock codes for {market} market.")
        return market_stocks

    except Exception as e:
        print(f"Error getting stock codes: {e}")
        return []

def should_update_codes():
    """
    检查是否需要更新股票代码（每天一次）。
    
    返回:
        bool: 如果需要更新返回 True，否则返回 False。
    """
    if not os.path.exists(last_update_file):
        return True  # 如果文件不存在，返回需要更新

    with open(last_update_file, 'r') as f:
        last_update = f.read().strip()
        
        # 检查文件是否为空
        if not last_update:
            return True  # 文件为空，返回需要更新

        last_update_date = datetime.strptime(last_update, "%Y-%m-%d")
        return datetime.now() >= last_update_date + timedelta(days=1)

def update_last_update_date():
    """更新最后更新时间文件。"""
    with open(last_update_file, 'w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d"))

if __name__ == "__main__":
    if should_update_codes():
        get_all_stock_codes()
        update_last_update_date()
    else:
        print("Stock codes are up to date.")
