import unittest
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_individuals, sort_by_crowding_distance


def default_other_dominating_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 3)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(3)
    return individual


def default_dominating_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 2)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(2)
    return individual


def default_dominated_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 0)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(0)
    return individual


def default_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 1)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(1)
    return individual


class SortTest(unittest.TestCase):

    def test_sort_individuals(self):
        individuals = [default_individual(), default_individual(), default_other_dominating_individual(),
                       default_dominating_individual(), default_dominated_individual()]
        result = sort_individuals(individuals, 1)
        self.assertEqual(
            [str(default_dominated_individual()), str(default_individual()), str(default_individual()), str(
                default_dominating_individual()), str(
                default_other_dominating_individual())], [str(r) for r in result])

    def test_sort_by_crowding_distance(self):
        individuals = [default_individual(), default_individual(), default_other_dominating_individual(),
                       default_dominating_individual(), default_dominated_individual()]
        result = sort_by_crowding_distance(individuals)
        self.assertEqual(
            [str(default_dominated_individual()), str(default_individual()), str(default_individual()), str(
                default_dominating_individual()), str(
                default_other_dominating_individual())], [str(r) for r in result])
