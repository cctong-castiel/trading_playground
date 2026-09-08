import pandas as pd
from tradingview_scraper.symbols import technicals, news
from src.utils.logs import set_up_log

logger = set_up_log(__name__)

class TradingViewService:
    """
    Service to scrape Technicals and News from TradingView.
    """
    def __init__(self):
        pass

    def get_technical_summary(self, symbol: str, interval: str = '1d'):
        """
        Get a summary of technical indicators for a symbol.
        """
        try:
            logger.info(f"Fetching technical summary for {symbol} at {interval} interval")
            # This assumes the tradingview_scraper package is installed
            # Using a simplified version based on the identified notebook logic
            tech = technicals.Indicators(symbol=symbol, interval=interval)
            return tech.get_summary()
        except Exception as e:
            logger.error(f"Error fetching technical summary for {symbol}: {e}")
            return None

    def get_latest_news(self, symbol: str):
        """
        Get the latest news for a symbol.
        """
        try:
            logger.info(f"Fetching latest news for {symbol}")
            news_scraper = news.NewsScraper(symbol=symbol)
            return news_scraper.get_news()
        except Exception as e:
            logger.error(f"Error fetching news for {symbol}: {e}")
            return None
