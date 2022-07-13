import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Whisky", 10)
    def test_drink_type(self):
        self.assertEqual("Whisky", self.drink.name)
    def test_drink_price(self):
        self.assertEqual(10, self.drink.price)