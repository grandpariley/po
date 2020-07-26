import unittest
from pkg.flowerpollination.flower_pollination import FlowerPollination 
from pkg.problem.tests.default_problems import defaultConsistentProblem

class FlowerPollinationTest(unittest.TestCase):
    def test_solve(self):
        flower_pollination = FlowerPollination(defaultConsistentProblem())
        # flower_pollination.solve()