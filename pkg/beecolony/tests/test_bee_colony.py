import unittest
from pkg.beecolony.bee_colony import BeeColony
from pkg.problem.tests.default_problems import defaultConsistentProblem
class BeeColonyTest(unittest.TestCase):
    def test_solve(self):
        bee_colony = BeeColony(defaultConsistentProblem())
        # bee_colony.solve()