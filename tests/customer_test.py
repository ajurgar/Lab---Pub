import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Alex", 50)

    def test_customer_name(self):
        self.assertEqual("Alex", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_reduce_money(self):
        self.customer.reduce_cash(10)
        self.assertEqual(40, self.customer.wallet)