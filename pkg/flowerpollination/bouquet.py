from pkg.random.random import Random
from pkg.consts import Constants
from pkg.problem.compare import dominates


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers
        self.best = []

    def calculate_best(self):
        flowers = self.flowers + self.best
        dominated = []
        for i in flowers:
            for j in flowers:
                if j not in dominated and dominates(i.get_objective_values(), j.get_objective_values()):
                    dominated.append(j)
                elif i not in dominated and dominates(j.get_objective_values(), i.get_objective_values()):
                    dominated.append(i)
        self.best = list(set(flowers) - set(dominated))

    def get_best(self):
        return self.best

    def pollinate(self, flower_index):
        if Random.random_float_between_0_and_1() < Constants.FP_SWITCH_PROBABILITY:
            self.global_pollination(flower_index)
        else:
            self.local_pollination(flower_index)

    # TODO
    def global_pollination(self, flower_index):
        pass

    # TODO
    def local_pollination(self, flower_index):
        pass

    def num_flowers(self):
        return len(self.flowers)
