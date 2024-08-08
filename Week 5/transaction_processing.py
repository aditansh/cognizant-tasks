import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='transaction_errors.log', level=logging.ERROR)

# Function to log errors
def log_error(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.error(f"{timestamp} - {message}")

# Example transaction processing function
def process_transaction(transaction_amount):
    try:
        if not isinstance(transaction_amount, (int, float)):
            raise ValueError("Transaction amount must be a number.")
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        
        # Simulate processing
        print(f"Processing transaction of amount: ${transaction_amount}")
    
    except ValueError as e:
        print(f"Error: {e}")
        log_error(str(e))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        log_error(str(e))

# Validate user input
def get_transaction_amount():
    while True:
        try:
            amount = float(input("Enter transaction amount: "))
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            return amount
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            log_error(str(e))

# Example usage
try:
    amount = get_transaction_amount()
    process_transaction(amount)
except Exception as e:
    print(f"An error occurred: {e}")
    log_error(str(e))
