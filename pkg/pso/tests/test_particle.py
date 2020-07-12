import unittest
from pkg.pso.particle import Particle
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint

class ParticleTest(unittest.TestCase):
    def defaultVariables(self):
        return [
            Variable([0, 1, 2]),
            Variable([0, 1, 2]),
            Variable([0, 1, 2]),
        ]

    def defaultConsistentProblem(self):
        variables = self.defaultVariables()
        variables[0].set_value(2)
        variables[1].set_value(1)
        variables[2].set_value(2)
        return Problem(
            variables,
            [
                Constraint((0, 2),
                           lambda variables: variables[0] == variables[1]),
                Constraint(tuple([1]), lambda variables: variables[0] == 1),
                Constraint(tuple([2]), lambda variables: variables[0] > 0)
            ], None)

    def defaultParticle(self):
        return Particle(self.defaultConsistentProblem())

    # def test_move(self):
    #     particle = self.defaultParticle()
    #     old_position = particle.curr_position
    #     v = particle.velocity
    #     particle.move()
    #     new_position = particle.curr_position
    #     self.assertEqual(old_position[0] + v[0], new_position[0])
    #     self.assertEqual(old_position[1] + v[1], new_position[1])