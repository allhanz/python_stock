import jsm
import numpy as np
import pandas as pd
import datetime

start_time = datetime.date(2010,1,1)
end_time = datetime.date(2015,12,31)

stock_getter=jsm.Quotes()
stock_getter_csv=jsm.QuotesCsv()

symbol_list=[4901,4689]
#price_data =[]
time_period =jsm.MONTHLY
price_current_data = stock_getter.get_price()

price_historical_data =stock_getter.get_historical_prices(symbol_list[0],time_period,start_time,end_time)

print(price_historical_data)

price_data_csv = stock_getter_csv.save_historical_prices(symbol_list[1],time_period,start_time,end_time)
print(price_data_csv)