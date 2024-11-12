import os
import time
from futu import OpenQuoteContext, RET_OK, KLType, AuType
import pandas as pd
from datetime import datetime

# 设置 Futu API 连接信息
host = '127.0.0.1'  # 修改为你的 Futu OpenD 的 IP 地址
port = 11111  # 修改为你的 Futu OpenD 的端口

# 定义数据存储目录
data_dir_futu = "../../data/stock/futu/"
os.makedirs(data_dir_futu, exist_ok=True)

def get_all_stock_codes(market='A股'):
    """获取指定市场的所有股票代码"""
    quote_ctx = OpenQuoteContext(host=host, port=port)
    if market == 'A股':
        ret, stocks = quote_ctx.get_stock_basicinfo(market='SH', stock_type='STOCK')
        if ret != RET_OK:
            print(f"获取 A股 股票信息失败: {stocks}")
            return None
    elif market == '港股':
        ret, stocks = quote_ctx.get_stock_basicinfo(market='HK', stock_type='STOCK')
        if ret != RET_OK:
            print(f"获取 港股 股票信息失败: {stocks}")
            return None
    else:
        print("无效的市场类型，请选择 'A股' 或 '港股'")
        return None
    
    return stocks[['code', 'name']]

def download_futu_stock_data(stock_code, start_date, end_date):
    """使用 Futu API 下载单个股票的数据"""
    quote_ctx = OpenQuoteContext(host=host, port=port)
    
    ret, data, page_req_key = quote_ctx.request_history_kline(
        stock_code, start=start_date, end=end_date, 
        ktype=KLType.K_DAY, autype=AuType.QFQ
    )
    
    if ret == RET_OK:
        all_data = data
        while page_req_key:
            ret, data, page_req_key = quote_ctx.request_history_kline(
                stock_code, start=start_date, end=end_date, 
                ktype=KLType.K_DAY, autype=AuType.QFQ,
                page_req_key=page_req_key
            )
            if ret == RET_OK:
                all_data = all_data.append(data)
            else:
                print(f"Futu: 下载额外数据失败 {stock_code}: {data}")
                break
        
        file_path = os.path.join(data_dir_futu, f"{stock_code}_futu_stock.csv")
        all_data.to_csv(file_path, index=False)
        print(f"Futu: 下载 {stock_code} 数据并保存到 {file_path}.")
    else:
        print(f"Futu: 下载 {stock_code} 数据失败: {data}")
    
    quote_ctx.close()

def download_all_stocks_data(market, start_date, end_date):
    """下载指定市场的所有股票数据"""
    stocks = get_all_stock_codes(market)
    if stocks is not None:
        for i, row in stocks.iterrows():
            stock_code = row['code']
            print(f"正在下载 {stock_code} 的数据...")
            download_futu_stock_data(stock_code, start_date, end_date)
            # 添加延迟以避免频率限制
            if (i + 1) % 60 == 0:  # 每下载60个请求，等待30秒
                print("达到请求限制，等待30秒...")
                time.sleep(30)  # 等待30秒
            else:
                time.sleep(0.5)  # 其他请求之间稍微等待一下，防止过于密集

def main():
    market = input("请输入市场类型 (A股 或 港股): ")
    choice = input("输入 'all' 下载所有股票数据，输入 'single' 下载单个股票数据: ").strip().lower()
    
    start_date = input("请输入开始日期 (格式: YYYY-MM-DD): ")
    end_date = datetime.today().strftime("%Y-%m-%d")

    if choice == 'all':
        download_all_stocks_data(market, start_date, end_date)
    elif choice == 'single':
        stock_code = input("请输入要下载的股票代码: ")
        download_futu_stock_data(stock_code, start_date, end_date)
    else:
        print("无效的选择，请输入 'all' 或 'single'.")

if __name__ == "__main__":
    main()
