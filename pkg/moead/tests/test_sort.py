import unittest

from pkg.moead.sort import euclidean_distance_mapping
from pkg.moead.tests.test_util import default_individuals


class SortTest(unittest.TestCase):

    def test_euclidean_distance_mapping(self):
        individuals = default_individuals()
        b = euclidean_distance_mapping(individuals)
        self.assertEqual(
            b,
            [[1, 2, 3, 0], [1, 3, 0, 2], [2, 0, 1, 3], [3, 2, 1, 0]]
        )
