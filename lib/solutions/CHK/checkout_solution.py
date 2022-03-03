from itertools import groupby

from .utils.factories import ProductDiscountFactorFactory

from .loading_factors.discount_loading_factors import (ProductDiscountFactor, CrossProductDiscountFactor)

# noinspection PyUnusedLocal
# skus = unicode string

PRODUCT_STOCK_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

DISCOUNT_LIST = {
    '3A': {
        'discount': 20,
        "loading_factor": ProductDiscountFactor(),
        'rules': {
            'min': 3,
            'max': 4,
        }
    },
    '5A': {
        'discount': 50,
        "loading_factor": ProductDiscountFactor(),
        'rules': {
            'min': 5,
            'max': 5,
        }
    },
    '2A': {
        'discount': 15,
        "loading_factor": ProductDiscountFactor(),
        'rules': {
            'min': 2,
            'max': 2,
        }
    },
    '2E': {
        'discount': PRODUCT_STOCK_PRICES['B'],
        "loading_factor": CrossProductDiscountFactor(cross_product_name='B'),
        'rules': {
            'min': 3,
            'max': 4,
        }
    },
}

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

def checkout(skus):
    try:
        allowed_choices = ["".join(key) for key in PRODUCT_STOCK_PRICES.keys()]

        if not isinstance(skus, str) or not all(
            allowed_sku in allowed_choices for allowed_sku in skus
        ):
            raise InvalidInputException("Invalid input detected")

        final_price = 0
        sort_skus = ["".join(group) for _, group in groupby(sorted(skus))]

        for sku_subset in sort_skus:
            product_name = sku_subset[0]
            product_price = PRODUCT_STOCK_PRICES[product_name]
            price_before_discount = len(sku_subset) * product_price
            price_after_discount = price_before_discount
            discounts = DiscountHandler().apply(product_name, sku_subset=sku_subset, skus_full_list=sort_skus)
            print(discounts)

            for discount in discounts:
                amount = discount['amount']
                price_after_discount -= amount

            final_price += price_after_discount
                    
    except InvalidInputException:
        return -1


