class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = ["Bacardi", "Jack Daniels", "Tequila"]

    def increase_till(self, amount):
        self.till += amount
