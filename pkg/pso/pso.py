from pkg.problem.solver import Solver
from pkg.pso.swarm import Swarm
from pkg.pso.particle import Particle
from pkg.problem.builder import generateManyRandomSolutions
from pkg.problem.compare import dominates

SWARM_SIZE = 30
MAX_ITERATIONS = 100

class Pso(Solver):
    def solve_helper(self):
        for _ in range(MAX_ITERATIONS):
            for particle in self.swarm.get_particles():
                particle.update_best()
            self.swarm.update_best()
            for particle in self.swarm.get_particles():
                particle.accelerate()
                particle.move()
        return self.swarm.get_best().get_problem()

    def solve(self):
        self.swarm = Swarm([Particle(p) for p in generateManyRandomSolutions(self.problem, SWARM_SIZE)])
        return self.solve_helper()