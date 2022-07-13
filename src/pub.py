class Pub:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount
    
    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if name == drink.name:
                return drink

    def sell_drink_to_customer(self, drink, amount):
        drink = self.find_drink_by_name(drink)
        self.increase_till(amount)
        self.customer.reduce_cash(amount)