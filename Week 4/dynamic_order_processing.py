# Define the DiscountStrategy interface
class DiscountStrategy:
    def apply_discount(self, order_amount):
        pass

# Implement different discount strategies
class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.9

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.8

# Define the Order class
class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount
        self.strategy = self._get_discount_strategy()

    def _get_discount_strategy(self):
        if self.customer_type == "regular":
            return RegularDiscount()
        elif self.customer_type == "premium":
            return PremiumDiscount()
        elif self.customer_type == "vip":
            return VIPDiscount()

    def final_price(self):
        return self.strategy.apply_discount(self.order_amount)

# Create instances of Order for different customer types and calculate the final price
regular_order = Order("regular", 150)
premium_order = Order("premium", 150)
vip_order = Order("vip", 150)

# Print the final prices after applying discounts
print(f"Final price for regular customer: ${regular_order.final_price()}")
print(f"Final price for premium customer: ${premium_order.final_price()}")
print(f"Final price for VIP customer: ${vip_order.final_price()}")
