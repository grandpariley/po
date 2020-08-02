import unittest
from pkg.flowerpollination.flower_pollination import FlowerPollination
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.consts import Constants
from pkg.log import Log


class FlowerPollinationTest(unittest.TestCase):
    def test_solve(self):
        Constants.FP_MAX_GENERATIONS = 100
        Constants.FP_NUMBER_OF_FLOWERS = 10
        flower_pollination = FlowerPollination(default_consistent_problem())
        solutions = flower_pollination.solve()
        Log.newline()
        Log.log([str(s) for s in solutions], context="test-flower-pollination")

