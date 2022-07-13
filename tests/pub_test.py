import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
   
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        
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

    # def test_can_find_pet_by_name(self):
    #     pet = self.pet_shop.find_pet_by_name("Sir Percy")
    #     self.assertEqual("Sir Percy", pet.name)
    def test_can_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Bacardi")
        self.assertEqual("Bacardi", drink.name)


    def test_can_sell_drink_to_customer(self):
        customer = Customer("Michael", 150)
        self.pub.increase_till(10)
        self.customer.reduce_cash(10)
        self.assertEqual(110.00, self.pub.till)
        self.assertEqual(140, self.customer.wallet)



        #  def test_can_sell_pet_to_customer(self):
        # customer = Customer("Jack Jarvis", 1000)
        # self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
        # self.assertEqual(500, customer.cash)
        # self.assertEqual(1500, self.pet_shop.total_cash)