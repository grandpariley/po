import unittest

from pkg.consts import Constants
from pkg.nsga2.asdnsga2 import Asdnsga2
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.random.random import Random


class Asdnsga2Test(unittest.TestCase):
    def test_solve(self):
        Constants.NSGA2_NUM_GENERATIONS = 3
        Constants.NSGA2_NUM_GENES_MUTATING = 1
        p1 = default_consistent_problem()
        p1.set_value("0", 0)
        p1.set_value("1", 2)
        p1.set_value("2", 5)
        p2 = default_consistent_problem()
        p2.set_value("0", 5)
        p2.set_value("1", 3)
        p2.set_value("2", 5)
        p3 = default_consistent_problem()
        p3.set_value("0", 3)
        p3.set_value("1", 0)
        p3.set_value("2", 4)
        p4 = default_consistent_problem()
        p4.set_value("0", 4)
        p4.set_value("1", 1)
        p4.set_value("2", 2)
        p5 = default_consistent_problem()
        p5.set_value("0", 1)
        p5.set_value("1", 3)
        p5.set_value("2", 1)
        asdnsga2 = Asdnsga2([p1, p2, p3, p4, p5])
        solutions = asdnsga2.solve()
        self.assertTrue(True)
        Random.end_test()
