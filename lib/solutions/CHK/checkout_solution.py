from itertools import groupby

# noinspection PyUnusedLocal
# skus = unicode string

class DiscountFactory:

    def build():
        pass


class AProductDiscountFactory(DiscountFactory):
    pass

class InvalidInputException(Exception):
    pass


class TellerSystem:
    def __init__(self, skus):


        self.stock = {
            'A': {
                'price': 50,
            },
            'B': {
                'price': 30,
            },
            'C': {
                'price': 20,
            },
            'D': {
                'price': 15,
            },
        }
        sort_skus = ["".join(group) for _, group in groupby(sorted(skus))]
        self.skus = sort_skus

    def load_in_skus(self, skus):

        allowed_choices = ["".join(key) for key in self.stock.keys()]

        if not isinstance(skus, str) or not all(allowed_sku in allowed_choices for allowed_sku in skus):
            raise InvalidInputException("Invalid input detected")


        sort_skus = ["".join(group) for _, group in groupby(sorted(skus))]
        self.skus = sort_skus

    def calculate_price(self):
        products = self.skus
        total_cost = 0
        for product in products:
            total_cost += len(product) * self.stock[product]['price']

def checkout(skus):
    try:
        teller = TellerSystem(skus=skus)
    except 
    return teller.calculate_price()

    

