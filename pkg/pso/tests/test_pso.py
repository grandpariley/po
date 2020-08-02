import unittest
from pkg.pso.pso import Pso
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.consts import Constants


class PsoTest(unittest.TestCase):
    def test_solve(self):
        Constants.PSO_SWARM_SIZE = 3
        Constants.PSO_MAX_ITERATIONS = 20
        pso = Pso(default_consistent_problem())
        solutions = pso.solve()
        print()
        print(str(solutions))
