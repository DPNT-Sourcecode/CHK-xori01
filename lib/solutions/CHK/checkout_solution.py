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
        sort_skus = ["".join(group) for _, group in groupby(sorted(skus)]
        self.skus = skus

    def calculate_price(self):
        


def checkout(skus):
    teller = TellerSystem(skus=skus)

    



