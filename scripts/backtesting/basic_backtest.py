import os
import sys
import pandas as pd
from datetime import datetime
sys.path.append(os.path.abspath("F:/HuiWork/scripts"))

from trading_strategies.kdj_selection_strategy import KDJSelectionStrategy  # 导入KDJ选股策略

class BacktestEnvironment:
    def __init__(self, initial_cash, start_date, end_date, max_holdings, single_stock_limit, total_portfolio_limit, data_directory):
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.portfolio_value = initial_cash
        self.max_holdings = max_holdings
        self.single_stock_limit = single_stock_limit
        self.total_portfolio_limit = total_portfolio_limit
        self.start_date = start_date
        self.end_date = end_date

        # 加载目录下的所有股票数据文件
        self.data = {}
        for filename in os.listdir(data_directory):
            if filename.endswith(".csv"):
                stock_code = filename.split(".")[0]
                file_path = os.path.join(data_directory, filename)
                
                df = pd.read_csv(
                    file_path,
                    parse_dates=['date'],
                    date_parser=lambda x: pd.to_datetime(x, format='%Y%m%d', errors='coerce')
                )
                df.set_index('date', inplace=True)
                
                filtered_df = df[(df.index >= pd.to_datetime(start_date)) & (df.index <= pd.to_datetime(end_date))]
                if not filtered_df.empty:
                    self.data[stock_code] = filtered_df

        self.holdings = {}
        self.transaction_log = []

    def buy_stock(self, stock, price, amount):
        cost = price * amount
        if self.cash >= cost:
            self.cash -= cost
            self.holdings[stock] = self.holdings.get(stock, 0) + amount
            self.transaction_log.append((self.current_date, 'BUY', stock, price, amount))
        else:
            print(f"Insufficient cash to buy {stock}.")

    def sell_stock(self, stock, price, amount):
        if self.holdings.get(stock, 0) >= amount:
            self.cash += price * amount
            self.holdings[stock] -= amount
            self.transaction_log.append((self.current_date, 'SELL', stock, price, amount))
            if self.holdings[stock] == 0:
                del self.holdings[stock]
        else:
            print(f"Insufficient holdings to sell {stock}.")

    def sell_strategy(self, date):
        """ 返回需要卖出的持仓股票列表 """
        sell_list = []
        for stock in list(self.holdings.keys()):
            if stock in self.data and date in self.data[stock].index:
                current_j_value = self.data[stock].loc[date, 'j']
                if current_j_value > 10:  # 卖出条件：J值 > 10
                    sell_list.append(stock)
        return sell_list

    def buy_strategy(self, date, selected_stocks):
        """ 返回需要买入的股票列表 """
        buy_list = []
        for stock, j_value in selected_stocks:
            if len(self.holdings) < self.max_holdings:
                if stock in self.data and date in self.data[stock].index:
                    price = self.data[stock].loc[date, 'close']
                    position_ratio = min(self.single_stock_limit, (self.total_portfolio_limit - self.current_position_ratio))
                    amount_to_buy = (self.cash * position_ratio) // price
                    if amount_to_buy > 0:
                        buy_list.append((stock, price, int(amount_to_buy)))
        return buy_list

    def run_backtest(self, strategy):
        for date in pd.date_range(start=self.start_date, end=self.end_date, freq='B'):
            self.current_date = date

            # Step 1: 先获得待卖出股票列表并卖出
            stocks_to_sell = self.sell_strategy(date)
            for stock in stocks_to_sell:
                price = self.data[stock].loc[date, 'close']
                amount = self.holdings[stock]
                self.sell_stock(stock, price, amount)

            # Step 2: 获得待买入股票列表并买入
            selected_stocks = strategy.select_stocks(date, self.data, True, 0, 100)
            self.current_position_ratio = sum(self.data[stock].loc[date, 'close'] * amount for stock, amount in self.holdings.items() if date in self.data[stock].index) / self.portfolio_value
            stocks_to_buy = self.buy_strategy(date, selected_stocks)
            for stock, price, amount in stocks_to_buy:
                self.buy_stock(stock, price, amount)

            # 更新投资组合价值
            self.portfolio_value = self.cash + sum(self.data[stock].loc[date, 'close'] * amount for stock, amount in self.holdings.items() if date in self.data[stock].index)

        self.finalize()

    def finalize(self):
        print("Final Portfolio Value:", self.portfolio_value)
        print("Transaction Log:", self.transaction_log)

# 执行回测
if __name__ == "__main__":
    data_directory = '../../data/stock/processed'
    initial_cash = 100000
    start_date = '2024-10-01'
    end_date = '2024-11-06'
    max_holdings = 5
    single_stock_limit = 0.2
    total_portfolio_limit = 0.8

    backtest = BacktestEnvironment(initial_cash, start_date, end_date, max_holdings, single_stock_limit, total_portfolio_limit, data_directory)
    strategy = KDJSelectionStrategy()
    backtest.run_backtest(strategy)
