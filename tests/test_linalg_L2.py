import unittest
from dumpy.linalg.L2 import outer, mvmul

class TestLinalgL2(unittest.TestCase):
    def test_outer(self):
        # Test that outer returns the correct result for some vectors
        self.assertEqual(outer([1, 2, 3], [4, 5, 6]), [[4, 5, 6], [8, 10, 12], [12, 15, 18]])
        self.assertEqual(outer([0, 0, 0], [4, 5, 6]), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(outer([1, 2, 3], [0, 0, 0]), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(outer([-1, -2, -3], [-4, -5, -6]), [[4, 5, 6], [8, 10, 12], [12, 15, 18]])
        self.assertEqual(outer([1, 2, 3], [3, 2, 1]), [[3, 2, 1], [6, 4, 2], [9, 6, 3]])

        # Test that outer raises an error for vectors of different lengths
        with self.assertRaises(ValueError):
            outer([1, 2, 3], [4, 5])

    def test_mvmul(self):
        # Test that mvmul returns the correct result for some matrices and vectors
        self.assertEqual(mvmul([[1, 2, 3], [4, 5, 6]], [1, 2, 3]), [[14], [32]])
        self.assertEqual(mvmul([[1, 2], [3, 4]], [1, 2]), [[5], [11]])
        self.assertEqual(mvmul([[1]], [1]), [[1]])

        # Test that mvmul raises a ValueError when the number of columns in the matrix
        # does not equal the number of rows in the vector
        with self.assertRaises(ValueError):
            mvmul([[1, 2, 3], [4, 5, 6]], [1, 2])
        with self.assertRaises(ValueError):
            mvmul([[1, 2], [3, 4]], [1, 2, 3])
        with self.assertRaises(ValueError):
            mvmul([[1]], [1, 2])

        # Test that mvmul returns the correct result for some vectors and matrices
        self.assertEqual(mvmul([1, 2], [[1, 2], [3, 4]]), [7, 10])
        self.assertEqual(mvmul([1], [[1]]), [1])

        # Test that mvmul raises a ValueError when the number of columns in the vector
        # does not equal the number of rows in the matrix
        with self.assertRaises(ValueError):
            mvmul([1, 2, 3], [[1, 2], [4, 5]])