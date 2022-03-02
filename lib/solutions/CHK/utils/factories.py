from textwrap import wrap

class AbstractDiscountFactory:

    def build(self, product_subset):
        product_count = len(product_subset)
        price_before_discount = product_count * kwargs['product_price']
        return price_before_discount

class AProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self):
        self.discounts = {
            '3A': 20
        }
    
    def build(self, product_subset, **kwargs):
        product_count = len(product_subset)
        price_before_discount = product_count * kwargs['product_price']
        chunk_product_subset = wrap(product_subset, 3)

        for chunk in chunk_product_subset:
            if len(chunk) == 3:
                price_before_discount -= self.discounts['3A']
            
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

