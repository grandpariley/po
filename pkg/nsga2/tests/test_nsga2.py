import unittest
from pkg.nsga2.nsga2 import Nsga2
from pkg.problem.tests.default_problems import default_consistent_problem


class Nsga2Test(unittest.TestCase):
    # TODO
    def test_fast_non_dominating_sort(self):
        pass

    # TODO
    def test_crowding_distance_assignment(self):
        pass

    # TODO
    def test_generate_children(self):
        pass

    # TODO
    def test_get_parents(self):
        pass

    # TODO
    def test_get_children(self):
        pass

    # TODO
    def test_tournament(self):
        pass

    def test_solve(self):
        nsga2 = Nsga2(default_consistent_problem())
        # nsga2.solve()
