import unittest

from pkg.nsga2.tests.test_util import default_individuals, default_individual, default_other_dominating_individual, \
    default_dominating_individual, default_dominated_individual
from pkg.nsga2.sort import sort_individuals, sort_by_crowding_distance, fast_non_dominated_sort


class SortTest(unittest.TestCase):

    def test_fast_non_dominating_sort(self):
        individuals = default_individuals()
        fast_non_dominated_sort(individuals)
        self.assertEqual(
            [i for i in range(len(individuals) - 1, -1, -1)],
            [individuals[i].get_domination_count() for i in range(len(individuals))]
        )

    def test_sort_individuals(self):
        individuals = [default_individual(), default_individual(), default_other_dominating_individual(),
                       default_dominating_individual(), default_dominated_individual()]
        result = sort_individuals(individuals, 1)
        self.assertEqual(
            [str(default_dominated_individual()), str(default_individual()), str(default_individual()), str(
                default_dominating_individual()), str(
                default_other_dominating_individual())], [str(r) for r in result])

    def test_sort_by_crowding_distance(self):
        individuals = [default_other_dominating_individual(),
                       default_dominating_individual(), default_dominated_individual()]
        result = sort_by_crowding_distance(individuals)
        self.assertEqual(
            [str(default_dominated_individual()), str(
                default_dominating_individual()), str(
                default_other_dominating_individual())], [str(r) for r in result])
