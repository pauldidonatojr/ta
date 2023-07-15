def calculate_leverage_profit(opening_price, closing_price, leverage, investment):
    profit_loss = (closing_price - opening_price) / opening_price * leverage * investment
    return profit_loss

# Use the function
opening_price = float(input("Enter the opening price: "))
closing_price = float(input("Enter the closing price: "))
leverage = float(input("Enter the leverage: "))
investment = float(input("Enter the investment amount: "))

profit_loss = calculate_leverage_profit(opening_price, closing_price, leverage, investment)
print(f"The profit or loss is: {profit_loss}")
