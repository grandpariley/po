import unittest
from pkg.pso.swarm import Swarm
from pkg.pso.particle import Particle
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint

class SwarmTest(unittest.TestCase):
    def defaultVariables(self):
        return [
            Variable([0, 1, 2, 3]),
            Variable([0, 1, 2, 3]),
            Variable([0, 1, 2, 3]),
        ]

    def defaultConsistentProblem(self):
        variables = self.defaultVariables()
        return Problem(
            variables,
            [
                Constraint((0, 2),
                           lambda variables: variables[0] == variables[1]),
                Constraint(tuple([2]), lambda variables: variables[0] > 0)
            ], [lambda variables: v.get_value() for v in variables])

    def default_problems(self):
        problems = [self.defaultConsistentProblem() for _ in range(3)]
        problems[0].variables[0].set_value(1)
        problems[0].variables[1].set_value(1)
        problems[0].variables[2].set_value(1)
        problems[1].variables[0].set_value(2)
        problems[1].variables[1].set_value(1)
        problems[1].variables[2].set_value(2)
        problems[2].variables[0].set_value(2)
        problems[2].variables[1].set_value(0)
        problems[2].variables[2].set_value(2)
        return problems

    def default_particles(self):
        return [Particle(p) for p in self.default_problems()]

    def default_swarm(self):
        return Swarm(self.default_particles())

    def test_update_best(self):
        swarm = self.default_swarm()
        swarm.update_best()
        self.assertEqual(swarm.get_best(), set([swarm.get_particles()[1], swarm.get_particles()[2]]))
