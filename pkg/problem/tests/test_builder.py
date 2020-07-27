import unittest
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.problem.builder import default_portfolio_optimization_problem
from pkg.problem.builder import generate_many_random_solutions


class BuilderTest(unittest.TestCase):
    def test_build(self):
        default_portfolio_optimization_problem()

    def test_generate_many_random_solutions(self):
        problem = default_consistent_problem()
        individuals = generate_many_random_solutions(problem, 2)
        self.assertIsNotNone(individuals)
        self.assertEqual(len(individuals), 2)
