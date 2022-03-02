from textwrap import wrap

class AbstractDiscountFactory:

    def __init__(self, stock_price):
        self.stock_price = stock_price

    def build(self, product_subset):
        product_count = len(product_subset)
        price_before_discount = product_count * self.stock_price
        return price_before_discount

class AProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self, stock_price):
        self.discounts = {
            '3A': 20
        }
        self.stock_price = stock_price
    
    def build(self, product_subset,skus_list=None):):
        product_count = len(product_subset)
        price_before_discount = product_count * self.stock_price
        chunk_product_subset = wrap(product_subset, 3)

        for chunk in chunk_product_subset:
            if len(chunk) == 3:
                price_before_discount -= self.discounts['3A']
            
        return price_before_discount

class BProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self, stock_price):
        self.discounts = {
            '2B': 15
        }
        self.stock_price = stock_price
    
    def build(self, product_subset, skus_list=None):
        product_count = len(product_subset)
        price_before_discount = product_count * self.stock_price
        chunk_product_subset = wrap(product_subset, 2)

        for chunk in chunk_product_subset:
            if len(chunk) == 2:
                price_before_discount -= self.discounts['2B']
            
        return price_before_discount

class EProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self, stock_price):
        self.stock_price = stock_price
    
    def build(self, product_subset, skus_list):
        product_count = len(product_subset)
        price_before_discount = product_count * self.stock_price
        chunk_product_subset = wrap(product_subset, 2)
        for chunk in chunk_product_subset:
            if len(chunk) == 2 and:
                price_before_discount -= self.discounts['2B']
            
        return price_before_discount
