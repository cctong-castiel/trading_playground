import pandas as pd


class IndicatorBase:
    """
    Base class for all indicators.
    This class should be inherited by all indicator classes.
    """

    def __init__(self, name: str):
        self.name = name

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