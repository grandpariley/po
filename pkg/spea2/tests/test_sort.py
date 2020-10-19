import unittest
from pkg.spea2.sort import sort_population_by_domination
from pkg.spea2.individual import Individual
from pkg.problem.tests.default_problems import default_consistent_problem_set_values
from pkg.spea2.tests.test_spea2 import default_population


def default_individual():
    return Individual(default_consistent_problem_set_values())


class SortTest(unittest.TestCase):

    def test_sort_population_by_domination(self):
        population = default_population()
        formatted_population = [[i.problem.get_value(j) for j in range(i.problem.num_variables())] for i in population]
        sorted_population = sort_population_by_domination(population)
        sorted_formatted_population = [[i.problem.get_value(j) for j in range(i.problem.num_variables())] for i in
                                       sorted_population]
        self.assertEqual(formatted_population[::-1], sorted_formatted_population)
