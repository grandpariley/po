from copy import deepcopy
from pkg.pso.particle import Particle
from pkg.problem.compare import non_dominated, dominates


def get_dominated(particle, best):
    dominated = []
    for b in best:
        if dominates(particle.get_objective_values(), b.get_objective_values()):
            dominated.append(b)
    return dominated

class Swarm:
    def __init__(self, particles):
        self.particles = particles
        self.best = set()

    def get_particles(self):
        return self.particles

    def update_best(self):
        for p in self.particles:
            if non_dominated(p.get_objective_values(), [b.get_objective_values() for b in self.best]):
                self.best.add(deepcopy(p))
            for d in get_dominated(p, self.best):
                self.best.remove(d)

    def get_best(self):
        return self.best
