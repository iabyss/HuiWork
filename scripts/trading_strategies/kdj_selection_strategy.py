import pandas as pd

class KDJSelectionStrategy:
    def __init__(self, p1=9, p2=3, p3=3, isShowLog=False):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.isShowLog = isShowLog

    def calculate_kdj(self, df, target_date):
        df = df.copy()  # 防止修改原始数据
        df = df.sort_index()  # 确保按日期排序
        
        # 检查数据量是否足够
        if len(df) < self.p1:
            raise ValueError(f"数据不足，计算KDJ需要至少 {self.p1} 天的历史数据。")

        # 计算最低价和最高价的滚动窗口
        low_min = df['low'].rolling(window=self.p1, min_periods=1).min()
        high_max = df['high'].rolling(window=self.p1, min_periods=1).max()
        
        

        # 计算 RSV
        df['rsv'] = (df['close'] - low_min) / (high_max - low_min) * 100
        
        print(low_min,high_max,df['rsv'])

        # 初始化K和D
        df['k'] = 50.0
        df['d'] = 50.0

        # 使用平滑公式计算 K 和 D
        for i in range(self.p2 - 1, len(df)):  # 从self.p2-1开始，以保证前面有足够的数值进行SMA计算
            # 计算新的K值，使用P2日SMA
            df.loc[df.index[i], 'k'] = df.loc[df.index[i], 'rsv'].mean()
        
            # 计算新的D值，使用P3日SMA
            df.loc[df.index[i], 'd'] = df.loc[df.index[i - self.p3 + 1:i + 1], 'k'].mean()
        
            # 计算新的J值
            df.loc[df.index[i], 'j'] = 3 * df.loc[df.index[i], 'k'] - 2 * df.loc[df.index[i], 'd']
            if self.isShowLog:
            # 打印对应日期的RSV, K, D, J值
                print(f"日期: {df.index[i]},LL: {df.loc[df.index[i], 'low']:.2f},HH: {df.loc[df.index[i], 'high']:.2f}, RSV: {df.loc[df.index[i], 'rsv']:.2f}, K: {df.loc[df.index[i], 'k']:.2f}, D: {df.loc[df.index[i], 'd']:.2f}, J: {df.loc[df.index[i], 'j']:.2f}")
               

        # 提取目标日期的KDJ值
        k_value = df.loc[target_date, 'k']
        d_value = df.loc[target_date, 'd']
        j_value = df.loc[target_date, 'j']
        close = df.loc[target_date, 'close']
        high = df.loc[target_date, 'high']
        low = df.loc[target_date, 'low']

        # 确保输出格式正确
        if isinstance(k_value, pd.Series):
            k_value = k_value.item()
        if isinstance(d_value, pd.Series):
            d_value = d_value.item()
        if isinstance(j_value, pd.Series):
            j_value = j_value.item()

        if self.isShowLog:
            print(f"目标日期 {target_date} 的数据 - Close: {close:.2f}, High: {high:.2f}, Low: {low:.2f}, K值: {k_value:.2f}, D值: {d_value:.2f}, J值: {j_value:.2f}")

        return k_value, d_value, j_value

# 创建包含日期、高、低、收盘价格的数据
data = {
    'date': [
        '2024-11-06', '2024-11-05', '2024-11-04', '2024-11-01', '2024-10-31',
        '2024-10-30', '2024-10-29', '2024-10-28', '2024-10-25', '2024-10-24',
        '2024-10-23', '2024-10-22', '2024-10-21', '2024-10-18', '2024-10-17',
        '2024-10-16', '2024-10-15', '2024-10-14', '2024-10-11', '2024-10-10',
        '2024-10-09', '2024-10-08', '2024-09-30', '2024-09-27', '2024-09-26',
        '2024-09-25', '2024-09-24', '2024-09-23'
    ],
    'high': [
        11.64, 11.66, 11.46, 11.55, 11.44, 11.58, 11.74, 11.68, 11.78, 11.86,
        11.89, 11.93, 11.94, 12.18, 12.23, 12.18, 12.23, 12.18, 12.17, 12.26,
        12.63, 13.43, 12.3, 11.56, 11.15, 10.7, 10.37, 10.09
    ],
    'low': [
        11.47, 11.39, 11.26, 11.34, 11.24, 11.27, 11.53, 11.53, 11.69, 11.72,
        11.75, 11.72, 11.63, 11.68, 11.93, 11.77, 11.88, 11.79, 11.58, 11.6,
        11.66, 12.34, 11.56, 11.03, 10.5, 10.45, 10.08, 9.87
    ],
    'close': [
        11.55, 11.65, 11.46, 11.43, 11.38, 11.32, 11.54, 11.64, 11.71, 11.75,
        11.86, 11.79, 11.81, 12.04, 11.95, 12.06, 11.9, 12.02, 11.72, 11.98,
        11.68, 12.88, 12.21, 11.42, 11.15, 10.5, 10.37, 10.04
    ]
}

# 创建 DataFrame 并设置日期为索引
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

strategy = KDJSelectionStrategy(isShowLog=True)
target_date = '2024-11-01'
k, d, j = strategy.calculate_kdj(df, target_date)
print(f"{target_date} 的 KDJ 值为: K={k:.2f}, D={d:.2f}, J={j:.2f}")
