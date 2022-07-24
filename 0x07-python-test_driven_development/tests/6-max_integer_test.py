#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test max_integer"""
    def test_def(self):
        """test normal input"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        """test empty imput"""
        self.assertEqual(max_integer(), None)

    def test_neg(self):
        """test negative"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_neg_pos(self):
        """test composed input"""
        self.assertEqual(max_integer([1, -4, -5, 5, 3]), 5)

    def test_non_int(self):
        """
        ...
        """
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

    def test_float(self):
        """
        ...
        """
        self.assertEqual(max_integer([1, 2, 3.3]), 3.3)


if __name__ == "__main__":
    unittest.main()
