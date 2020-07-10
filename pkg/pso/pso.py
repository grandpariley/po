from pkg.problem.solver import Solver
from pkg.pso.swarm import Swarm
from pkg.pso.particle import Particle
from pkg.problem.compare import compareObjectives

SWARM_SIZE = 30
MAX_ITERATIONS = 100
DRAG = 0.5
SOCIAL_SCALE = 1.5
COGNITIVE_SCALE = 1.5

class Pso(Solver):
    def solve_helper(self):
        for _ in range(MAX_ITERATIONS):
            best = self.swarm.top()
            for j in range(SWARM_SIZE):
                if compareObjectives(self.swarm.top(), best):
                    best = self.swarm.top()
            for particle in self.swarm.get_particles():
                particle.move()
                particle.accelerate()
                particle.update_best(best)
        return best.get_problem()


    def solve(self):
        self.swarm = Swarm([Particle(self.problem) for i in range(SWARM_SIZE)])
        return self.solve_helper()