import unittest

from pkg.consts import Constants
from pkg.moead.moead import refresh_ep, solve_helper, Moead
from pkg.moead.tests.test_util import default_individual, default_individuals
from pkg.problem.tests.default_problems import default_consistent_problem, get_test_data


class MoeadTest(unittest.TestCase):

    def test_solve_helper(self):
        Constants.NUM_GENERATIONS = 3
        Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS = 2
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
        moead = Moead([p1, p2, p3, p4, p5], get_test_data())
        actual_solution = moead.solve()
        self.assertTrue(True)

    def test_refresh_ep(self):
        ep = {default_individual()}
        y = default_individuals()[1]
        refresh_ep(ep, y)
        expected = [default_individual(), default_individual()]
        expected[0].problem.set_value('0', 1)
        expected[0].problem.set_value('1', 2)
        expected[0].problem.set_value('2', 2)
        expected[1].problem.set_value('0', 2)
        expected[1].problem.set_value('1', 1)
        expected[1].problem.set_value('2', 2)
        self.assertEqual(ep, set(expected))
