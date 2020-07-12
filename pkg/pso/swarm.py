from pkg.pso.particle import Particle

class Swarm:
    def __init__(self, particles):
        self.particles = particles

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
