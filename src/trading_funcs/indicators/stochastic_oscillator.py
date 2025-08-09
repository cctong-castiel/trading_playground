from typing import Any
import pandas as pd
from src.trading_funcs.indicators.base import IndicatorBase


class StochasticOscillator(IndicatorBase):
    """
    Stochastic Oscillator indicator class.
    This class calculates the Stochastic Oscillator based on the provided DataFrame.
    """

    def __init__(self, name: str = "Stochastic Oscillator"):
        super().__init__(name)

    def calculate_indicator_df(self, df: pd.DataFrame, period=14) -> pd.DataFrame:
        """
        Calculate the Stochastic Oscillator DataFrame based on the provided DataFrame.
        """
        
        df['low_new'] = df['low']
        df['high_new'] = df['high']
        df['close_new'] = df['close']
        low_min = df['low_new'].rolling(window=period).min()
        high_max = df['high_new'].rolling(window=period).max()
        k_percent = 100 * ((df['close_new'] - low_min) / (high_max - low_min))
        d_percent = k_percent.rolling(window=3).mean()

        return pd.DataFrame({
            'time': df['time'],
            '%K': k_percent.fillna(0),
            '%D': d_percent.fillna(0),
            'Stochastic 20%': [20] * len(df),
            'Stochastic 80%': [80] * len(df)
        })
    
    def create(self, chart: Any, data: pd.DataFrame) -> None:
        """
        Create the Stochastic Oscillator indicator on the provided chart.
        This method should be implemented by subclasses.
        """
        
        stochastic_data = self.calculate_indicator_df(data)
        stochastic_k_line = chart.create_line(name='%K', color="#ff00ff", width=1, price_line=False, price_label=False)
        stochastic_d_line = chart.create_line(name='%D', color="#00ffff", width=1, price_line=False, price_label=False)
        stochastic_20_line = chart.create_line(name='Stochastic 20%', color="#ff0000", width=1, price_line=False, price_label=False)
        stochastic_80_line = chart.create_line(name='Stochastic 80%', color="#00ff00", width=1, price_line=False, price_label=False)
        stochastic_k_line.set(stochastic_data)
        stochastic_d_line.set(stochastic_data)
        stochastic_20_line.set(stochastic_data)
        stochastic_80_line.set(stochastic_data)

        return chart