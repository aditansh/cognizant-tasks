# Define the order amount
order_amount = 150

# Function to apply a discount if the order amount is over $100
def apply_discount(order_amount):
    if order_amount > 100:
        return order_amount * 0.9  # Apply 10% discount
    else:
        return order_amount

# Calculate the final price for the example order
final_price = apply_discount(order_amount)

# Print the final price after applying the discount
print(f"Final price after discount: ${final_price}")
