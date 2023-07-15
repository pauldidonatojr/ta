from tradingview_ta import TA_Handler, Interval
output =TA_Handler(symbol='MATICUSDT',screener='Crypto',exchange='Binance',interval= Interval.INTERVAL_15_MINUTES)
res = output.get_analysis().summary
ind = output.get_analysis().indicators
print(res)
# print(ind)