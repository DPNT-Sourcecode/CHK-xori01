from textwrap import wrap
from copy import deepcopy

class AbstractDiscountFactory:

    def build(self, product_subset, **kwargs):
        product_count = len(product_subset)
        price_before_discount = product_count * kwargs['product_price']
        return price_before_discount

class AProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self):
        self.discounts = {
            '3A': 20,
            '5A': 50
        }
    
    def build(self, product_subset, **kwargs):
        product_count = len(product_subset)
        price_before_discount = product_count * kwargs['product_price']
        clone_product_subset = deepcopy(product_subset)

        chunks = []

        while len(clone_product_subset) > 0:
            chunk_target = 

        if product_count % 5 == 0:
            flt = product_count / 5
            price_before_discount -= (self.discounts['5A'] * flt)

        else:
            if len(product_subset[:5]) == 5:
                price_before_discount -= self.discounts['5A']
                tmp_string = tmp_string[:-5]
            
            if len(product_subset[:3]) == 3:
                price_before_discount -= self.discounts['3A']
                tmp_string = tmp_string[:-3]
            
        return price_before_discount


class BProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self):
        self.discounts = {
            '2B': 15
        }
    
    def build(self, product_subset, **kwargs):
        product_count = len(product_subset)
        price_before_discount = product_count * kwargs['product_price']
        chunk_product_subset = wrap(product_subset, 2)

        for chunk in chunk_product_subset:
            if len(chunk) == 2:
                price_before_discount -= self.discounts['2B']
            
        return price_before_discount

class EProductDiscountFactory(AbstractDiscountFactory):
    
    def build(self, product_subset, **kwargs):
        product_count = len(product_subset)
        price_before_discount = product_count * kwargs['product_price']
        chunk_product_subset = wrap(product_subset, 2)
        for chunk in chunk_product_subset:
            if len(chunk) == 2 and 'B' in kwargs['product_list']:
                b_product_price = kwargs['stock_list']['B']['price']
                price_before_discount -= b_product_price
            
        return price_before_discount
