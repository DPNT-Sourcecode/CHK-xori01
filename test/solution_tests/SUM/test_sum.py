import pytest

from solutions.SUM import sum_solution, OutOfRangeException, NegativeValuesException


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(50, 50) == 100
        assert sum_solution.compute(100, 100) == 200

    def test_should_not_accept_negative_numbers():
        with pytest.raises(NegativeValuesException):
            sum_solution.compute(-1, 2)

    def test_should_not_accept_out_of_range_input():
        with pytest.raises(OutOfRangeException):
            sum_solution.compute(200, 300)

    def test_should_not_allow_non_ints():
        with pytest.raises()


