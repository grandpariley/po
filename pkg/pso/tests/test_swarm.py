import unittest
from pkg.pso.swarm import Swarm
from pkg.pso.particle import Particle
from pkg.problem.tests.default_problems import default_consistent_problem


class SwarmTest(unittest.TestCase):

    def default_problems(self):
        problems = [default_consistent_problem() for _ in range(3)]
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
        self.assertEqual(swarm.get_best(), set(
            [swarm.get_particles()[1]]))
