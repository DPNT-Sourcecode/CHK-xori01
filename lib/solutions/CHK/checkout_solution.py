from itertools import groupby

from .utils.factories import ProductDiscountFactorFactory
from .constants import PRODUCT_STOCK_PRICES

# noinspection PyUnusedLocal
# skus = unicode string

class DiscountHandler():
    
    def __init__(self):
        self.discount_factories = {
            'A': ProductDiscountFactorFactory(['5A', '3A']),
            'B': ProductDiscountFactorFactory(['2B']),
            'E': ProductDiscountFactorFactory(['2E']),
        }

    def apply(self, product_name, **kwargs):
        try:
            discounts = self.discount_factories[product_name].build(
                product_subset=kwargs['sku_subset'],
                skus_full_list=kwargs['skus_full_list'],
            )
            return discounts
        except KeyError:
            return []


class InvalidInputException(Exception):
    pass

PRODUCTS = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

def checkout(skus):
    try:
        allowed_choices = ["".join(key) for key in PRODUCT_STOCK_PRICES.keys()]

        if not isinstance(skus, str) or not all(
            allowed_sku in allowed_choices for allowed_sku in skus
        ):
            raise InvalidInputException("Invalid input detected")

        product_discounts_list = {
           'E': {
               '2': {
                   'count': 0,
                   "discount": 0,
                   'discount_threshold': 2,
               }
           },
           'A': {
               '5': {
                   'count': 0,
                   "discount": 0,
                   'discount_threshold': 5,
               },
               '2': {
                   'count': 0,
                   "discount": 0,
                   'discount_threshold': 2,
               }
           },
           'B': {
               '2': {
                   'count': 0,
                   "discount": 0,
                   'discount_threshold': 2,
               }
           },
       }

       
                    
    except InvalidInputException:
        return -1


