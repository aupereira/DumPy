import unittest
from dumpy.trig.trig import taylor_sin
import math

class TestTrig(unittest.TestCase):
    def test_taylor_sin(self):
        # Test that taylor_sin returns the correct result for some values of theta
        self.assertAlmostEqual(taylor_sin(0), 0)
        self.assertAlmostEqual(taylor_sin(math.pi/2), 1)
        self.assertAlmostEqual(taylor_sin(math.pi), 0)
        self.assertAlmostEqual(taylor_sin(3*math.pi/2), -1)
        self.assertAlmostEqual(taylor_sin(2*math.pi), 0)

        # Test that taylor_sin returns the same result as math.sin for some values of theta
        self.assertAlmostEqual(taylor_sin(math.pi/4), math.sin(math.pi/4))
        self.assertAlmostEqual(taylor_sin(math.pi/3), math.sin(math.pi/3))
        self.assertAlmostEqual(taylor_sin(math.pi/6), math.sin(math.pi/6))