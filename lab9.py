class CoffeeShop:
    def __init__(self, coffee_price=5, sandwich_price=10):
        self.coffee_price = coffee_price
        self.sandwich_price = sandwich_price

    def calculate_total(self, coffee_count, sandwich_count):
        if coffee_count < 0 or sandwich_count < 0:
            raise ValueError("Item counts cannot be negative.")
        return (coffee_count * self.coffee_price) + (sandwich_count * self.sandwich_price)

    def update_menu_prices(self, coffee_price=None, sandwich_price=None):
        if coffee_price is not None:
            self.coffee_price = coffee_price
        if sandwich_price is not None:
            self.sandwich_price = sandwich_price
