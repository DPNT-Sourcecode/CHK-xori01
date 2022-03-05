import pytest

from solutions.CHK import checkout_solution
from solutions.CHK.constants import PRODUCT_STOCK_PRICES

def test_checkout_solution_sums_without_discount():
    skus = 'A'
    assert checkout_solution.checkout(skus) == 50

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
    ('H', PRODUCT_STOCK_PRICES['H']),
    ('H' * 2, PRODUCT_STOCK_PRICES['H'] * 2),
    ('H' * 3, PRODUCT_STOCK_PRICES['H'] * 3),
    ('H' * 4, PRODUCT_STOCK_PRICES['H'] * 4),
    ('H' * 5, (PRODUCT_STOCK_PRICES['H'] * 5) - 5),
    ('H' * 6, (PRODUCT_STOCK_PRICES['H'] * 6) - 5),
    ('H' * 7, (PRODUCT_STOCK_PRICES['H'] * 7) - 5),
    ('H' * 8, (PRODUCT_STOCK_PRICES['H'] * 8) - 5),
    ('H' * 9, (PRODUCT_STOCK_PRICES['H'] * 9) - 5),
    ('H' * 10, (PRODUCT_STOCK_PRICES['H'] * 10) - 20),
    ('H' * 10 + 'AA' + 'B', ((PRODUCT_STOCK_PRICES['H'] * 10) - 20) + (PRODUCT_STOCK_PRICES['A'] * 2) + (PRODUCT_STOCK_PRICES['B'])),
    ('H' * 10 + 'AAA' + 'BB', ((PRODUCT_STOCK_PRICES['H'] * 10) - 20) + ((PRODUCT_STOCK_PRICES['A'] * 3) - 20) + (PRODUCT_STOCK_PRICES['B'] * 2 - 15)),
])
def test_h_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('K', PRODUCT_STOCK_PRICES['K']),
    ('K' * 2, (PRODUCT_STOCK_PRICES['K'] * 2) - 20),
    ('K' * 3, (PRODUCT_STOCK_PRICES['K'] * 3) - 20),
    ('K' * 4, (PRODUCT_STOCK_PRICES['K'] * 4) - 40),
    ('K' * 2 + 'AA' + 'B', (PRODUCT_STOCK_PRICES['K'] * 2) - 20 + 100 + 30),
    ('K' * 4 + 'AAA' + 'BB', (PRODUCT_STOCK_PRICES['K'] * 4) - 40 + 130 + 45),
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
    ('U' * 3, 120),
    ('U' * 4, 120),
    ('U' * 5, 160),
])
def test_u_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('V', 50),
    ('V' * 2, 90),
    ('V' * 3, 130),
    ('V' * 4, 130 + 50),
])
def test_v_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

@pytest.mark.parametrize("skus,expected", [
    ('S', 20),
    ('SS', 40),
    ('SST', 45),
    ('SSX', 45),
    ('SSZ', 45),
    ('SSX', 45),
    ('SSY', 45),
    ('STY', 45),
    ('SXY', 45),
    ('SSZ', 45),
    ('ZZZ', 45),
    ('ZZS', 45),
    ('ZZSZ', 66),
    ('TTSZ', 66),
    ('SXTZ', 66),
    ('SXTZY', 86),
    ('ZSZSZ', 87),
    ('ZSZSZX', 90),
    ('STUVW', 20 + 20 + 40 + 50 + 20),
])
def test_group_discounts(skus, expected):
    assert checkout_solution.checkout(skus) == expected

def test_all_products():
    skus = 'ABCDEFGHIJKLMNOPQRUVWYZ'
    assert checkout_solution.checkout(skus) == 796

    skus_list = [item for item in PRODUCT_STOCK_PRICES.keys()]
    skus = "".join(skus_list)
    assert checkout_solution.checkout(skus) == 796 + 45
    
    skus = 'ABCDEFGHIJKLMNOPQRSTUVW'
    assert checkout_solution.checkout(skus) == 795


def test_invalid_input_responds_as_expected():
    skus = '12384'
    assert checkout_solution.checkout(skus) == -1

    skus = 'AzB'
    assert checkout_solution.checkout(skus) == -1







