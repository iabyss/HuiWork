import os
import tushare as ts
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "stock", "tushare", "raw")
STOCK_CODES_FILE = os.path.join(DATA_DIR, "stock_codes.txt")
OUTPUT_DIR = os.path.join(DATA_DIR, "historical_data")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def read_stock_codes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            stock_codes = [line.strip() for line in f if line.strip()]
            return stock_codes
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def download_stock_data(stock_code, start_date, end_date):
    pro = ts.pro_api("4b35a2f33e123904201a3635e0e3a160c2b7d8db8e861be875d34887")  # Replace with your Tushare API token
    data = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    
    # Save to CSV
    output_file = os.path.join(OUTPUT_DIR, f"{stock_code}.csv")
    data.to_csv(output_file, index=False)
    print(f"Saved data for {stock_code} to {output_file}")

def main():
    print(f"Attempting to read stock codes from: {STOCK_CODES_FILE}")
    stock_codes = read_stock_codes(STOCK_CODES_FILE)

    if not stock_codes:
        print("No stock codes found.")
        return

    start_date = "20200101"
    end_date = datetime.today().strftime('%Y%m%d')
    
    for stock_code in stock_codes:
        print(f"Downloading data for {stock_code} from {start_date} to {end_date}...")
        download_stock_data(stock_code, start_date, end_date)

if __name__ == "__main__":
    main()
