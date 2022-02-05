import unittest

from pkg.nsga2.crowding_distance import crowding_distance_assignment
from pkg.nsga2.tests.test_util import default_individuals


class CrowdingDistanceTest(unittest.TestCase):
    def test_crowding_distance_assignment(self):
        individuals = default_individuals()
        for individual in individuals:
            self.assertEqual(individual.get_crowding_distance(), 0)
        crowding_distance_assignment(individuals)
        self.assertEqual(individuals[0].get_crowding_distance(), float('inf'))
        self.assertEqual(individuals[1].get_crowding_distance(), 3.3333333333333335)
        self.assertEqual(individuals[2].get_crowding_distance(), float('inf'))
        self.assertEqual(individuals[3].get_crowding_distance(), float('inf'))
