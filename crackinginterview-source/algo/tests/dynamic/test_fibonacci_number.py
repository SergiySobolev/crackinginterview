import unittest

from parameterized import parameterized

from dynamic.tasks.fibonacci_number import FibonacciNumber


class TestFibonacciNumber(unittest.TestCase):

    @parameterized.expand([
        ['1', 0, 0],
        ['1', 1, 1],
        ['2', 2, 1],
        ['3', 3, 2],
        ['4', 4, 3],
        ['5', 5, 5],
        ['6', 6, 8],
        ['7', 7, 13],
        ['8', 8, 21],
        ['9', 9, 34],
        ['10', 10, 55]

    ])
    def test_rod_cut_optimum_down_recursive(self, name, n, expected_value):
        self.assertEqual(FibonacciNumber.calc_fibonacci_number(n), expected_value)
