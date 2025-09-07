from typing import Any
import pandas as pd
from lightweight_charts import Chart
from src.settings.consts import SHIFT_STOCHASTIC_VAL
from src.trading_funcs.indicators.base import IndicatorBase


class StochasticOscillator(IndicatorBase):
    """
    Stochastic Oscillator indicator class.
    This class calculates the Stochastic Oscillator based on the provided DataFrame.
    """

    def __init__(self, chart: Chart, name: str = "Stochastic Oscillator"):
        super().__init__(name)
        self.chart = chart
        self.stochastic_k_line = chart.create_line(name='%K', color=self.color.get('stochastic_k_line'), width=1, price_line=False, price_label=False)
        self.stochastic_d_line = chart.create_line(name='%D', color=self.color.get('stochastic_d_line'), width=1, price_line=False, price_label=False)
        self.stochastic_20_line = chart.create_line(name='Stochastic 20%', color=self.color.get('stochastic_20'), width=1, price_line=False, price_label=False)
        self.stochastic_80_line = chart.create_line(name='Stochastic 80%', color=self.color.get('stochastic_80'), width=1, price_line=False, price_label=False)

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

        # shift both k_percent and d_percent down by 100 units
        k_percent = k_percent - SHIFT_STOCHASTIC_VAL
        d_percent = d_percent - SHIFT_STOCHASTIC_VAL

        return pd.DataFrame({
            'time': df['time'],
            '%K': k_percent.fillna(0),
            '%D': d_percent.fillna(0),
            'Stochastic 20%': [80 - SHIFT_STOCHASTIC_VAL] * len(df),
            'Stochastic 80%': [20 - SHIFT_STOCHASTIC_VAL] * len(df)
        })
    
    def create(self, data: pd.DataFrame) -> None:
        """
        Create the Stochastic Oscillator indicator on the provided chart.
        This method should be implemented by subclasses.
        """
        
        stochastic_data = self.calculate_indicator_df(data)
        self.stochastic_k_line.set(stochastic_data)
        self.stochastic_d_line.set(stochastic_data)
        self.stochastic_20_line.set(stochastic_data)
        self.stochastic_80_line.set(stochastic_data)