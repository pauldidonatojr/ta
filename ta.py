from tradingview_ta import TA_Handler, Interval
from datetime import datetime
import pytz

# Function to get current time in specific timezone
def get_current_time(timezone_str):
    timezone = pytz.timezone(timezone_str)
    return datetime.now(timezone)

# Map user inputs to Interval values
interval_dict = {
    "5 minutes": Interval.INTERVAL_5_MINUTES,
    "15 minutes": Interval.INTERVAL_15_MINUTES,
    "30 minutes": Interval.INTERVAL_30_MINUTES,
    "1 hour": Interval.INTERVAL_1_HOUR,
    "2 hours": Interval.INTERVAL_2_HOURS,
    "4 hours": Interval.INTERVAL_4_HOURS,
    "1 day": Interval.INTERVAL_1_DAY,
    "1 week": Interval.INTERVAL_1_WEEK,
}

# List to store symbols
symbols = []

# Display current date
print(f"Current Date: {datetime.now().date()}")

# Display current time in various timezones
print(f"Current time in East Coast US: {get_current_time('US/Eastern')}")
print(f"Current time in Pakistan: {get_current_time('Asia/Karachi')}")
print(f"Current time in England: {get_current_time('Europe/London')}")
print(f"Current time in China: {get_current_time('Asia/Shanghai')}")

# Ask user for number of coins to search
while True:
    num_coins = input("Do you want to check for 1 coin or multiple coins? Enter 1 for one coin and 2 for multiple coins: ")
    if num_coins == '1':
        symbol = input("Enter the symbol for the coin: ")
        symbols.append(symbol)
        break
    elif num_coins == '2':
        for i in range(3):
            symbol = input("Enter the symbol for coin " + str(i+1) + ": ")
            symbols.append(symbol)
        break
    else:
        print("Invalid input. Please enter either 1 or 2.")

# Ask user for the time interval
while True:
    time_interval = input("Enter the time interval (options: 5 minutes, 15 minutes, 30 minutes, 1 hour, 2 hours, 3 hours, 4 hours, 8 hours, 1 day, 1 week): ")
    if time_interval in interval_dict:
        break
    else:
        print("Invalid time interval. Valid options are: 5 minutes, 15 minutes, 30 minute, 1 hour, 2 hours, 3 hours, 4 hours, 8 hours, 1 day, 1 week.")

for symbol in symbols:
    output = TA_Handler(symbol=symbol, screener='Crypto', exchange='Binance', interval=interval_dict[time_interval])
    res = output.get_analysis().summary
    print(f"Symbol: {symbol}")
    print("Summary: ", res)
    print("========================================")
