import unittest
from pkg.spea2.spea2 import Spea2 
from pkg.problem.tests.default_problems import default_consistent_problem

class Spea2Test(unittest.TestCase):
    def test_solve(self):
        spea2 = Spea2(default_consistent_problem())
        # spea2.solve()