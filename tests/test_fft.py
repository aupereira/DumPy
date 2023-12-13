import unittest
from dumpy.fft.fft import fft

class TestFFT(unittest.TestCase):
    def test_fft_single_element(self):
        # Test that fft returns the same value for single element list
        self.assertEqual(fft([1]), [1])
        self.assertEqual(fft([0]), [0])
        self.assertEqual(fft([-1]), [-1])

    def test_fft_two_elements(self):
        # Test that fft returns the correct result for two element list
        self.assertEqual(fft([1, 0]), [1, 1])
        self.assertEqual(fft([0, 1]), [1, -1])
        self.assertEqual(fft([-1, 1]), [0, -2])

    def test_fft_complex_elements(self):
        # Test that fft returns the correct result for complex numbers
        self.assertEqual(fft([1j, 1]), [1+1j, 1j-1])
        self.assertEqual(fft([1+1j, 1]), [2+1j, 1j])

    def test_fft_multiple_elements(self):
        # Test that fft returns the correct result for multiple elements
        self.assertEqual(fft([0, 1, 3, 4]), [8, -3+3j, -2, -3-3j])

    def test_fft_empty_list(self):
        # Test that fft returns an empty list when input is an empty list
        self.assertEqual(fft([]), [])

if __name__ == '__main__':
    unittest.main()