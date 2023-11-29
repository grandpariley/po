import unittest

from pkg.consts import Constants
from pkg.moead.sort import euclidean_distance_mapping
from pkg.moead.tests.test_util import default_individuals

NUMBER_FEED = iter([7, 4, 7, 5, 2, 9, 3, 8, 9, 2, 5, 6, 7, 5, 3, 2, 8, 2, 9])


class SortTest(unittest.TestCase):

    def test_euclidean_distance_mapping(self):
        Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS = 4
        individuals = default_individuals()
        input_b = []
        for i in range(len(individuals)):
            input_b.append([])
            for _ in range(len(individuals[i].get_objective_values())):
                input_b[i].append(1.00 / next(NUMBER_FEED))

        b = euclidean_distance_mapping(input_b)
        self.assertEqual(
            b,
            [[0, 2, 1, 3], [1, 0, 2, 3], [2, 3, 0, 1], [3, 2, 0, 1]]
        )
