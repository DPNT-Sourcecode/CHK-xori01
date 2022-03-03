from itertools import groupby

from .utils.factories import ProductDiscountFactorFactory, CrossProductDiscountFactorFactory
from .constants import PRODUCT_STOCK_PRICES

# noinspection PyUnusedLocal
# skus = unicode string

class DiscountHandler():
    
    def __init__(self):
        self.discount_factories = {
            'A': ProductDiscountFactorFactory(['5A', '3A']),
            'B': CrossProductDiscountFactorFactory(cross_product_name='EE', discounts_to_apply=['2B']),
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

        price_before_discount = 0

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
        return final_price
                    
    except InvalidInputException:
        return -1

