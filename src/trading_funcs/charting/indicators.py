from lightweight_charts import Chart
from src.trading_funcs.indicators import SMA
from src.trading_funcs.indicators import StochasticOscillator
from src.trading_funcs.indicators import RSI
from src.trading_funcs.indicators import DonchianChannels
from src.trading_funcs.indicators import BollingerBands


class StockIndicators:
    def __init__(self, chart: Chart):
        self.sma = SMA(chart=chart)
        self.stochastic_oscillator = StochasticOscillator(chart=chart)
        self.rsi = RSI(chart=chart)
        self.donchian_channels = DonchianChannels(chart=chart)
        self.bollinger_bands = BollingerBands(chart=chart)