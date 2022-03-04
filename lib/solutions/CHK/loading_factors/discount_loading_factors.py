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

def product_b_pricing_factor(skus, product_list, product):
    number_a_products = skus.count("B")
    product_price = product['B']

    b2 = 2

    while number_a_products > 0:
        if number_a_products > 0 and number_a_products % b2 == 0:
            product_list['B']['2']['count'] += 1
            number_a_products -= b2
        else:
            number_a_products -= 1

    
    b2_applied_count = product_list['B']['2']['count']

    remainder_product_count = skus.count('B') - (b2_applied_count * b2) 

    apply_b2_discount = (b2_applied_count * product_price * b2) - (b2_applied_count * 15)

    price = apply_b2_discount + (remainder_product_count * product_price)

    return price, skus

def product_e_pricing_factor(skus, product_list, product):
    number_e_products = skus.count("E")
    number_b_products = skus.count("B")

    product_price = product['E']
    product_discount_2e = product_list['E']['2']

    e2 = product_discount_2e['discount_threshold']

    while number_e_products > 0:
        if number_e_products > 0 and number_e_products % e2 == 0:
            if number_b_products > 0:
                skus = skus.replace('B', '', 1)
            
            product_discount_2e['count'] += 1
            number_e_products -= e2
        else:
            number_e_products -= 1

    
    e2_applied_count = product_discount_2e['count']

    remainder_product_count = skus.count('E') - (e2_applied_count * e2) 

    apply_b2_discount = (e2_applied_count * product_price * e2)

    price = apply_b2_discount + (remainder_product_count * product_price)

    return price, skus

def product_f_pricing_factor(skus, product_list, product):
    number_f_products = skus.count("F")
    product_price = product['F']
    product_discount_3f = product_list['F']['3']

    f3 = product_discount_3f['discount_threshold']

    while number_f_products > 0:
        if number_f_products > 0 and number_f_products % f3 == 0:
            product_list['F']['3']['count'] += 1
            number_f_products -= f3
        else:
            number_f_products -= 1

    
    f3_applied_count = product_discount_3f['count']

    remainder_product_count = skus.count('F') - (f3_applied_count * f3) 

    apply_f3_discount = (f3_applied_count * product_price * f3) - (f3_applied_count * 10)

    price = apply_f3_discount + (remainder_product_count * product_price)

    return price, skus

def product_h_pricing_factor(skus, product_list, product):
    number_of_products = skus.count("H")
    product_price = product['H']
    product_discount_10h = product_list['H']['10']
    product_discount_5h = product_list['H']['5']

    h10 = product_discount_10h['discount_threshold']
    h5 = product_discount_5h['discount_threshold']

    while number_of_products > 0:
        prioritise_h10 = number_of_products % h10
        
        if prioritise_h10 == 0:
            product_discount_10h['count'] += 1
            number_of_products -= h10
        elif number_of_products > 0 and prioritise_h10 == h5:
            product_discount_5h['count'] += 1
            number_of_products -= h5
        else:
            number_of_products -= 1

    
    h10_applied_count = product_discount_10h['count']
    h5_applied_count = product_discount_5h['count']

    remainder_product_count = skus.count('H') - (h10_applied_count * h10 + h5_applied_count * h5) 

    apply_h10_discount = (h10_applied_count * product_price * h10) - (h10_applied_count * 20)
    apply_h5_discount = (h5_applied_count * product_price * h5) - (h5_applied_count * 5)

    price = apply_h10_discount + apply_h5_discount + (remainder_product_count * product_price)

    return price, skus

def product_k_pricing_factor(skus, product_list, product):
    number_k_products = skus.count("K")
    product_price = product['K']
    product_discount_2k = product_list['K']['2']

    k2 = product_discount_2k['discount_threshold']

    while number_k_products > 0:
        if number_k_products > 0 and number_k_products % k2 == 0:
            product_list['K']['2']['count'] += 1
            number_k_products -= k2
        else:
            number_k_products -= 1

    
    k2_applied_count = product_discount_2k['count']

    remainder_product_count = skus.count('K') - (k2_applied_count * k2) 

    apply_k2_discount = (k2_applied_count * product_price * k2) - (k2_applied_count * 10)

    price = apply_k2_discount + (remainder_product_count * product_price)

    return price, skus

def product_loading_factor_one_discount(skus, product_list, product, product_name, rule):
    number_of_products = skus.count(product_name)
    product_price = product[product_name]
    breakpoint()
    product_discount_data_object = product_list[product_name][rule]

    discount_threshold = product_discount_data_object['discount_threshold']

    while number_of_products > 0:
        if number_of_products > 0 and number_of_products % discount_threshold == 0:
            product_list['K']['2']['count'] += 1
            number_of_products -= discount_threshold
        else:
            number_of_products -= 1

    
    applied_discount = product_discount_data_object['count']

    remainder_product_count = skus.count(product_name) - (applied_discount * discount_threshold) 

    apply_discount = (applied_discount * product_price * discount_threshold) - (applied_discount * 10)

    price = apply_discount + (remainder_product_count * product_price)

    return price, skus

def product_multi_deal_loading_factor(skus, product_list, product, product_name, rule):
    number_of_products = skus.count(product_name)
    product_price = product[product_name]
    discount_list = []
    remainder_product_count = 0

    product_discount_data_object = product_list[product_name][rule]

    discount_threshold = product_discount_data_object['discount_threshold']

    while number_of_products > 0:
        prioritise_first_discount = number_of_products % discount_threshold
        
        if prioritise_first_discount == 0:
            product_discount_data_object['count'] += 1
            number_of_products -= discount_threshold
        elif number_of_products > 0 and prioritise_first_discount == discount_threshold:
            product_discount_data_object['count'] += 1
            number_of_products -= discount_threshold
        else:
            number_of_products -= 1

        breakpoint()

    applied_discount = product_discount_data_object['count']

    remainder_product_count += skus.count(product_name) - (applied_discount * discount_threshold) 

    apply_discount = (applied_discount * product_price * discount_threshold) - (applied_discount * 10)

    discount_list.append(apply_discount)

    breakpoint()
    price = 0
    # price = apply_a5_discount + apply_a3_discount + (remainder_product_count * product_price)

    return price, skus

def get_loading_factor(product_name):
    discount_loading_factors = OrderedDict([
        ('A', product_multi_deal_loading_factor),
        ('B', product_b_pricing_factor),
        ('E', product_e_pricing_factor),
        ('F', product_f_pricing_factor),
        ('H', product_h_pricing_factor),
        ('K', product_loading_factor_one_discount),
        
    ])

    return discount_loading_factors[product_name]

def apply_price_loading_factors(skus, product_discount_list, products):
    final_price = 0

    for item in PRODUCT_STOCK_PRICES.keys():
        try:
            discount_loading_factor = get_loading_factor(item)
            for rule in product_discount_list[item].keys():
                breakpoint()
                if item in ['K', 'A']:
                    price, updated_skus = discount_loading_factor(skus, product_discount_list, products, item, rule)
                else:
                    price, updated_skus = discount_loading_factor(skus, product_discount_list, products)
                skus = updated_skus
                final_price += price
        except KeyError:
            product_price = products[item]
            product_quantity = skus.count(item)
            final_price += product_price * product_quantity
    return final_price





