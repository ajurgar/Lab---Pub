import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
   
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        
    def test_pub_has_name(self):
        actual = self.pub.name
        self.assertEqual("The Prancing Pony", actual)

    def test_pub_till_starts_100(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_can_increase_till(self):
        self.pub.increase_till(25.00)
        self.assertEqual(125.00, self.pub.till)

    def test_number_of_drinks(self):
        self.assertEqual(3, len(self.pub.drinks))