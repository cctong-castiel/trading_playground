import pandas as pd
from src.settings.consts import indicator_config


class IndicatorBase:
    """
    Base class for all indicators.
    This class should be inherited by all indicator classes.
    """

    def __init__(self, name: str):
        self.name = name
        self.color = indicator_config.get('colour')

    def calculate_indicator_df(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate the indicator DataFrame based on the provided DataFrame.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def create(self, data):
        """
        Calculate the indicator value based on the provided data.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")