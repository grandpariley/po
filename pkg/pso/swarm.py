import copy
from pkg.pso.particle import Particle
from pkg.problem.compare import dominates

class Swarm:
    def __init__(self, particles):
        self.particles = particles
        if self.particles:
            self.best = self.particles[-1]
        else:
            self.best = None

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
        self.best = self.top()
        for particle in self.particles:
            if dominates(particle.problem.objective_values(), self.best.problem.objective_values()):
                self.best = copy.deepcopy(particle)

    def get_best(self):
        return self.best

