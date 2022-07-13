import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
   
    def setUp(self):
        
        self.customer = Customer("Michael", 150)

        self.drink_1 = Drink("Whisky", 10)
        self.drink_2 = Drink("Rum", 5)
        self.drink_3 = Drink("Tequila", 8)

        drinks = [self.drink_1, self.drink_2, self.drink_3]

        self.pub = Pub("The Prancing Pony", 100.00, drinks)

    def test_pub_has_name(self):
        actual = self.pub.name
        self.assertEqual("The Prancing Pony", actual)

    def test_pub_till_starts_100(self):
        self.assertEqual(100.00, self.pub.till)
    
    
    def test_number_of_drinks(self):
        self.assertEqual(3, len(self.pub.drinks))

    
    def test_can_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110.00, self.pub.till)

    
    def test_can_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Whisky")
        self.assertEqual("Whisky", self.drink_1.name)


    def test_can_sell_drink_to_customer(self):
        customer = Customer("Michael", 150)
        self.pub.increase_till(10)
        self.customer.reduce_cash(10)
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(140, self.customer.wallet)

