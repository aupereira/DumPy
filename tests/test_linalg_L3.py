import unittest
from dumpy.linalg.L3 import transpose, identity, matadd, matsub, matmul

class TestLinalg(unittest.TestCase):
    def test_transpose(self):
        # Test that transpose returns the correct result for a 2x2 matrix
        self.assertEqual(transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

        # Test that transpose returns the correct result for a 3x3 matrix
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

        # Test that transpose returns the correct result for a 1x3 matrix
        self.assertEqual(transpose([[1, 2, 3]]), [[1], [2], [3]])

        # Test that transpose returns the correct result for a 3x1 matrix
        self.assertEqual(transpose([[1], [2], [3]]), [[1, 2, 3]])

        # Test that transpose returns the correct result for an empty matrix
        self.assertEqual(transpose([]), [])

    def test_identity(self):
        # Test that identity returns the correct result for n=1
        self.assertEqual(identity(1), [[1]])

        # Test that identity returns the correct result for n=2
        self.assertEqual(identity(2), [[1, 0], [0, 1]])

        # Test that identity returns the correct result for n=3
        self.assertEqual(identity(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        # Test that identity returns the correct result for n=4
        self.assertEqual(identity(4), [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

        # Test that identity returns the correct result for n=0
        self.assertEqual(identity(0), [])

    def test_matadd(self):
        # Test that matadd returns the correct result for two 2x2 matrices
        self.assertEqual(matadd([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]])

        # Test that matadd returns the correct result for two 3x3 matrices
        self.assertEqual(matadd([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]), [[11, 13, 15], [17, 19, 21], [23, 25, 27]])

        # Test that matadd returns the correct result for two 1x3 matrices
        self.assertEqual(matadd([[1, 2, 3]], [[4, 5, 6]]), [[5, 7, 9]])

        # Test that matadd returns the correct result for two 3x1 matrices
        self.assertEqual(matadd([[1], [2], [3]], [[4], [5], [6]]), [[5], [7], [9]])

        # Test that matadd returns the correct result for two empty matrices
        self.assertEqual(matadd([], []), [])

    def test_matsub(self):
        # Test that matsub returns the correct result for two 2x2 matrices
        self.assertEqual(matsub([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[-4, -4], [-4, -4]])

        # Test that matsub returns the correct result for two 3x3 matrices
        self.assertEqual(matsub([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]), [[-9, -9, -9], [-9, -9, -9], [-9, -9, -9]])

        # Test that matsub returns the correct result for two 1x3 matrices
        self.assertEqual(matsub([[1, 2, 3]], [[4, 5, 6]]), [[-3, -3, -3]])

        # Test that matsub returns the correct result for two 3x1 matrices
        self.assertEqual(matsub([[1], [2], [3]], [[4], [5], [6]]), [[-3], [-3], [-3]])

        # Test that matsub returns the correct result for two empty matrices
        self.assertEqual(matsub([], []), [])

    def test_matmul(self):
        # Test that matmul returns the correct result for two 2x2 matrices
        self.assertEqual(matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]])

        # Test that matmul returns the correct result for two 3x3 matrices
        self.assertEqual(matmul([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]), [[84, 90, 96], [201, 216, 231], [318, 342, 366]])

        # Test that matmul returns the correct result for a 1x3 matrix and a 3x1 matrix
        self.assertEqual(matmul([[1, 2, 3]], [[4], [5], [6]]), [[32]])

        # Test that matmul returns the correct result for a 3x1 matrix and a 1x3 matrix
        self.assertEqual(matmul([[1], [2], [3]], [[4, 5, 6]]), [[4, 5, 6], [8, 10, 12], [12, 15, 18]])

        # Test that matmul returns the correct result for two empty matrices
        self.assertEqual(matmul([], []), [])