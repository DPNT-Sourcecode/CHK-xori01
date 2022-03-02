import pytest

from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_should_not_accept_negative_numbers():
        with pytest.raises(Exception):
            sum_solution.compute(-1, 2)

    def test_should_not_accept_out_of_range_input():
        with py

