from itertools import groupby
from textwrap import wrap

# noinspection PyUnusedLocal
# skus = unicode string

class AbstractDiscountFactory:

    def __init__(self, stock_price):
        self.stock_price = stock_price

    def build(self, *args, **kwargs):
        return self.stock_price

class AProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self, stock_price):
        self.discounts = {
            '3A': {
                'count': 3,
                'discount_to_apply': 20
            }
        }
        self.stock_price = stock_price
    
    def build(self, product_subset):
        max_count = 5
        product_count = len(product_subset)
        price_before_discount = product_count * self.stock_price
        get_first_3 = product_subset[:2]
        if len(get_first_3) % 3 == 0:
            price_before_discount -= self.discounts['3A']['discount_to_apply']

        breakpoint()
        return price_before_discount

class BProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self, stock_price):
        self.discounts = {
            '2B': 15
        }
        self.stock_price = stock_price
    
    def build(self, product_subset):
        product_count = len(product_subset)
        price_before_discount = product_count * self.stock_price

        if product_count % 2 == 0:
            price_before_discount -= self.discounts['2B']
            return price_before_discount

        return price_before_discount

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

    








