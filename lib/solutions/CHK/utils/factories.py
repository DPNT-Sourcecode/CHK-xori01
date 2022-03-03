from copy import deepcopy

from ..checkout_solution import DISCOUNT_LIST

class ProductDiscountFactorFactory:

    def __init__(self, discounts_to_apply=[]):
        self.discounts_to_apply = discounts_to_apply

    def build(self, product_subset, skus_full_list):
        clone_product_subset = deepcopy(product_subset)
        applied_discounts = []
        index = 0

        while len(clone_product_subset) > 0:
            # Keep trying the same discount until we can't apply it anymore
            while index != len(self.discounts_to_apply):
                discount = self.discounts_to_apply[index]
                selected_discount_attributes = DISCOUNT_LIST[discount]
                min = selected_discount_attributes['rules']['min']
                max = selected_discount_attributes['rules']['max']
                desired_chunk_size = 
                loading_factor = selected_discount_attributes['loading_factor']

        pass