import unittest
from pkg.problem.builder import defaultPortfolioOptimizationProblem

class BuilderTest(unittest.TestCase):
    def test_build(self):
        defaultPortfolioOptimizationProblem()