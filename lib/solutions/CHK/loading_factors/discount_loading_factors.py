class ProductDiscountFactor:

    product_subset = []

    def __init__(self, cross_product_name=None):
        self.cross_product_name = cross_product_name

    def should_apply_discount(self, min, max, **kwargs):
        return bool(len(self.product_subset) >= min and len(self.product_subset) <= max)


class CrossProductDiscountFactor:

    product_subset = []

    def __init__(self, cross_product_name):
        self.cross_product_name = cross_product_name

    def should_apply_discount(
        self,
        min,
        max,
        skus_full_list,
    ):
        breakpoint()
        return bool(
            len(self.product_subset) >= min
            and len(self.product_subset) <= max
            and any(self.cross_product_name in word for word in skus_full_list) and "".join(skus_full_list).count(self.cross_product_name) % 2 == 0
        )




