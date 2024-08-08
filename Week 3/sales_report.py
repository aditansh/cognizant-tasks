# Define a list of sales amounts
sales = [200, 600, 150, 800, 300]

# Function to generate a report for the sales list
def generate_report(sales):
    total_sales = 0
    for sale in sales:
        total_sales += sale
        if sale > 500:
            print(f"Sale amount: ${sale} (Over $500)")
        else:
            print(f"Sale amount: ${sale}")
    
    print(f"Total sales for the month: ${total_sales}")

# Generate the report for the example sales list
generate_report(sales)
