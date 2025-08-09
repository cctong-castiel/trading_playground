import os
import pandas as pd
import numpy as np
from lightweight_charts import Chart
import yfinance as yf
# create a class to wrap the above script and plot the chart. Also use stochastic_oscillator.py and rsi.py to add these 2 indicators
from src.trading_funcs.indicators.rsi import RSI
from src.trading_funcs.indicators.stochastic_oscillator import StochasticOscillator


class StockChart:
    def __init__(self, stock_code: str, stock_data_path: str, start_date: str, end_date: str, interval: str = '1d', save_flag: bool = True):
        self.stock_code = stock_code
        self.stock_data_path = stock_data_path
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.save_flag = save_flag
        self.chart = Chart(toolbox=True)
        self._set_chart_styles()
        
    def _set_chart_styles(self):
        self.chart.layout(background_color='#131722', font_family='Trebuchet MS', font_size=16)
        self.chart.volume_config(up_color='#2962ffcb', down_color='#e91e63cb')
        self.chart.name = self.stock_code
        self.chart.legend(visible=True, font_family='Trebuchet MS', ohlc=True, percent=True)
        self.chart.events.search += self.on_search
        self.chart.topbar.textbox('symbol', self.stock_code)
        self.chart.horizontal_line(200, func=self.on_horizontal_line_move)
        
    def contains_excel_file(self, path: str, filename: str) -> bool:
        if not os.path.isdir(path):
            print("Invalid directory path.")
            return False

        for root, dirs, files in os.walk(path):
            for file in files:
                if filename.lower() == file.lower():
                    return True

        print("No Excel files found.")
        return False

    def download_yf_data(self, stock_code: str) -> pd.DataFrame:
        """
        Download stock data from Yahoo Finance.
        
        :param stock_code: Stock ticker symbol.
        :param start_date: Start date for the data in 'YYYY-MM-DD' format.
        :param end_date: End date for the data in 'YYYY-MM-DD' format.
        :param interval: Data interval (default is '1d').
        :return: DataFrame with stock data.
        """

        data = yf.download([stock_code], start=self.start_date, end=self.end_date, interval=self.interval)
        data = self.preprocess_stock_data(data)
        if self.save_flag:
            print(f"saving path: {self.stock_data_path}/{stock_code}_{self.end_date}.csv")
            data.to_csv(f"{self.stock_data_path}/{stock_code}_{self.end_date}.csv")
        return data

    def get_bar_data(self, stock_code: str) -> pd.DataFrame:
        """    Get bar data for a given stock symbol.
        :param symbol: Stock ticker symbol.
        :return: DataFrame with stock data or an empty DataFrame if no data is found
        """

        if self.contains_excel_file(self.stock_data_path, f"{stock_code}_{self.end_date}.csv") is False:
            print(f'No data for "{stock_code}" download it from Yahoo Finance')
            return self.download_yf_data(stock_code=stock_code)
        print(f'Get data for "{stock_code}" from {self.stock_data_path}')
        return pd.read_csv(f'{self.stock_data_path}/{stock_code}_{self.end_date}.csv')

    # twist the stock data for downstream processing
    def preprocess_stock_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess stock data to have a consistent format.
        
        :param data: DataFrame with stock data.
        :return: Preprocessed DataFrame.
        """
        data = data.reset_index()
        data.columns = data.columns.droplevel(1)
        data.rename(columns={
            'Date': 'time',
            'Open': 'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume'
        }, inplace=True)
        return data

    def on_search(self, chart, searched_string):  # Called when the user searches.
        new_data = self.get_bar_data(searched_string)
        if new_data.empty:
            return
        chart.topbar['symbol'].set(searched_string)
        chart.set(new_data)

    def on_timeframe_selection(self, chart):  # Called when the user changes the timeframe.
        new_data = self.get_bar_data(stock_code)
        if new_data.empty:
            return
        chart.set(new_data, True)

    def on_timeframe_selection(self, chart):  # Called when the user changes the timeframe.
        new_data = self.get_bar_data(stock_code)
        if new_data.empty:
            return
        chart.set(new_data, True)

    def on_horizontal_line_move(self, line):
        print(f'Horizontal line moved to: {line.price}')


    def plot(self):
        data = self.get_bar_data(stock_code=self.stock_code)
        if data is None:
            print(f'No data available for {self.stock_code}')
            return
        
        self.chart.set(data)
        
        # Add RSI indicator
        rsi_indicator = RSI()
        self.chart = rsi_indicator.create(self.chart, data)
        
        # Add Stochastic Oscillator indicator
        # stochastic_indicator = StochasticOscillator()
        # self.chart = stochastic_indicator.create(self.chart, data)
        
        # Show the chart
        self.chart.show(block=True)

        return self.chart
    
# Example usage
if __name__ == "__main__":

    # input the stock code
    stock_code = input("Enter stock code (e.g., AAPL): ").strip().upper()
    if not stock_code:
        print("No stock code provided. Exiting.")
        exit()

    # initialization
    stock_data_path = "./src/tests/data"
    start_date = '2024-06-09'
    end_date = '2024-07-26'
    interval = '1d'
    save_flag = True
    excel_extensions = ['.xlsx', '.xls', '.xlsm', 'csv']

    stock_chart = StockChart(
        stock_code=stock_code, 
        stock_data_path=stock_data_path, 
        start_date=start_date, 
        end_date=end_date,
        interval=interval,
        save_flag=save_flag
    )
    stock_chart.plot()