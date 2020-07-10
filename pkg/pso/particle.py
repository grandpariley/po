import random

class Particle:
    def __init__(self, problem):
        self.problem = problem
        self.best_values = self.problem.objective_values()
        self.velocity = [0, 0]
    
    def move(self):
        pass
    
    def accelerate(self):
        pass

    def update_best(self, global_best):
        pass

    def get_best(self):
        return self.best_values

    def get_problem(self):
        return self.problem

