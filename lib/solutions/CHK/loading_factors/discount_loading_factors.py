from collections import OrderedDict
from math import remainder

from ..constants import PRODUCT_STOCK_PRICES

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

    
    a5_applied_count = product_list['A']['5']['count']
    a3_applied_count = product_list['A']['3']['count']

    remainder_product_count = skus.count('A') - (a5_applied_count * a5 + a3_applied_count * a3) 

    apply_a5_discount = (a5_applied_count * product_price * a5) - (a5_applied_count * 50)
    apply_a3_discount = (a3_applied_count * product_price * a3) - (a3_applied_count * 20)

    price = apply_a5_discount + apply_a3_discount + (remainder_product_count * product_price)

    return price, skus

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
        except KeyError as e:
            breakpoint()
            product_price = products[item]
            product_quantity = skus.count(item)
            final_price += product_price * product_quantity
    breakpoint()
    return final_price








