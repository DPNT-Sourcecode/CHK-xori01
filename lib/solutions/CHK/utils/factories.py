from copy import deepcopy

class ProductDiscountFactorFactory:

    def __init__(self, discounts_to_apply=[]):
        self.discounts_to_apply = discounts_to_apply

    def build(self, product_subset, skus_full_list):
        clone_product_subset = deepcopy(product_subset)
        applied_discounts = []
        index = 0

        while len(clone_product_subset) > 0:
            
        pass