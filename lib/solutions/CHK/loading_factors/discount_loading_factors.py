from typing import Dict, Tuple

from collections import OrderedDict
from math import remainder
from unittest import skipUnless

from ..constants import PRODUCT_STOCK_PRICES

def cross_product_loading_factor(skus: str, product_list: Dict[str, object], product: Dict[str, int], product_name: str, rules: list) -> Tuple[str, str]:
    """
    Cross product loading factor for calculating discounts across products

    Parameters
    ----------
    skus: str
        String containing indiviudal product skus
    
    product_list: Dict[str, object]
        Product discount list used for applying discounts

    product: Dict[str, int]
        Product list used for returning the current products price

    product_name: str
        The name of the product

    rules: List
        List of discount rules names to apply

    Returns
    -------

    price: int
        Calculated price

    skus: str
        Updated skus list

    """
    number_of_products = skus.count(product_name)
    product_price = product[product_name]
    product_discount_data_object = product_list[product_name][rules[0]]
    cross_product_name = product_discount_data_object['cross_product_name']
    cross_product_count = skus.count(cross_product_name)


    discount_threshold = product_discount_data_object['discount_threshold']

    while number_of_products > 0:
        if number_of_products > 0 and number_of_products % discount_threshold == 0:
            if cross_product_count > 0:
                skus = skus.replace(cross_product_name, '', 1)
            
            product_discount_data_object['count'] += 1
            number_of_products -= discount_threshold
        else:
            number_of_products -= 1

    
    applied_discount_count = product_discount_data_object['count']

    remainder_product_count = skus.count(product_name) - (applied_discount_count * discount_threshold) 

    apply_b2_discount = (applied_discount_count * product_price * discount_threshold)

    price = apply_b2_discount + (remainder_product_count * product_price)

    return price, skus

def product_loading_factor_single_discount(skus: str, product_list: Dict[str, object], product: Dict[str, int], product_name: str, rules: list) -> Tuple[str, str]:
    """
    Single product loading factor for calculating discounts with one rule

    Parameters
    ----------
    skus: str
        String containing indiviudal product skus
    
    product_list: Dict[str, object]
        Product discount list used for applying discounts

    product: Dict[str, int]
        Product list used for returning the current products price

    product_name: str
        The name of the product

    rules: List
        List of discount rules names to apply

    Returns
    -------

    price: int
        Calculated price

    skus: str
        Updated skus list

    """
    number_of_products = skus.count(product_name)
    product_price = product[product_name]
    product_discount_data_object = product_list[product_name][rules[0]]

    discount_threshold = product_discount_data_object['discount_threshold']

    while number_of_products > 0:
        if number_of_products > 0 and number_of_products % discount_threshold == 0:
            product_discount_data_object['count'] += 1
            number_of_products -= discount_threshold
        else:
            number_of_products -= 1
    
    applied_discount = product_discount_data_object['count']

    remainder_product_count = skus.count(product_name) - (applied_discount * discount_threshold)
    discount_to_apply = product_discount_data_object['discount']
    apply_discount = (applied_discount * product_price * discount_threshold) - (applied_discount * discount_to_apply)

    price = apply_discount + (remainder_product_count * product_price)

    return price, skus

def product_loading_factor_multiple_discount(skus: str, product_list: Dict[str, object], product: Dict[str, int], product_name: str, rules: list) -> Tuple[str, str]:
    """
    Multiple product loading factor for calculating discounts with two rule

    Parameters
    ----------
    skus: str
        String containing indiviudal product skus
    
    product_list: Dict[str, object]
        Product discount list used for applying discounts

    product: Dict[str, int]
        Product list used for returning the current products price

    product_name: str
        The name of the product

    rules: List
        List of discount rules names to apply

    Returns
    -------

    price: int
        Calculated price

    skus: str
        Updated skus list

    """
    number_of_products = skus.count(product_name)
    product_price = product[product_name]
    product_discount_data_object_a = product_list[product_name][rules[0]]
    product_discount_data_object_b = product_list[product_name][rules[1]]
    
    discount_threshold_a = product_discount_data_object_a['discount_threshold']
    discount_threshold_b = product_discount_data_object_b['discount_threshold']

    while number_of_products > 0:
        prioritise_first_rule = number_of_products % discount_threshold_a
        
        if prioritise_first_rule == 0:
            product_discount_data_object_a['count'] += 1
            number_of_products -= discount_threshold_a
        elif number_of_products > 0 and prioritise_first_rule == discount_threshold_b:
            product_discount_data_object_b['count'] += 1
            number_of_products -= discount_threshold_b
        else:
            number_of_products -= 1

    
    discount_rule_a_count = product_discount_data_object_a['count']
    discount_rule_b_count = product_discount_data_object_b['count']

    remainder_product_count = skus.count(product_name) - (discount_rule_a_count * discount_threshold_a + discount_rule_b_count * discount_threshold_b) 

    discount_to_apply_a = product_discount_data_object_a['discount']
    discount_to_apply_b = product_discount_data_object_b['discount']

    apply_a_discount = (discount_rule_a_count * product_price * discount_threshold_a) - (discount_rule_a_count * discount_to_apply_a)
    apply_b_discount = (discount_rule_b_count * product_price * discount_threshold_b) - (discount_rule_b_count * discount_to_apply_b)

    price = apply_a_discount + apply_b_discount + (remainder_product_count * product_price)

    return price, skus

def group_discount_loading_factor(skus: str, product_list: Dict[str, object], product: Dict[str, int], product_name: str, rules: list) -> Tuple[str, str]:
    """
    Group product loading factor for calculating discounts that have shared group discounts

    Parameters
    ----------
    skus: str
        String containing indiviudal product skus
    
    product_list: Dict[str, object]
        Product discount list used for applying discounts

    product: Dict[str, int]
        Product list used for returning the current products price

    product_name: str
        The name of the product

    rules: List
        List of discount rules names to apply

    Returns
    -------

    price: int
        Calculated price

    skus: str
        Updated skus list

    """

    matched_list = [characters in ['S','T','X','Y','Z'] for characters in skus]
    if not any(matched_list):
        return 0, skus

    product_price = product[product_name]
    product_discount_data_object = product_list[product_name][rules[0]]

    group_discount_list = product_discount_data_object['discount_group']
    discount_threshold = product_discount_data_object['discount_threshold']

    product_count = 0
    groups = []

    for group in group_discount_list:
        group_match_count = skus.count(group)
        product_count += group_match_count
        if group_match_count > 0: groups.append(group * group_match_count)
    while product_count > 0:
        if product_count > 0 and product_count % discount_threshold == 0:
            product_discount_data_object['count'] += 1
            product_count -= discount_threshold
        else:
            product_count -= 1
        
    applied_discount = product_discount_data_object['count']

    for group in group_discount_list:
        product_count += skus.count(group)

    remainder_product_count = product_count - (applied_discount * discount_threshold)
    discount_to_apply = product_discount_data_object['discount']
    apply_discount = (applied_discount * product_price * discount_threshold) - (applied_discount * discount_to_apply)

    group_skus = "".join(groups)
    clone_group_skus = group_skus
    divisible = len(group_skus[0:3]) / 3


    while divisible.is_integer():
        if len(clone_group_skus) < 3:
            break
        clone_group_skus = clone_group_skus[int(3 * divisible):]

    remainder_cost = 0

    if len(group_skus) > 0:
        for _ in range(remainder_product_count):
            remaining_product_name = clone_group_skus[0]
            remainder_cost += (1 * product[remaining_product_name])
            clone_group_skus = clone_group_skus[1:]
    result = ''
    for sku in skus:
        if sku in group_skus:
            result += ''
        else:
            result += sku

    skus = result
    price = apply_discount + remainder_cost
    return price, skus

def get_loading_factor(product_name: str) -> function:
    """
    Helper method for returning loading factors against product

    Parameters
    ----------

    product_name: str

    Returns
    -------

    discount_loading_factor: function
    """
    discount_loading_factors = OrderedDict([
        ('A', product_loading_factor_multiple_discount),
        ('B', product_loading_factor_single_discount),
        ('E', cross_product_loading_factor),
        ('F', cross_product_loading_factor),
        ('H', product_loading_factor_multiple_discount),
        ('K', product_loading_factor_single_discount),
        ('N', cross_product_loading_factor),
        ('P', product_loading_factor_single_discount),
        ('Q', product_loading_factor_single_discount),
        ('R', cross_product_loading_factor),
        ('U', cross_product_loading_factor),
        ('V', product_loading_factor_multiple_discount),
        ('S', group_discount_loading_factor),
        ('T', group_discount_loading_factor),
        ('X', group_discount_loading_factor),
        ('Y', group_discount_loading_factor),
        ('Z', group_discount_loading_factor),
    ])

    return discount_loading_factors[product_name]

def apply_price_loading_factors(skus: str, product_discount_list: Dict[str, object], product: Dict[str, int]):
    final_price = 0

    for item in PRODUCT_STOCK_PRICES.keys():
        try:
            discount_loading_factor = get_loading_factor(item)
            rules = list(product_discount_list[item].keys())
            price, updated_skus = discount_loading_factor(skus, product_discount_list, product, item, rules)
            skus = updated_skus
            final_price += price
        except KeyError:
            product_price = products[item]
            product_quantity = skus.count(item)
            final_price += product_price * product_quantity

    return final_price
