from typing import Any
import pandas as pd
from src.trading_funcs.indicators.base import IndicatorBase


class DonchianChannelsOscillator(IndicatorBase):
    """
    Donchian channels Oscillator indicator class.
    This class calculates the Donchian channels Oscillator based on the provided DataFrame.
    """

    def __init__(self, name: str = "Donchian channels Oscillator"):
        super().__init__(name)

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
    
    def create(self, chart: Any, data: pd.DataFrame) -> None:
        """
        Create the Donchian channels indicator on the provided chart.
        This method should be implemented by subclasses.
        """
        
        donchian20_data = self.calculate_indicator_df(data, period=20)
        donchian20_upper_line = chart.create_line(name='Upper Donchian 20', color="#00ff11", width=1, price_line=False, price_label=False)
        donchian20_lower_line = chart.create_line(name='Lower Donchian 20', color="#ff4800", width=1, price_line=False, price_label=False)
        donchian20_mean_line = chart.create_line(name='Mean Donchian 20', color="#ffffff", width=1, price_line=False, price_label=False)
        donchian20_upper_line.set(donchian20_data)
        donchian20_lower_line.set(donchian20_data)
        donchian20_mean_line.set(donchian20_data)

        return chart