# tests/test_max_integer.py

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_positive_numbers(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_max_integer_negative_numbers(self):
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)

    def test_max_integer_mixed_numbers(self):
        result = max_integer([1, -3, 5, -2, 4])
        self.assertEqual(result, 5)

    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_single_element_list(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_max_integer_duplicate_values(self):
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()

