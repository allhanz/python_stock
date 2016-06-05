from yahoo_finance import Share
yahoo= Share('YHOO')
print('stock information:')
print(yahoo.get_open())
print(yahoo.get_price())
print(yahoo.get_trade_datetime())

print ('refresh the data')
yahoo.refresh()
print(yahoo.get_price())
print(yahoo.get_trade_datetime())
