import unittest
from pkg.spea2.spea2 import Spea2 
from pkg.problem.tests.default_problems import defaultConsistentProblem

class Spea2Test(unittest.TestCase):
    def test_solve(self):
        spea2 = Spea2(defaultConsistentProblem())
        # spea2.solve()