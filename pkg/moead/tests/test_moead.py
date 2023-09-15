import unittest

from pkg.moead.moead import refresh_ep
from pkg.moead.tests.test_util import default_individual, default_individuals


class MoeadTest(unittest.TestCase):

    def test_solve_helper(self):
        pass

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
