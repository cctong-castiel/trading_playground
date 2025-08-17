from typing import Any
import pandas as pd
from src.settings.consts import SHIFT_RSI_VAL
from src.trading_funcs.indicators.base import IndicatorBase


class RSI(IndicatorBase):
    """
    Relative Strength Index (RSI) indicator class.
    This class calculates the RSI based on the provided DataFrame.
    """

    def __init__(self, name: str = "RSI"):
        super().__init__(name)

    def calculate_indicator_df(self, df: pd.DataFrame, period=14, close_col='close') -> pd.DataFrame:
        """
        Calculate the RSI DataFrame based on the provided DataFrame.
        """
        
        df['close_new'] = df[close_col]  # Adjust close prices
        delta = df[close_col].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        # shift RSI down by 100 units
        rsi = rsi - SHIFT_RSI_VAL

        # plot 30% and 70% lines
        return pd.DataFrame({
            'time': df['time'],
            'RSI': rsi.fillna(0),
            'RSI 30%': [70 - SHIFT_RSI_VAL] * len(df),
            'RSI 70%': [30 - SHIFT_RSI_VAL] * len(df)
        })

    def create(self, chart: Any, data: pd.DataFrame) -> None:
        """
        Create the RSI indicator on the provided chart.
        """
        
        rsi_data = self.calculate_indicator_df(data)
        rsi_line = chart.create_line(name=self.name, color=self.color.get('rsi_line'), width=1, price_line=False, price_label=False)
        rsi_30_line = chart.create_line(name='RSI 30%', color=self.color.get('rsi_30'), width=1, price_line=False, price_label=False)
        rsi_70_line = chart.create_line(name='RSI 70%', color=self.color.get('rsi_70'), width=1, price_line=False, price_label=False)
        rsi_30_line.set(rsi_data)
        rsi_70_line.set(rsi_data)
        rsi_line.set(rsi_data)

        return chart