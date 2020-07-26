import unittest
from pkg.nsga2.nsga2 import Nsga2 
from pkg.problem.tests.default_problems import defaultConsistentProblem

class Nsga2Test(unittest.TestCase):
    def test_solve(self):
        nsga2 = Nsga2(defaultConsistentProblem())
        # nsga2.solve()