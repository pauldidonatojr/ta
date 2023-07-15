def calculate_liquidation_price(entry_price, margin_percentage, leverage, position_type):
    if position_type.lower() == 'long':
        liquidation_price = entry_price / (1 - margin_percentage * leverage)
    elif position_type.lower() == 'short':
        liquidation_price = entry_price / (1 + margin_percentage * leverage)
    else:
        return "Invalid position type. Must be 'long' or 'short'."
    return liquidation_price

# Use the function
entry_price = float(input("Enter the entry price: "))
margin_percentage = float(input("Enter the initial margin percentage (as a decimal): "))
leverage = float(input("Enter the leverage: "))
position_type = input("Enter the position type (long/short): ")

liquidation_price = calculate_liquidation_price(entry_price, margin_percentage, leverage, position_type)
print(f"The liquidation price is: {liquidation_price}")
