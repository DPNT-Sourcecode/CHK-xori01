from solutions.CHK import checkout_solution

def test_checkout_solution_sums_without_discount():
    skus = 'A'
    assert checkout_solution.checkout(skus) == 50

def test_checkout_solution_sums_with_discounts():
    skus = 'AAA'
    assert checkout_solution.checkout(skus) == 130

    skus = 'AAAA'
    assert checkout_solution.checkout(skus) == 130

    

