import datetime
from dateutil.relativedelta import relativedelta
from src.trading_funcs.charting.plotting import StockChart
from src.trading_funcs.tradingview_service import TradingViewService
from src.utils.logs import set_up_log

logger = set_up_log(__name__)

def main():
    # 1. Input Stock Code
    stock_code = input("Enter stock code (e.g., AAPL): ").strip().upper()
    if not stock_code:
        logger.info("No stock code provided. Exiting.")
        return

    # 2. Initialization
    stock_data_path = "./src/tests/data"
    start_date = (datetime.datetime.now() - relativedelta(years=3)).strftime('%Y-%m-%d')
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    interval = '1d'
    
    # 3. Setup Stock Charts (Main + Oscillator)
    stock_chart_manager = StockChart(
        stock_code=stock_code, 
        stock_data_path=stock_data_path, 
        start_date=start_date, 
        end_date=end_date,
        interval=interval
    )
    data = stock_chart_manager.get_bar_data(stock_code=stock_code)
    main_chart, osc_chart = stock_chart_manager.plot(data=data)

    # 4. Setup TradingView Service (Intel Tab)
    tv_service = TradingViewService()
    summary = tv_service.get_technical_summary(symbol=stock_code)
    news = tv_service.get_latest_news(symbol=stock_code)

    print("\n" + "="*50)
    print(f" TRADING VIEW INTEL FOR {stock_code} ")
    print("="*50)
    if summary:
        print(f"Technical Summary: {summary}")
    else:
        print("Technical summary not available.")
    
    if news:
        print("\nLatest News:")
        for item in news[:5]: # Show top 5
            print(f"- {item}")
    else:
        print("News not available.")
    print("="*50 + "\n")

    # 5. Show Charts
    # In lightweight-charts, calling .show() on multiple Chart instances 
    # can cause "cannot start a process twice" because they share the same WV process.
    # To show multiple charts, we can't call .show() twice. 
    # Instead, we should use a single chart or check if the library supports multiple.
    # For now, we will show the main chart and since oscillator_chart is a separate instance,
    # we'll let the user know. 
    
    # Note: lightweight-charts currently typically supports one active WV process per script.
    main_chart.show(block=True)

if __name__ == "__main__":
    main()
