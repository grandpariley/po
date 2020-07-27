import copy
from pkg.random.random import Random
from pkg.problem.compare import dominates
from pkg.consts import Constants


class Particle:
    def __init__(self, problem):
        self.problem = problem
        self.best = copy.deepcopy(problem)
        self.velocity = [Random.random_float_between_0_and_1()
                         for _ in range(problem.num_variables())]

    def __str__(self):
        return str(self.best)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def move(self):
        for i in range(self.problem.num_variables()):
            self.problem.set_value(i, self.problem.closest_in_domain(
                i, self.velocity[i] + self.problem.get_value(i)))

    def accelerate(self):
        for i in range(self.problem.num_variables()):
            self.velocity[i] = (Constants.PSO_DRAG * self.velocity[i])
            + (Constants.PSO_SOCIAL_SCALE * Random.random_float_between_0_and_1() *
               (self.best.get_value(i) - self.problem.get_value(i)))
            + (Constants.PSO_COGNITIVE_SCALE * Random.random_float_between_0_and_1() *
               (self.best.get_value(i) - self.problem.get_value(i)))

    def update_best(self):
        if dominates(self.problem.objective_values(), self.best.objective_values()):
            self.best = copy.deepcopy(self.problem)

    def get_best(self):
        return self.best

    def get_problem(self):
        return self.problem

    def get_objective_values(self):
        return self.problem.objective_values()
