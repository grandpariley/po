import unittest
from pkg.spea2.sort import sort_population_by_domination
from pkg.spea2.individual import Individual
from pkg.problem.tests.default_problems import default_consistent_problem_set_values


class SortTest(unittest.TestCase):
    def default_individual(self):
        return Individual(default_consistent_problem_set_values())

    def test_sort_population_by_domination(self):
        population = [None for _ in range(5)]
        for i in range(5):
            population[i] = self.default_individual()
            population[i].problem.set_value(0, i)
            population[i].problem.set_value(1, i + 1)
            population[i].problem.set_value(2, i + 1)
        formatted_population = [[i.problem.get_value(j) for j in range(i.problem.num_variables())] for i in population]
        sorted_population = sort_population_by_domination(population)
        sorted_formatted_population = [[i.problem.get_value(j) for j in range(i.problem.num_variables())] for i in sorted_population]
        self.assertEqual(formatted_population[::-1], sorted_formatted_population)
