import unittest
from pkg.pso.particle import Particle

class ParticleTest(unittest.TestCase):
    def defaultParticle(self):
        return Particle()

    def test_move(self):
        particle = self.defaultParticle()
        old_position = particle.curr_position
        v = particle.velocity
        particle.move()
        new_position = particle.curr_position
        self.assertEqual(old_position[0] + v[0], new_position[0])
        self.assertEqual(old_position[1] + v[1], new_position[1])