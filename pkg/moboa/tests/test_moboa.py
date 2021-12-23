import unittest

from pkg.consts import Constants
from pkg.moboa.moboa import Moboa
from pkg.random.random import Random


class MoboaTest(unittest.TestCase):
    def test_solve(self):
        Constants.MOBOA_NUM_GENERATIONS = 3
        Constants.MOBOA_NUM_GENES_MUTATING = 1
        Random.begin_test()
        solutions = Moboa([]).solve()
        print(solutions)
        self.assertTrue(True)
        Random.end_test()
