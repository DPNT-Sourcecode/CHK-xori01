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
                desired_chunk_size = clone_product_subset[:max]
                loading_factor = selected_discount_attributes['loading_factor']
                loading_factor.product_subset = desired_chunk_size

                discount_enabled = loading_factor.should_apply_discount(
                    min=min, max=max, skus_full_list=skus_full_list
                )

                if discount_enabled:
                    clone_product_subset = clone_product_subset[:-min]
                    applied_discounts.append({ "amount": selected_discount_attributes['discount'] })
                else:
                    index += 1
            
            clone_product_subset = clone_product_subset[:-len(clone_product_subset)]


        return applied_discounts