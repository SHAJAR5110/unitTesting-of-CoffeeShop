import unittest
from lab9 import CoffeeShop

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.shop = CoffeeShop()

    def test_calculate_total_valid(self):
        self.assertEqual(self.shop.calculate_total(2, 3), 40)
        self.assertEqual(self.shop.calculate_total(0, 0), 0)
        self.assertEqual(self.shop.calculate_total(5, 0), 25)

    def test_calculate_total_with_negative_values(self):
        with self.assertRaises(ValueError):
            self.shop.calculate_total(-1, 2)
        with self.assertRaises(ValueError):
            self.shop.calculate_total(2, -1)

    def test_calculate_total_after_price_update(self):
        self.shop.update_menu_prices(coffee_price=6, sandwich_price=12)
        self.assertEqual(self.shop.calculate_total(1, 1), 18)  
        self.assertEqual(self.shop.calculate_total(3, 2), 42)  

    def test_update_menu_prices(self):
        self.shop.update_menu_prices(coffee_price=7)
        self.assertEqual(self.shop.coffee_price, 7)
        self.assertEqual(self.shop.sandwich_price, 10)

        self.shop.update_menu_prices(sandwich_price=15)
        self.assertEqual(self.shop.sandwich_price, 15)

if __name__ == '__main__':
    unittest.main()
