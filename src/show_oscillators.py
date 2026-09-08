import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
from src.trading_funcs.charting.plotting import StockChart
from src.utils.logs import set_up_log

logger = set_up_log(__name__)

def main():
    # 1. Input Stock Code
    stock_code = input("Enter stock code for Oscillators (e.g., AAPL): ").strip().upper()
    if not stock_code:
        logger.info("No stock code provided. Exiting.")
        return

    # 2. Initialization
    stock_data_path = "./src/tests/data"
    start_date = (datetime.datetime.now() - relativedelta(years=3)).strftime('%Y-%m-%d')
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    interval = '1d'
    
    # 3. Setup Stock Chart Manager
    # We use the existing StockChart logic but we will only plot the oscillators
    stock_chart_manager = StockChart(
        stock_code=stock_code, 
        stock_data_path=stock_data_path, 
        start_date=start_date, 
        end_date=end_date,
        interval=interval
    )
    
    # 4. Get data
    data = stock_chart_manager.get_bar_data(stock_code=stock_code)
    
    # 5. Plotting
    # Based on the recent changes to plotting.py, .plot() returns (main_chart, osc_chart)
    main_chart, osc_chart = stock_chart_manager.plot(data=data)
    
    # We only want to show the Oscillator chart
    logger.info(f"Opening Oscillator Chart for {stock_code}...")
    # Ensure we only show the chart containing RSI and Stochastic
    osc_chart.show(block=True)

if __name__ == "__main__":
    main()
