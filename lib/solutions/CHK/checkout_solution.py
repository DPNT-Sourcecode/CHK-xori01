from itertools import groupby

from .utils import factories

# noinspection PyUnusedLocal
# skus = unicode string



class InvalidInputException(Exception):
    pass


class TellerSystem:
    def __init__(self):
        self.stock = {
            'A': {
                'discount_loading_factor': AProductDiscountFactory(50)
            },
            'B': {
                'discount_loading_factor': BProductDiscountFactory(30)
            },
            'C': {
                'discount_loading_factor': AbstractDiscountFactory(20)
            },
            'D': {
                'discount_loading_factor': AbstractDiscountFactory(15)
            },
            'E': {
                'discount_loading_factor': AbstractDiscountFactory(40)
            }
        }

    def load_in_skus(self, skus):

        allowed_choices = ["".join(key) for key in self.stock.keys()]

        if not isinstance(skus, str) or not all(allowed_sku in allowed_choices for allowed_sku in skus):
            raise InvalidInputException("Invalid input detected")


        sort_skus = ["".join(group) for _, group in groupby(sorted(skus))]
        self.skus = sort_skus

    def calculate_price(self):
        products_list = self.skus
        total_cost = 0
        for product_subset in products_list:
            product_name = product_subset[0]
            discount_factory = self.stock[product_name]['discount_loading_factor']
            total_cost += discount_factory.build(product_subset)

        return total_cost

def checkout(skus):
    try:
        teller = TellerSystem()
        teller.load_in_skus(skus=skus)
        return teller.calculate_price()
    except InvalidInputException:
        return -1

    




