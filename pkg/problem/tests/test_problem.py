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
                Constraint((0, 1),
                           lambda variables: variables[0] != variables[1]),
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

    def test_all_assigned_true(self):
        """
        test the check where all variables have values
        """
        problem = self.defaultConsistentProblem()
        self.assertTrue(problem.all_assigned())

    def test_all_assigned_false(self):
        """
        test the check where all variables have values when not all variables have values
        """
        problem = self.defaultConsistentProblem()
        problem.reset_value(1)
        self.assertFalse(problem.all_assigned())

    def test_set_value(self):
        """
        test set value
        """
        problem = self.defaultConsistentProblem()
        problem.set_value(1, 2)
        self.assertEqual(problem.variables[1].get_value(), 2)

    def test_set_value_out_of_scope(self):
        """
        test set value out of scope
        """
        problem = self.defaultConsistentProblem()
        orig_variables = problem.variables
        problem.set_value(5, 3)
        self.assertEqual(problem.variables, orig_variables)

    def test_reset_value(self):
        """
        test resetting a variable
        """
        problem = self.defaultConsistentProblem()
        problem.reset_value(1)
        self.assertIsNone(problem.variables[1].get_value())

    def test_get_domain(self):
        """
        test getting the domain of a variable
        """
        problem = self.defaultConsistentProblem()
        self.assertEqual(problem.get_domain(1), [0, 1, 2])

    def test_num_variables(self):
        """
        test number of variables
        """
        problem = self.defaultConsistentProblem()
        self.assertEqual(problem.num_variables(), 3)

    def test_will_be_consistent(self):
        """
        test whether a potential assignment will be consistent
        """
        problem = self.defaultConsistentProblem()
        self.assertTrue(problem.will_be_consistent(2, 1))
        self.assertEqual(problem.variables[2].get_value(), 2)
    
    def test_will_be_consistent_false(self):
        """
        test whether a potential assignment will be consistent when it won't be 
        """
        problem = self.defaultConsistentProblem()
        self.assertFalse(problem.will_be_consistent(2, 0))
        self.assertEqual(problem.variables[2].get_value(), 2)

    def test_variable_assignments(self):
        """
        test fetching current tuple of variable assignments
        """
        problem = self.defaultConsistentProblem()
        self.assertEqual(problem.variable_assignments(), (2, 1, 2))

