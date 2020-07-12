import unittest
from pkg.pso.particle import Particle
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint

class ParticleTest(unittest.TestCase):
    def defaultVariables(self):
        return [
            Variable([0, 1, 2, 3]),
            Variable([0, 1, 2, 3]),
            Variable([0, 1, 2, 3]),
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
            ], [lambda variables : v.get_value() for v in variables])

    def defaultParticle(self):
        return Particle(self.defaultConsistentProblem())

    def test_move_no_velocity(self):
        particle = self.defaultParticle()
        old_position = particle.problem.objective_values()
        v = particle.velocity
        particle.move()
        new_position = particle.problem.objective_values()
        self.assertEqual(old_position[0] + v[0], new_position[0])
        self.assertEqual(old_position[1] + v[1], new_position[1])
        self.assertEqual(old_position[2] + v[2], new_position[2])

    def test_move(self):
        particle = self.defaultParticle()
        old_position = particle.problem.objective_values()
        particle.velocity = [1, 1, 1]
        v = particle.velocity
        particle.move()
        new_position = particle.problem.objective_values()
        self.assertEqual(old_position[0] + v[0], new_position[0])
        self.assertEqual(old_position[1] + v[1], new_position[1])
        self.assertEqual(old_position[2] + v[2], new_position[2])