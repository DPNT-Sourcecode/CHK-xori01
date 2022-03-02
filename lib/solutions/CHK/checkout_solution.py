from itertools import groupby

# noinspection PyUnusedLocal
# skus = unicode string

class DiscountFactory:

    def build():
        pass


class AProductDiscountFactory(DiscountFactory):
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

    def calculate_price(self):
        products = self.skus
        total_cost = 0
        for product in products:
            total_cost += len(product) * self.stock[product]['price']

def checkout(skus):
    try:
        allowed_choices = [ for key in  ]
        teller = TellerSystem(skus=skus)
        if not isinstance(skus, str) and 
    except
    return teller.calculate_price()

    
