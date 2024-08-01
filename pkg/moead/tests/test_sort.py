import unittest

from pkg.consts import Constants
from pkg.moead.sort import euclidean_distance_mapping
from pkg.moead.tests.test_util import default_individuals


class SortTest(unittest.TestCase):

    def test_euclidean_distance_mapping(self):
        Constants.MOEAD_NUM_WEIGHT_VECTORS_T = 4
        b = euclidean_distance_mapping(default_individuals())
        self.assertEqual(
            b,
            [[0, 1, 2, 3], [1, 0, 2, 3], [2, 1, 3, 0], [3, 2, 1, 0]]
        )
