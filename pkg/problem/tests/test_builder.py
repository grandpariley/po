import unittest
from pkg.problem.problem import Problem
from pkg.problem.constraint import Constraint
from pkg.problem.variable import Variable
from pkg.problem.builder import defaultPortfolioOptimizationProblem
from pkg.problem.builder import generateManyRandomSolutions

class BuilderTest(unittest.TestCase):
    def defaultVariables(self):
        return [
            Variable([0, 1, 2]),
            Variable([0, 1, 2]),
            Variable([0, 1, 2]),
        ]

    def defaultConsistentProblem(self):
        variables = self.defaultVariables()
        variables[0].set_value(2)
        variables[1].set_value(1)
        variables[2].set_value(2)
        return Problem(
            variables,
            [
                Constraint((0, 1),
                           lambda variables: variables[0] != variables[1]),
                Constraint(tuple([1]), lambda variables: variables[0] > 0),
                Constraint(tuple([2]), lambda variables: variables[0] < 2)
            ], None)

    def test_build(self):
        defaultPortfolioOptimizationProblem()

    def test_generate_many_random_solutions(self):
        problem = self.defaultConsistentProblem()
        individuals = generateManyRandomSolutions(problem, 2)
        print([str(i) for i in individuals])
        self.assertIsNotNone(individuals)
        self.assertEqual(len(individuals), 2)