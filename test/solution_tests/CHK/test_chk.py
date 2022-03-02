import pytest

from solutions.CHK import checkout_solution, InvalidInputException

def test_checkout_solution_sums_without_discount():
    skus = 'A'
    assert checkout_solution.checkout(skus) == 50

def test_checkout_solution_sums_with_discounts():
    skus = 'AAA'
    assert checkout_solution.checkout(skus) == 130

    skus = 'AAAA'
    assert checkout_solution.checkout(skus) == 200

    skus = 'AAAAA'
    assert checkout_solution.checkout(skus) == 250

    skus = 'AAABB'
    expected_A_cost = 130
    expected_B_cost= 45
    assert checkout_solution.checkout(skus) == (expected_A_cost + expected_B_cost)

    skus = 'AAAB'
    expected_A_cost = 130
    expected_B_cost= 30
    assert checkout_solution.checkout(skus) == (expected_A_cost + expected_B_cost)

def test_invalid_input_responds_as_expected():
    skus = 'LLLP'
    with pytest.raises(InvalidInputException):
        checkout_solution.checkout(skus)

    skus = '12384'
    with pytest.raises(InvalidInputException):
        checkout_solution.checkout(skus)

    skus = 'AzB'
    with pytest.raises(InvalidInputException):
        checkout_solution.checkout(skus)








