import unittest
from pkg.beecolony.bee_colony import BeeColony
from pkg.problem.tests.default_problems import default_consistent_problem
class BeeColonyTest(unittest.TestCase):
    @unittest.skip("bee coplony algorithm unfinished")
    def test_solve(self):
        bee_colony = BeeColony(default_consistent_problem())
        bee_colony.solve()