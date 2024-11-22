import numpy as np
import pandas as pd

class Main:
    @staticmethod
    def sma(values, period):
        """
        计算简单移动平均 (Simple Moving Average).
        :param values: 数据序列 (list or numpy array)
        :param period: 时间窗口 (int)
        :return: SMA 数组 (numpy array)
        """
        return np.convolve(values, np.ones(period) / period, mode='valid')
    
    @staticmethod
    def custom_sma(values, period, smooth_factor=1):
        """
        自定义 SMA (平滑参数公式版)
        :param values: 数据序列 (list or numpy array)
        :param period: 时间窗口 (int)
        :param smooth_factor: 平滑系数
        :return: 自定义 SMA 数组
        """
        sma = []
        for i in range(len(values)):
            if i == 0:
                sma.append(values.iloc[i] if isinstance(values, pd.Series) else values[i])  # 初始值
            else:
                sma.append((smooth_factor * (values.iloc[i] if isinstance(values, pd.Series) else values[i]) +
                            (period - smooth_factor) * sma[i - 1]) / period)
        return np.array(sma)
