import unittest
from pkg.pso.pso import Pso
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.consts import Constants
from pkg.log import Log


class PsoTest(unittest.TestCase):
    def test_solve(self):
        Constants.PSO_SWARM_SIZE = 3
        Constants.PSO_MAX_ITERATIONS = 100
        pso = Pso(default_consistent_problem())
        solutions = pso.solve()
        Log.newline()
        Log.log([str(s) for s in solutions], context="test-pso")
