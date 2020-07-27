import unittest
import random
import copy
import unittest.mock as mock
from pkg.pso.particle import Particle, DRAG, SOCIAL_SCALE, COGNITIVE_SCALE
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
            ], [lambda variables: v.get_value() for v in variables])

    def defaultParticle(self):
        return Particle(self.defaultConsistentProblem())

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

    # TODO
    def test_accelerate(self):
        with mock.patch('random.uniform', lambda dont, care : 0.5):
            particle = self.defaultParticle()
            old_particle = copy.deepcopy(particle)
            particle.accelerate()
            new_velocity = particle.velocity
            calculated_velocity = [
                (DRAG * old_particle.velocity[i]) + (SOCIAL_SCALE * random.uniform(0.0, 1.0) * (old_particle.best.get_value(i) - old_particle.problem.get_value(i))) + (COGNITIVE_SCALE * random.uniform(0.0, 1.0) * (old_particle.best.get_value(i) - old_particle.problem.get_value(i)))
                for i in range(3)
            ]
            self.assertEqual(calculated_velocity[0], new_velocity[0])
            self.assertEqual(calculated_velocity[1], new_velocity[1])
            self.assertEqual(calculated_velocity[2], new_velocity[2])

    # TODO
    def test_update_best(self):
        pass
