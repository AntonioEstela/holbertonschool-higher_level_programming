#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_integer(unittest.TestCase):
    """Class to tests the function Max_integer
    """

    def test_max_integer(self):
        """Method to test thw function max_integer with unittest"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -30]), 3)
        self.assertEqual(max_integer([2**2, 40, (10 * 3) + 12, 5]), 42)
        self.assertEqual(max_integer([-5645645 ** 56474, -434575867552,
                                      -2345647, -30]), -30)
        self.assertEqual(max_integer([5645645 ** 56474, 434575867552,
                                      2345647, 30]), 5645645 ** 56474)
        self.assertEqual(max_integer([6**77, (345**3) / 10, 234 * 353]), 6**77)
        self.assertIsInstance(max_integer([1, 2, 3, 4]), int)
        self.assertIsNone(max_integer([]))
        self.assertNotIsInstance(max_integer([]), int)
        self.assertIsInstance(max_integer([23, 34, 54]), int)
        self.assertEqual(max_integer([8]), 8)
