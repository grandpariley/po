import unittest
from pkg.flowerpollination.flower_pollination import FlowerPollination 
from pkg.problem.tests.default_problems import default_consistent_problem

class FlowerPollinationTest(unittest.TestCase):
    def test_solve(self):
        flower_pollination = FlowerPollination(default_consistent_problem())
        # flower_pollination.solve()