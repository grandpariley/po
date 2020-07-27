import unittest
from pkg.nsga2.nsga2 import Nsga2
from pkg.problem.tests.default_problems import default_consistent_problem


class Nsga2Test(unittest.TestCase):
    def test_solve(self):
        nsga2 = Nsga2(default_consistent_problem())
        # nsga2.solve()
