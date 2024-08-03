import unittest

from pkg.problem.tests.default_problems import default_consistent_problem_set_values, default_consistent_problem, \
    default_inconsistent_problem_set_values, default_multi_objective_problem_set_values


class ProblemTest(unittest.TestCase):
    def test_consistent(self):
        problem = default_consistent_problem_set_values()
        self.assertTrue(problem.consistent())

    def test_inconsistent(self):
        problem = default_inconsistent_problem_set_values()
        self.assertFalse(problem.consistent())

    def test_objective_values(self):
        problem = default_multi_objective_problem_set_values()
        obj_vals = problem.objective_values()
        self.assertEqual(obj_vals, (5, -5))

    def test_objective_values_empty(self):
        problem = default_consistent_problem()
        problem.objective_funcs = None
        self.assertIsNone(problem.objective_values())

    def test_set_value(self):
        problem = default_consistent_problem_set_values()
        problem.set_value("1", 2)
        self.assertEqual(problem.variables["1"].get_value(), 2)

    def test_keys(self):
        self.assertEqual(["0", "1", "2"], default_consistent_problem().keys())

    def test_str(self):
        self.assertEqual(
            "{'variables': {'0': {'value': 2}, '1': {'value': 1}, '2': {'value': 2}}, 'constraints': [{'variables': ['0', '1']}, {'variables': ['2']}], 'objectives': [2, 1, 2]}",
            str(default_consistent_problem_set_values())
        )
