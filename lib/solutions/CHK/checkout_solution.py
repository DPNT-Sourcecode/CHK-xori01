

# noinspection PyUnusedLocal
# skus = unicode string

class DiscountFactory:

    def build():
        pass


class AProductDiscountFactory(DiscountFactory):
    pass


class TellerSystem:
    def __init__(self, skus):
        self.skus = skus

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


def checkout(skus):
    teller = TellerSystem(skus=skus)


