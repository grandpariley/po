import unittest
from pkg.problem.constraint import Constraint
from pkg.problem.problem import Problem 
from pkg.problem.variable import Variable
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_individuals, sort_by_crowding_distance

class SortTest(unittest.TestCase):
    def defaultVariables(self):
        return [
            Variable([0, 1, 2, 3]),
            Variable([0, 1, 2, 3]),
            Variable([0, 1, 2, 3]),
        ]

    def defaultConsistentProblem(self):
        variables = self.defaultVariables()
        return Problem(
            variables,
            [
                Constraint((0, 2),
                           lambda variables: variables[0] == variables[1]),
                Constraint(tuple([2]), lambda variables: variables[0] > 0)
            ], [lambda v: tuple(u.get_value() for u in v)])

    def defaultIndividual(self):
        problem = self.defaultConsistentProblem()
        problem.set_value(0, 1)
        problem.set_value(1, 1)
        problem.set_value(2, 1)
        individual = Individual(problem)
        individual.set_crowding_distance(1)
        return individual
    
    def defaultDominatedIndividual(self):
        problem = self.defaultConsistentProblem()
        problem.set_value(0, 1)
        problem.set_value(1, 0)
        problem.set_value(2, 1)
        individual = Individual(problem)
        individual.set_crowding_distance(0)
        return individual
    def defaultDominatingIndividual(self):
        problem = self.defaultConsistentProblem()
        problem.set_value(0, 1)
        problem.set_value(1, 2)
        problem.set_value(2, 1)
        individual = Individual(problem)
        individual.set_crowding_distance(2)
        return individual
    def defaultOtherDominatingIndividual(self):
        problem = self.defaultConsistentProblem()
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