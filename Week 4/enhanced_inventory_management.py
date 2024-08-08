import threading
import time

# Define the Inventory class
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name, quantity):
        if name in self.items and self.items[name] >= quantity:
            self.items[name] -= quantity
        else:
            print(f"Insufficient stock of {name} to remove {quantity} units.")

    def check_stock(self):
        for name, quantity in self.items.items():
            if quantity == 0:
                print(f"{name} is out of stock!")
            elif quantity < 5:
                print(f"{name} is low on stock!")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for name, quantity in self.items.items():
                    file.write(f"{name},{quantity}\n")
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.items = {}
                for line in file:
                    name, quantity = line.strip().split(',')
                    self.items[name] = int(quantity)
        except IOError as e:
            print(f"Error loading inventory from file: {e}")

# Periodically check stock levels and print restocking alerts
def stock_check_periodically(inventory):
    while True:
        inventory.check_stock()
        time.sleep(10)  # Check every 10 seconds

# Create an inventory instance, perform operations, and save the state to a file
inventory = Inventory()
inventory.add_item("item1", 10)
inventory.add_item("item2", 3)
inventory.add_item("item3", 0)

# Start a thread to check stock levels periodically
thread = threading.Thread(target=stock_check_periodically, args=(inventory,))
thread.start()

# Save the inventory state to a file
inventory.save_to_file('inventory.txt')

# Load the inventory state from the file and print it
inventory.load_from_file('inventory.txt')
print("Loaded inventory state:", inventory.items)
