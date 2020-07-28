import unittest
from pkg.spea2.spea2 import Spea2
from pkg.problem.tests.default_problems import default_consistent_problem


class Spea2Test(unittest.TestCase):
    # TODO
    def test_calculate_fitness(self):
        pass

    # TODO
    def test_truncate(self):
        pass

    # TODO
    def test_binary_tournament_selection(self):
        pass

    # TODO
    def test_get_tournament_pool(self):
        pass

    # TODO
    def test_assign_tournament_probabilities(self):
        pass

    def test_solve(self):
        spea2 = Spea2(default_consistent_problem())
        # spea2.solve()
