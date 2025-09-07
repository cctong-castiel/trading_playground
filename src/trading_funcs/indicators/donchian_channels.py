from typing import Any
import pandas as pd
from lightweight_charts import Chart
from src.trading_funcs.indicators.base import IndicatorBase


class DonchianChannels(IndicatorBase):
    """
    Donchian channels  indicator class.
    This class calculates the Donchian channels based on the provided DataFrame.
    """

    def __init__(self, chart: Chart, name: str = "Donchian channels"):
        super().__init__(name)
        self.chart = chart
        self.donchian20_upper_line = chart.create_line(name='Upper Donchian 20', color=self.color.get('donchian_upper'), width=1, price_line=False, price_label=False)
        self.donchian20_lower_line = chart.create_line(name='Lower Donchian 20', color=self.color.get('donchian_lower'), width=1, price_line=False, price_label=False)
        self.donchian20_mean_line = chart.create_line(name='Mean Donchian 20', color=self.color.get('donchian_mean'), width=1, price_line=False, price_label=False)

    def calculate_indicator_df(self, df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
        """
        Calculate the Donchian channels DataFrame based on the provided DataFrame.
        """
        
        high = df['high'].rolling(window=period).max()
        low = df['low'].rolling(window=period).min()
        mean = (high + low) / 2

        return pd.DataFrame({
            'time': df['time'],
            f'Upper Donchian {period}': high.fillna(0),
            f'Mean Donchian {period}': mean.fillna(0),
            f'Lower Donchian {period}': low.fillna(0)
        })
    
    def create(self, data: pd.DataFrame) -> None:
        """
        Create the Donchian channels indicator on the provided chart.
        This method should be implemented by subclasses.
        """
        
        donchian20_data = self.calculate_indicator_df(data, period=20)
        self.donchian20_upper_line.set(donchian20_data)
        self.donchian20_lower_line.set(donchian20_data)
        self.donchian20_mean_line.set(donchian20_data)