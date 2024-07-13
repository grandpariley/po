import unittest

from pkg.problem.builder import default_portfolio_optimization_problem_arch_2, generate_solutions_discrete_domain


class BuilderTest(unittest.TestCase):
    @unittest.skip("data.json is not guaranteed to be there")
    def test_build(self):
        problem = default_portfolio_optimization_problem_arch_2()
        self.assertTrue(True)

    @unittest.skip("data.json is not guaranteed to be there")
    def test_generate(self):
        problems = generate_solutions_discrete_domain(default_portfolio_optimization_problem_arch_2(), 5)
        self.assertTrue(True)
