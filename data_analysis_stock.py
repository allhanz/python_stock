import numpy as np
import pandas as pd

names = ['AAPL','GOOG','MSFT','DELL','GS','MS','BAC','C']
def get_px(stock,start,end):
	return web.get_data_yahoo(stock,start,end)['Adj Close']

px = DataFrame({n: get_px(n,'1/1/2009','6/1/2012')for n in names})
px = ps.asfreq('B').fillna(method='pad')
rets = px.pct_change()
((1+rets).cumprod()-1).plot()
