import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(StatEngine([1, 2, 3, 4]).get_mean(), 2.5)

    def test_median_even(self):
        self.assertEqual(StatEngine([1, 2, 3, 4]).get_median(), 2.5)

    def test_median_odd(self):
        self.assertEqual(StatEngine([1, 2, 3]).get_median(), 2)

    def test_mode(self):
        self.assertEqual(StatEngine([1, 2, 2, 3]).get_mode(), [2.0])

    def test_no_mode(self):
        self.assertEqual(StatEngine([1, 2, 3]).get_mode(), "No mode (all values are unique)")

    def test_empty(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_std(self):
        engine = StatEngine([2,4,4,4,5,5,7,9])
        self.assertAlmostEqual(engine.get_standard_deviation(False), 2)

if __name__ == "__main__":
    unittest.main()