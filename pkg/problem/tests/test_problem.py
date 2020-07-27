import unittest
from pkg.problem.tests.default_problems import default_consistent_problem_set_values, default_consistent_problem, default_inconsistent_problem_set_values, default_multi_objective_problem_set_values


class ProblemTest(unittest.TestCase):
    def test_consistent(self):
        problem = default_consistent_problem_set_values()
        self.assertTrue(problem.consistent())

    def test_inconsistent(self):
        problem = default_inconsistent_problem_set_values()
        self.assertFalse(problem.consistent())

    def test_objective_values(self):
        problem = default_multi_objective_problem_set_values()
        objVals = problem.objective_values()
        self.assertEqual(objVals, (5, -5))

    def test_objective_values_empty(self):
        problem = default_consistent_problem()
        problem.objectiveFuncs = None
        self.assertIsNone(problem.objective_values())

    def test_all_assigned_true(self):
        problem = default_consistent_problem_set_values()
        self.assertTrue(problem.all_assigned())

    def test_all_assigned_false(self):
        problem = default_consistent_problem_set_values()
        problem.reset_value(1)
        self.assertFalse(problem.all_assigned())

    def test_set_value(self):
        problem = default_consistent_problem_set_values()
        problem.set_value(1, 2)
        self.assertEqual(problem.variables[1].get_value(), 2)

    def test_set_value_out_of_scope(self):
        problem = default_consistent_problem_set_values()
        orig_variables = problem.variables
        problem.set_value(5, 3)
        self.assertEqual(problem.variables, orig_variables)

    def test_reset_value(self):
        problem = default_consistent_problem_set_values()
        problem.reset_value(1)
        self.assertIsNone(problem.variables[1].get_value())

    def test_get_domain(self):
        problem = default_consistent_problem_set_values()
        self.assertEqual(problem.get_domain(1), [0, 1, 2, 3, 4, 5])

    def test_num_variables(self):
        problem = default_consistent_problem_set_values()
        self.assertEqual(problem.num_variables(), 3)

    def test_will_be_consistent(self):
        problem = default_consistent_problem_set_values()
        self.assertTrue(problem.will_be_consistent(2, 1))
        self.assertEqual(problem.variables[2].get_value(), 2)

    def test_will_be_consistent_false(self):
        problem = default_consistent_problem_set_values()
        self.assertFalse(problem.will_be_consistent(2, 0))
        self.assertEqual(problem.variables[2].get_value(), 2)

    def test_variable_assignments(self):
        problem = default_consistent_problem_set_values()
        self.assertEqual(problem.variable_assignments(), (2, 1, 2))
