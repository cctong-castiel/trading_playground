from typing import Any
import pandas as pd
from src.trading_funcs.indicators.base import IndicatorBase


class SMA(IndicatorBase):
    """
    SMA indicator class.
    This class calculates the SMA based on the provided DataFrame.
    """

    def __init__(self, name: str = "SMA"):
        super().__init__(name)

    def calculate_indicator_df(self, df: pd.DataFrame, period: int = 20, num_std_dev: int = 2) -> pd.DataFrame:
        """
        Calculate the SMA DataFrame based on the provided DataFrame.
        """
        
        return pd.DataFrame({
            'time': df['time'],
            f'SMA {period}': df['close'].rolling(window=period).mean()
        }).fillna(0)
        
    def create(self, chart: Any, data: pd.DataFrame) -> None:
        """
        Create the SMA indicator on the provided chart.
        This method should be implemented by subclasses.
        """
        
        sma9_line = chart.create_line(name='SMA 9', color='#ffeb3b', width=1, price_label=False)
        sma9_data = self.calculate_indicator_df(data, period=9)
        sma9_line.set(sma9_data)

        sma4_line = chart.create_line(name='SMA 4', color ="#5f3bff", width=1, price_label=False)
        sma4_data = self.calculate_indicator_df(data, period=4)
        sma4_line.set(sma4_data)

        return chart