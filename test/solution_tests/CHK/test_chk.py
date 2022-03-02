import pytest

from solutions.CHK import checkout_solution, InvalidInputException

def test_checkout_solution_sums_without_discount():
    skus = 'A'
    assert checkout_solution.checkout(skus) == 50

def test_checkout_solution_sums_with_discounts():
    skus = 'AAA'
    assert checkout_solution.checkout(skus) == 130

    skus = 'AAAA'
    assert checkout_solution.checkout(skus) == 180

    skus = 'AAAAA'
    assert checkout_solution.checkout(skus) == 230

    skus = 'AAAAAA'
    assert checkout_solution.checkout(skus) == 260

    skus = 'AAABB'
    expected_A_cost = 130
    expected_B_cost= 45
    assert checkout_solution.checkout(skus) == (expected_A_cost + expected_B_cost)

    skus = 'AAAB'
    expected_A_cost = 130
    expected_B_cost= 30
    assert checkout_solution.checkout(skus) == (expected_A_cost + expected_B_cost)

def test_B_product_discounts():
    skus = 'BB'
    assert checkout_solution.checkout(skus) == 45

    skus = 'BBB'
    assert checkout_solution.checkout(skus) == 75

    skus = 'BBBB'
    assert checkout_solution.checkout(skus) == 90

    skus = 'BBBBB'
    assert checkout_solution.checkout(skus) == 120

def test_mixture_products():
    skus = 'AAABBAAA'
    assert checkout_solution.checkout(skus) == 305

    skus = 'AABBCD'
    assert checkout_solution.checkout(skus) == 180

    skus = 'ABCDABCD'
    assert checkout_solution.checkout(skus) == 215

    skus = 'BABDDCAC'
    assert checkout_solution.checkout(skus) == 215

    skus = 'ABCDCBAABCABBAAA'
    assert checkout_solution.checkout(skus) == 505


def test_invalid_input_responds_as_expected():
    skus = 'LLLP'
    assert checkout_solution.checkout(skus) == -1

    skus = '12384'
    assert checkout_solution.checkout(skus) == -1

    skus = 'AzB'
    assert checkout_solution.checkout(skus) == -1











