import copy
from pkg.pso.particle import Particle
from pkg.problem.compare import dominates

class Swarm:
    def __init__(self, particles):
        self.particles = particles
        self.best = []

    def get_particles(self):
        return self.particles

    def top(self):
        if not self.particles:
            return None
        return self.particles[-1]

    def pop(self):
        if not self.particles:
            return
        self.particles.pop()

    def get_local_best(self, particle_index):
        if 0 <= particle_index < len(self.particles):
            return None
        return self.particles[particle_index].get_best()
    
    def update_best(self):
        self.best = [self.top()]
        for particle in self.particles:
            for b in self.best:
                if dominates(particle.get_objective_values(), b.get_objective_values()):
                    self.best.remove(b)
                    self.best.append(copy.deepcopy(b))

    def get_best(self):
        return self.best

