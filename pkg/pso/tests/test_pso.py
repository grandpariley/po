import unittest
from pkg.pso.pso import Pso 
from pkg.problem.problem import Problem 
from pkg.problem.constraint import Constraint
from pkg.problem.variable import Variable
from pkg.consts import Constants

class PsoTest(unittest.TestCase):
    def defaultVariables(self):
        return [
            Variable([0, 1, 2]),
            Variable([0, 1, 2]),
            Variable([0, 1, 2]),
        ]

    def defaultConsistentProblem(self):
        variables = self.defaultVariables()
        return Problem(
            variables,
            [
                Constraint((0, 2),
                           lambda variables: variables[0] == variables[1]),
                Constraint(tuple([2]), lambda variables: variables[0] > 0)
            ], [lambda v: tuple(u.get_value() for u in v)])

    def test_solve(self):
        Constants.PSO_SWARM_SIZE = 3
        pso = Pso(self.defaultConsistentProblem())
        solution = pso.solve()
        for s in solution:
            print(s)