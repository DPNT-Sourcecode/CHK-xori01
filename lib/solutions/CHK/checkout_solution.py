from itertools import groupby

# noinspection PyUnusedLocal
# skus = unicode string

class AbstractDiscountFactory:

    def build():
        pass

class AProductDiscountFactory(AbstractDiscountFactory):

    def __init__(self, stock_price):
        self.discounts = {
            '3A': 20
        }
        self.stock_price = stock_price
    
    def build(self, product_subset):
        product_count = len(product_subset)
        price_before_discount = product_count * self.stock_price
        price_after_discount = 0

        if product_count % 3 == 0:
            price_before_discount -= self.discounts['3A']
            breakpoint()
            return price_after_discount

        return price_before_discount

class InvalidInputException(Exception):
    pass


class TellerSystem:
    def __init__(self):
        self.stock = {
            'A': {
                'price': 50,
                'discount': AProductDiscountFactory(50)
            },
            'B': {
                'price': 30,
                'discount': AbstractDiscountFactory()
            },
            'C': {
                'price': 20,
                'discount': AbstractDiscountFactory()
            },
            'D': {
                'price': 15,
                'discount': AbstractDiscountFactory()
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
            discount_factory = self.stock[product_name]['discount']
            total_cost += discount_factory.build(product_subset)

        return total_cost

def checkout(skus):
    try:
        teller = TellerSystem()
        teller.load_in_skus(skus=skus)
        return teller.calculate_price()
    except InvalidInputException:
        return -1

    








