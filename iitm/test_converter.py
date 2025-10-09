import unittest
from converter import km_to_miles

class TestConverter(unittest.TestCase):
    def test_km_to_miles(self):
        self.assertAlmostEqual(km_to_miles(10), 6.21371)
        self.assertAlmostEqual(km_to_miles(0), 0)
        self.assertAlmostEqual(km_to_miles(1), 0.621371)

if __name__ == '__main__':
    unittest.main()
