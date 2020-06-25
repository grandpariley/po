import unittest
from pkg.problem.problem import Problem
from pkg.problem.constraint import Constraint
from pkg.problem.variable import Variable


class ProblemTest(unittest.TestCase):
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
                Constraint((0, 2),
                           lambda variables: variables[0] == variables[1]),
                Constraint(tuple([1]), lambda variables: variables[0] == 1),
                Constraint(tuple([2]), lambda variables: variables[0] > 0)
            ], None)

    def defaultInconsistentProblem(self):
        variables = self.defaultVariables()
        return Problem(
            variables,
            [
                Constraint((0, 2),
                           lambda variables: False),
            ], None)

    def defaultMultiObjectiveProblem(self):
        variables = self.defaultVariables()
        variables[0].set_value(2)
        variables[1].set_value(1)
        variables[2].set_value(2)
        return Problem(
            variables,
            [
                Constraint((0, 2),
                           lambda variables: variables[0] == variables[1]),
                Constraint(tuple([1]), lambda variables: variables[0] == 1),
                Constraint(tuple([2]), lambda variables: variables[0] > 0)
            ], [lambda variables: sum([var.get_value() for var in variables]), lambda variables: -sum(var.get_value() for var in variables)])

    def test_consistent(self):
        """
        test consistent
        """
        problem = self.defaultConsistentProblem()
        self.assertTrue(problem.consistent())

    def test_inconsistent(self):
        """
        test inconsistent
        """
        problem = self.defaultInconsistentProblem()
        self.assertFalse(problem.consistent())

    def test_objective_values(self):
        """
        test getting objective function values
        """
        problem = self.defaultMultiObjectiveProblem()
        objVals = problem.objective_values()
        self.assertEqual(objVals, (5, -5))
    
    def test_objective_values_empty(self):
        """
        test getting objective function values when no objectives
        """
        problem = self.defaultConsistentProblem()
        self.assertIsNone(problem.objective_values())




