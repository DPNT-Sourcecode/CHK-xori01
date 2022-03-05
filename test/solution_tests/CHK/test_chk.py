import pytest

from solutions.CHK import checkout_solution, InvalidInputException

# def test_checkout_solution_sums_without_discount():
#     skus = 'A'
#     assert checkout_solution.checkout(skus) == 50

def test_checkout_solution_sums_with_discounts():
    skus = 'AA'
    assert checkout_solution.checkout(skus) == 100

    skus = 'AAA'
    assert checkout_solution.checkout(skus) == 130

    skus = 'AAAA'
    assert checkout_solution.checkout(skus) == 180

    skus = 'AAAAA'
    assert checkout_solution.checkout(skus) == 200

    skus = 'AAAAAA'
    assert checkout_solution.checkout(skus) == 250

    skus = 'AAAAAAA' # 7
    assert checkout_solution.checkout(skus) == 300


    skus = 'AAAAAAAA' # 8
    assert checkout_solution.checkout(skus) == 330

    skus = 'AAAAAAAAA' # 9
    assert checkout_solution.checkout(skus) == 380

    skus = 'AAAAAAAAAA' # 10
    assert checkout_solution.checkout(skus) == 400

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
    assert checkout_solution.checkout(skus) == 295

    skus = 'AABBCD'
    assert checkout_solution.checkout(skus) == 180

    skus = 'ABCDABCD'
    assert checkout_solution.checkout(skus) == 215

    skus = 'BABDDCAC'
    assert checkout_solution.checkout(skus) == 215

    skus = 'ABCDCBAABCABBAAA'
    assert checkout_solution.checkout(skus) == 495

def test_E_product_discounts():
    skus = 'E'
    assert checkout_solution.checkout(skus) == 40

    skus = 'EE'
    assert checkout_solution.checkout(skus) == 80

    skus = 'EEB'
    assert checkout_solution.checkout(skus) == 80

    skus = 'EEEEBB'
    assert checkout_solution.checkout(skus) == 160
    
    skus = 'AAAAAEEBAAABB'
    assert checkout_solution.checkout(skus) == 455

def test_F_product_discounts():
    skus = 'F'
    assert checkout_solution.checkout(skus) == 10

    skus = 'FF'
    assert checkout_solution.checkout(skus) == 20

    skus = 'FFF'
    assert checkout_solution.checkout(skus) == 20

    skus = 'AAFFFBB'
    assert checkout_solution.checkout(skus) == 165

    skus = 'AAAFFFBB'
    expected = 130 + 20 + 45
    assert checkout_solution.checkout(skus) == expected

    skus = 'AAAFFFFBB'
    expected = 130 + 30 + 45
    assert checkout_solution.checkout(skus) == expected

    skus = 'AAAFFFFFFBB'
    expected = 130 + 40 + 45
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('H', 10),
    ('H' * 2, 20),
    ('H' * 3, 30),
    ('H' * 4, 40),
    ('H' * 5, 45),
    ('H' * 6, 55),
    ('H' * 7, 65),
    ('H' * 8, 75),
    ('H' * 9, 85),
    ('H' * 10, 80),
    ('H' * 10 + 'AA' + 'B', 80 + 100 + 30),
    ('H' * 10 + 'AAA' + 'BB', 80 + 130 + 45),
])
def test_h_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('K', 80),
    ('K' * 2, 150),
    ('K' * 3, 150 + 80),
    ('K' * 4, 300),
    ('K' * 5, 300 + 80),
    ('K' * 6, 450),
    ('K' * 7, 450 + 80),
    ('K' * 8, 600),
    ('K' * 2 + 'AA' + 'B', 150 + 100 + 30),
    ('K' * 4 + 'AAA' + 'BB', 300 + 130 + 45),
])
def test_k_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('N', 40),
    ('N' * 2, 80),
    ('N' * 3, 120),
    ('N' * 3 + 'M', 120),
    ('N' * 3 + 'MM', 135),
    ('N' * 6 + 'MM', 240),
    ('N' * 6 + 'MM' + 'AAA', 240 + 130),
])
def test_n_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('P', 50),
    ('P' * 2, 100),
    ('P' * 3, 150),
    ('P' * 4, 200),
    ('P' * 5, 200),
    ('P' * 6, 250),
    ('P' * 10, 400),
])
def test_p_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('Q', 30),
    ('Q' * 2, 60),
    ('Q' * 3, 80),
    ('Q' * 4, 110),
    ('Q' * 5, 140),
    ('Q' * 6, 160),
])
def test_q_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('RQ', 80),
    ('R' * 2 + 'Q', 130),
    ('R' * 3 + 'Q', 150),
    ('R' * 4 + 'Q', 200),
    ('R' * 6 + 'QQ', 300),
])
def test_r_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('U', 40),
    ('U' * 2, 80),
    ('U' * 3, 80),
    ('U' * 4, 120),
    ('U' * 5, 160),
    ('U' * 6, 160),
])
def test_u_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('V', 50),
    ('V' * 2, 80),
])
def test_v_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

def test_invalid_input_responds_as_expected():
    skus = '12384'
    assert checkout_solution.checkout(skus) == -1

    skus = 'AzB'
    assert checkout_solution.checkout(skus) == -1







