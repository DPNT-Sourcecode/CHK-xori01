from collections import OrderedDict

from .loading_factors.discount_loading_factors import apply_price_loading_factors
from .constants import PRODUCT_STOCK_PRICES

# noinspection PyUnusedLocal
# skus = unicode string


class InvalidInputException(Exception):
    pass

def checkout(skus):
    try:
        allowed_choices = ["".join(key) for key in PRODUCT_STOCK_PRICES.keys()]

        if not isinstance(skus, str) or not all(
            allowed_sku in allowed_choices for allowed_sku in skus
        ):
            raise InvalidInputException("Invalid input detected")

        tmp_list = OrderedDict([
            ('E', (2, (0, 0, 2)))
        ])

        breakpoint()

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
               '3': {
                   'count': 0,
                   "discount": 0,
                   'discount_threshold': 3,
               }
           },
           'B': {
               '2': {
                   'count': 0,
                   "discount": 0,
                   'discount_threshold': 2,
               }
           },
           'F': {
               '3': {
                   'count': 0,
                   "discount": 0,
                   'discount_threshold': 3,
               }
           },
           'H': {
               '5': {
                    'count': 0,
                    "discount": 0,
                    'discount_threshold': 5,
               },
               '10': {
                    'count': 0,
                    "discount": 0,
                    'discount_threshold': 10,
               }
           },
           "K": {

           }
       }

        return apply_price_loading_factors(skus, product_discounts_list, PRODUCT_STOCK_PRICES)


                    
    except InvalidInputException:
        return -1


