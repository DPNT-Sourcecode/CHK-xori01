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
            'A': ProductDiscountFactorFactory()
        }

    def apply(self, product_name, **kwargs):
        discounts = self.discount_factories[product_name].build(
            
        )


class InvalidInputException(Exception):
    pass


class TellerSystem:
    def __init__(self):
        self.stock = {
            "A": {"price": 50, "discount_loading_factor": AProductDiscountFactory()},
            "B": {"price": 30, "discount_loading_factor": BProductDiscountFactory()},
            "C": {"price": 20, "discount_loading_factor": AbstractDiscountFactory()},
            "D": {"price": 15, "discount_loading_factor": AbstractDiscountFactory()},
            "E": {"price": 40, "discount_loading_factor": EProductDiscountFactory()},
        }

    def load_in_skus(self, skus):

        allowed_choices = ["".join(key) for key in self.stock.keys()]

        if not isinstance(skus, str) or not all(
            allowed_sku in allowed_choices for allowed_sku in skus
        ):
            raise InvalidInputException("Invalid input detected")

        sort_skus = ["".join(group) for _, group in groupby(sorted(skus))]
        self.skus = sort_skus

    def calculate_price(self):
        products_list = self.skus
        total_cost = 0
        final_price = 0
        for product_subset in products_list:
            product_name = product_subset[0]
            product_price = self.stock[product_name]["price"]
            discount_factory = self.stock[product_name]["discount_loading_factor"]
            total_cost += discount_factory.build(
                product_subset,
                product_price=product_price,
                stock_list=self.stock,
                product_list=products_list,
            )

        return total_cost


def checkout(skus):
    try:
        teller = TellerSystem()
        teller.load_in_skus(skus=skus)
        return teller.calculate_price()
    except InvalidInputException:
        return -1
