import os
from datetime import datetime
from futu import *

# 设置 Futu API 连接信息
host = '127.0.0.1'  # 修改为你的 Futu OpenD 的 IP 地址
port = 11111  # 修改为你的 Futu OpenD 的端口

# 定义数据存储目录
data_dir = "../../data/stock/futu/stock/"
os.makedirs(data_dir, exist_ok=True)

def download_futu_stock_data(stock_code, start_date, end_date):
    """使用 Futu API 下载股票数据"""
    # 初始化 Futu API 的行情上下文
    quote_ctx = OpenQuoteContext(host=host, port=port)
    
    # 请求历史 K 线数据
    ret, data, page_req_key = quote_ctx.request_history_kline(
        stock_code, start=start_date, end=end_date, 
        ktype=KLType.K_DAY, autype=AuType.QFQ
    )
    
    if ret == RET_OK:
        # 循环获取完整数据（如果需要翻页）
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
                print(f"Error downloading additional data for {stock_code}: {data}")
                break
        
        # 定义文件路径，文件名包含日期、股票代码及数据来源
        file_path = os.path.join(data_dir, f"{stock_code}_futu_stock.csv")
        all_data.to_csv(file_path, index=False)
        print(f"Downloaded Futu stock data for {stock_code} and saved to {file_path}.")
    else:
        print(f"Error downloading Futu stock data for {stock_code}: {data}")
    
    # 关闭行情上下文
    quote_ctx.close()

# 示例调用
if __name__ == "__main__":
    # 你可以在这里指定股票代码、开始日期和结束日期
    stock_code = "HK.00700"  # 腾讯控股的代码
    start_date = "2023-01-01"
    end_date = datetime.today().strftime("%Y-%m-%d")
    
    download_futu_stock_data(stock_code, start_date, end_date)
