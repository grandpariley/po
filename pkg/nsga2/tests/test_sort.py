import unittest
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_individuals, sort_by_crowding_distance

class SortTest(unittest.TestCase):
    def defaultIndividual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 1)
        problem.set_value(2, 1)
        individual = Individual(problem)
        individual.set_crowding_distance(1)
        return individual
    
    def defaultDominatedIndividual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 0)
        problem.set_value(2, 1)
        individual = Individual(problem)
        individual.set_crowding_distance(0)
        return individual
    def defaultDominatingIndividual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 2)
        problem.set_value(2, 1)
        individual = Individual(problem)
        individual.set_crowding_distance(2)
        return individual
    def defaultOtherDominatingIndividual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 3)
        problem.set_value(2, 1)
        individual = Individual(problem)
        individual.set_crowding_distance(3)
        return individual

    def test_sort_individuals(self):
        individuals = [self.defaultIndividual(), self.defaultOtherDominatingIndividual(), self.defaultDominatingIndividual(), self.defaultDominatedIndividual()]
        result = sort_individuals(individuals, 1)
        self.assertEqual([self.defaultDominatedIndividual(), self.defaultIndividual(), self.defaultDominatingIndividual(), self.defaultOtherDominatingIndividual()], result)
    
    def test_sort_by_crowding_distance(self):
        individuals = [self.defaultIndividual(), self.defaultOtherDominatingIndividual(), self.defaultDominatingIndividual(), self.defaultDominatedIndividual()]
        result = sort_by_crowding_distance(individuals)
        self.assertEqual([self.defaultDominatedIndividual(), self.defaultIndividual(), self.defaultDominatingIndividual(), self.defaultOtherDominatingIndividual()], result)