import random

class Particle:
    def __init__(self, problem):
        self.problem = problem
        self.best_values = self.problem.objective_values()
        self.velocity = [0 for _ in problem.num_variables()]
    
    def move(self):
        for i in range(self.problem.num_variables()):
            self.problem.set_value(i, self.problem.closet_in_domain(i, self.velocity[i] + self.problem.get_domain(i)))
    
    def accelerate(self):
        pass

    def update_best(self, global_best):
        pass

    def get_best(self):
        return self.best_values

    def get_problem(self):
        return self.problem

