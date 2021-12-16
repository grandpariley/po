import unittest

from pkg.consts import Constants
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain
from pkg.problem.tests.default_problems import default_consistent_problem


class BuilderTest(unittest.TestCase):
    def test_build(self):
        problem = default_portfolio_optimization_problem()
        print(problem)
        self.assertTrue(True)

    def test_generate(self):
        problems = generate_solutions_discrete_domain(default_portfolio_optimization_problem(), 5)
        print(problems)
        self.assertTrue(True)
