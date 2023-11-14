import unittest
from dumpy.matrix import randmat, matmul

class TestMatrix(unittest.TestCase):
    def test_randmat(self):
        # Test that randmat returns a matrix of the correct size
        m = randmat(3, 4)
        self.assertEqual(m.shape, (3, 4))

        # Test that randmat returns a matrix with values in the correct range
        m = randmat(2, 2, 0, 1)
        self.assertTrue((m >= 0).all() and (m <= 1).all())

    def test_matmul(self):
        # Test that matmul returns the correct result for a simple case
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matmul(A, B), expected)

        # Test that matmul returns the same result for single and multithreaded
        A = randmat(100, 100)
        B = randmat(100, 100)
        self.assertEqual(matmul(A, B, mt=False), matmul(A, B, mt=True))