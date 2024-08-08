# 1. Lists
product_names = ["Product1", "Product2", "Product3"]

def add_product(name):
    product_names.append(name)

def remove_product(name):
    if name in product_names:
        product_names.remove(name)

def update_product(index, new_name):
    if 0 <= index < len(product_names):
        product_names[index] = new_name

# 2. Dictionaries
product_details = {
    "Product1": {"quantity": 10, "price": 100},
    "Product2": {"quantity": 5, "price": 200},
    "Product3": {"quantity": 20, "price": 50},
}

def add_product_details(name, quantity, price):
    product_details[name] = {"quantity": quantity, "price": price}

def update_product_details(name, quantity=None, price=None):
    if name in product_details:
        if quantity is not None:
            product_details[name]["quantity"] = quantity
        if price is not None:
            product_details[name]["price"] = price

def delete_product_details(name):
    if name in product_details:
        del product_details[name]

# 3. Tuples
product_catalog = (
    ("Product1", 100),
    ("Product2", 200),
    ("Product3", 50),
)

def display_product_catalog():
    for product in product_catalog:
        print(product)

# 4. Sets
product_categories = {"Electronics", "Clothing", "Books"}

def add_category(category):
    product_categories.add(category)

def remove_category(category):
    if category in product_categories:
        product_categories.remove(category)

# 5. Combining Collections
def generate_report():
    sorted_products = sorted(product_details.items(), key=lambda x: x[1]["price"])
    for name, details in sorted_products:
        print(f"{name}: ${details['price']}")

def find_products_in_price_range(min_price, max_price):
    result = {name for name, details in product_details.items() if min_price <= details["price"] <= max_price}
    return result

# Example usage
add_product("Product4")
update_product(0, "UpdatedProduct1")

add_product_details("Product4", 15, 300)
update_product_details("Product1", price=120)

print("Product catalog:")
display_product_catalog()

generate_report()

print("Products in price range $100-$200:", find_products_in_price_range(100, 200))

