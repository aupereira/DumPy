# FILEPATH: /c:/Users/Aurora/Desktop/dumpy/tests/test_linalg.py

import unittest
from dumpy.linalg.L1 import inner, norm
import math

class TestLinalgL1(unittest.TestCase):
    def test_inner(self):
        # Test that inner returns the correct result for some vectors
        self.assertEqual(inner([1, 2, 3], [4, 5, 6]), 32)
        self.assertEqual(inner([0, 0, 0], [4, 5, 6]), 0)
        self.assertEqual(inner([1, 2, 3], [0, 0, 0]), 0)
        self.assertEqual(inner([-1, -2, -3], [-4, -5, -6]), 32)
        self.assertEqual(inner([1, 2, 3], [3, 2, 1]), 10)

        # Test that inner returns 0 for orthogonal vectors
        self.assertEqual(inner([1, 0], [0, 1]), 0)

        # Test that inner returns the square of the norm for a vector with itself
        self.assertEqual(inner([1, 2, 3], [1, 2, 3]), 14)

    def test_norm(self):
        # Test that norm returns the correct result for some vectors
        self.assertEqual(norm([3, 4]), 5)  # 2-norm
        self.assertEqual(norm([3, 4], 1), 7)  # 1-norm
        self.assertEqual(norm([1, 1, 1, 1], 1), 4)  # 1-norm
        self.assertEqual(norm([1, 2, 3, 4], 2), math.sqrt(30))  # 2-norm
        self.assertEqual(norm([-1, -2, -3, -4], 2), math.sqrt(30))  # 2-norm
        self.assertEqual(norm([1, 0, 0, 0], float('inf')), 1)  # infinity-norm
        self.assertEqual(norm([1, 2, 3, 4], float('inf')), 4)  # infinity-norm

        # Test that norm returns 0 for the zero vector
        self.assertEqual(norm([0, 0, 0, 0]), 0)

        # Test that norm returns the absolute value for a 1D vector
        self.assertEqual(norm([-7]), 7)
        self.assertEqual(norm([7]), 7)