from typing import Any
import pandas as pd
from src.trading_funcs.indicators.base import IndicatorBase


class BollingerBands(IndicatorBase):
    """
    Bollinger bands indicator class.
    This class calculates the Bollinger bands based on the provided DataFrame.
    """

    def __init__(self, name: str = "Bollinger bands"):
        super().__init__(name)

    def calculate_indicator_df(self, df: pd.DataFrame, period: int = 20, num_std_dev: int = 2) -> pd.DataFrame:
        """
        Calculate the Bollinger bands DataFrame based on the provided DataFrame.
        """
        
        sma = df['close'].rolling(window=period).mean()
        rolling_std = df['close'].rolling(window=period).std()
        upper_band = sma + (rolling_std * num_std_dev)
        lower_band = sma - (rolling_std * num_std_dev)     

        return pd.DataFrame({
            'time': df['time'],
            f'Upper Bollinger {period}': upper_band.fillna(0),
            f'Mean Bollinger {period}': sma.fillna(0),
            f'Lower Bollinger {period}': lower_band.fillna(0)
        })
    
    def create(self, chart: Any, data: pd.DataFrame) -> None:
        """
        Create the Bollinger bands indicator on the provided chart.
        This method should be implemented by subclasses.
        """
        
        bollinger20_data = self.calculate_indicator_df(data, period=20, num_std_dev=2)
        bollinger20_upper_line = chart.create_line(name='Upper Bollinger 20', color=self.color.get('bollinger_upper'), width=1, price_line=False, price_label=False)
        bollinger20_lower_line = chart.create_line(name='Lower Bollinger 20', color=self.color.get('bollinger_lower'), width=1, price_line=False, price_label=False)
        bollinger20_mean_line = chart.create_line(name='Mean Bollinger 20', color=self.color.get('bollinger_mean'), width=1, price_line=False, price_label=False)
        bollinger20_upper_line.set(bollinger20_data)
        bollinger20_lower_line.set(bollinger20_data)
        bollinger20_mean_line.set(bollinger20_data)

        return chart