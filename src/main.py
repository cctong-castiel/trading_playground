import datetime
from dateutil.relativedelta import relativedelta
from src.trading_funcs.charting import StockChart
from src.utils.logs import set_up_log


logger = set_up_log(__name__)


if __name__ == "__main__":

    # input the stock code
    stock_code = input("Enter stock code (e.g., AAPL): ").strip().upper()
    if not stock_code:
        logger.info("No stock code provided. Exiting.")
        exit()

    # initialization
    stock_data_path = "./src/data"
    start_date = (datetime.datetime.now() - relativedelta(years=3)).strftime('%Y-%m-%d')
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
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
    data = stock_chart.get_bar_data(stock_code=stock_code)
    chart_plot = stock_chart.plot(data=data)
    chart_plot.show(block=True)  # This will open the chart in a web browser