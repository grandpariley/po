import unittest
import random
import copy
import unittest.mock as mock
from pkg.random.random import Random
from pkg.consts import Constants
from pkg.problem.tests.default_problems import default_consistent_problem_set_values
from pkg.pso.particle import Particle


class ParticleTest(unittest.TestCase):
    def default_particle(self):
        return Particle(default_consistent_problem_set_values())

    def test_move(self):
        particle = self.default_particle()
        old_position = particle.problem.objective_values()
        particle.velocity = [1, 1, 1]
        v = particle.velocity
        particle.move()
        new_position = particle.problem.objective_values()
        self.assertEqual(old_position[0] + v[0], new_position[0])
        self.assertEqual(old_position[1] + v[1], new_position[1])
        self.assertEqual(old_position[2] + v[2], new_position[2])

    def test_accelerate(self):
        Random.begin_test()
        for _ in range(6):
            Random.set_test_value_for("random_float_between_0_and_1", 0.5)
        particle = self.default_particle()
        old_particle = copy.deepcopy(particle)
        particle.accelerate()
        new_velocity = particle.velocity
        calculated_velocity = [
            (Constants.PSO_DRAG * old_particle.velocity[i]) + (Constants.PSO_SOCIAL_SCALE * Random.random_float_between_0_and_1() * (old_particle.best.get_value(i) - old_particle.problem.get_value(
                i))) + (Constants.PSO_COGNITIVE_SCALE * Random.random_float_between_0_and_1() * (old_particle.best.get_value(i) - old_particle.problem.get_value(i)))
            for i in range(3)
        ]
        self.assertEqual(calculated_velocity[0], new_velocity[0])
        self.assertEqual(calculated_velocity[1], new_velocity[1])
        self.assertEqual(calculated_velocity[2], new_velocity[2])
        Random.end_test()

    def test_update_best(self):
        particle = Particle(default_consistent_problem_set_values())
        better_problem = default_consistent_problem_set_values()
        better_problem.set_value(0, 3)
        better_problem.set_value(2, 3)
        self.assertEqual(str(particle.problem), str(particle.get_best()))
        particle.problem = better_problem
        particle.update_best()
        self.assertEqual(str(particle.best), str(better_problem))
