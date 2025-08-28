# Function to calculate final price after applying discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
    else:
        final_price = price
    return final_price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Validate inputs
    if price < 0 or discount_percent < 0:
        print("Price and discount percentage cannot be negative.")
    else:
        # Calculate and display final price
        final_price = calculate_discount(price, discount_percent)
        print(f"The final price is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")