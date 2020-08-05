from pkg.problem.solver import Solver
from pkg.pso.swarm import Swarm
from pkg.pso.particle import Particle
from pkg.problem.builder import generate_many_random_solutions
from pkg.problem.compare import dominates
from pkg.consts import Constants
from pkg.log import Log


class Pso(Solver):
    def solve_helper(self):
        for _ in range(Constants.PSO_MAX_ITERATIONS):
            for particle in self.swarm.get_particles():
                particle.update_best()
            self.swarm.update_best()
            for particle in self.swarm.get_particles():
                particle.accelerate()
                particle.move()
        return tuple(b.get_problem() for b in self.swarm.get_best())

    def solve(self):
        self.swarm = Swarm([Particle(p) for p in generate_many_random_solutions(
            self.problem, Constants.PSO_SWARM_SIZE)])
        Log.begin_debug("pso")
        solns = self.solve_helper()
        Log.end_debug()
        return solns
        