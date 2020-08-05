import unittest
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_individuals, sort_by_crowding_distance


class SortTest(unittest.TestCase):
    def default_individual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 1)
        problem.set_value(2, 1)
        individual = Individual(problem=problem)
        individual.set_crowding_distance(1)
        return individual

    def default_dominated_individual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 0)
        problem.set_value(2, 1)
        individual = Individual(problem=problem)
        individual.set_crowding_distance(0)
        return individual

    def default_dominating_individual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 2)
        problem.set_value(2, 1)
        individual = Individual(problem=problem)
        individual.set_crowding_distance(2)
        return individual

    def default_other_dominating_individual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 3)
        problem.set_value(2, 1)
        individual = Individual(problem=problem)
        individual.set_crowding_distance(3)
        return individual

    def test_sort_individuals(self):
        individuals = [self.default_individual(), self.default_individual(), self.default_other_dominating_individual(), self.default_dominating_individual(), self.default_dominated_individual()]
        result = sort_individuals(individuals, 1)
        self.assertEqual([str(self.default_dominated_individual()), str(self.default_individual()), str(self.default_individual()), str(self.default_dominating_individual()), str(self.default_other_dominating_individual())], [str(r) for r in result])

    def test_sort_by_crowding_distance(self):
        individuals = [self.default_individual(), self.default_individual(), self.default_other_dominating_individual(), self.default_dominating_individual(), self.default_dominated_individual()]
        result = sort_by_crowding_distance(individuals)
        self.assertEqual([str(self.default_dominated_individual()), str(self.default_individual()), str(self.default_individual()), str(self.default_dominating_individual()), str(self.default_other_dominating_individual())], [str(r) for r in result])
