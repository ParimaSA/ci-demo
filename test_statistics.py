"""Provides module using for test statistics function."""
from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt


class StatisticsTest(TestCase):
    """Provides test for statistics function."""

    def test_variance_typical_values(self):
        """Variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """Variance should work with decimal values."""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_variance_with_empty_list(self):
        """Variance with empty list must raise an error."""
        with self.assertRaises(ValueError):
            variance([])

    def test_stdev(self):
        """Standard variation should work."""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_average(self):
        """Average should work."""
        # average of the single value should be that value
        self.assertEqual(12.0, average([12.0]))
        # simple test
        self.assertEqual(4.0, average([3, 5]))
        # variance([1, 1, 2 , 12, 45]) is 12.2
        self.assertEqual(12.2, average([1, 1, 2, 12, 45]))

    def test_average_with_empty_list(self):
        """Average with empty list must raise an error."""
        with self.assertRaises(ValueError):
            average([])
