from collections import OrderedDict

from ..constants import PRODUCT_STOCK_PRICES

class ProductDiscountFactor:

    product_subset = []

    def __init__(self, cross_product_name=None):
        self.cross_product_name = cross_product_name

    def should_apply_discount(self, min, max, **kwargs):
        return bool(len(self.product_subset) >= min and len(self.product_subset) <= max)


class CrossProductDiscountFactor:

    product_subset = []

    def __init__(self, cross_product_name):
        self.cross_product_name = cross_product_name

    def should_apply_discount(
        self,
        min,
        max,
        skus_full_list,
    ):
        breakpoint()
        return bool(
            len(self.product_subset) >= min
            and len(self.product_subset) <= max
            and any(self.cross_product_name in word for word in skus_full_list) and "".join(skus_full_list).count(self.cross_product_name) % 2 == 0
        )

def product_a_pricing_factor(skus, product_list, product):
    number_a_products = skus.count("A")
    product_price = product['A']

    a5 = 5
    a3 = 3

    while number_a_products > 0:
        prioritise_a5 = number_a_products % a5
        
        if prioritise_a5 == 0:
            product_list['A']['5']['count'] += 1
            number_a_products -= a5
        elif number_a_products > 0 and prioritise_a5 == a3:
            product_list['A']['3']['count'] += 1
            number_a_products -= a3
        else:
            number_a_products -= 1

        



    return product_price, skus

def get_loading_factor(product_name):
    discount_loading_factors = OrderedDict([
        ('A', product_a_pricing_factor),
        ('B', product_a_pricing_factor),
        ('E', product_a_pricing_factor),
    ])

    return discount_loading_factors[product_name]

def apply_price_loading_factors(skus, product_discount_list, products):
    final_price = 0

    for item in PRODUCT_STOCK_PRICES.keys():
        try:
            discount_loading_factor = get_loading_factor(item)
            price, updated_skus = discount_loading_factor(skus, product_discount_list, products)
            skus = updated_skus
            final_price += price
        except KeyError:
            product_price = products[item]
            product_quantity = skus.count(item)
            final_price += product_price * product_quantity




