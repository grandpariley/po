from pkg.random.random import Random
from pkg.consts import Constants
from pkg.problem.compare import get_dominated


def get_best_wrt_objective(flowers, objective_index):
    if not flowers:
        return None
    best = flowers[0]
    for f in flowers:
        if best.get_objective_values()[objective_index] < f.get_objective_values()[objective_index]:
            best = f
    return best


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers
        self.best = []

    def calculate_best(self):
        flowers = self.flowers + self.best
        dominated = get_dominated(flowers)
        self.best = list(set(flowers).difference(set(dominated)))

    def get_best(self):
        return self.best

    def pollinate(self, flower_index):
        if not self.best:
            self.calculate_best()
        if Random.random_float_between_0_and_1() < Constants.FP_SWITCH_PROBABILITY:
            self.global_pollination(flower_index)
        else:
            self.local_pollination(flower_index)

    def global_pollination(self, flower_index):
        for o in range(len(self.flowers[flower_index].get_objective_values())):
            best_wrt_objective = get_best_wrt_objective(self.best, o)
            for v in range(self.flowers[flower_index].num_variables()):
                new_value = self.flowers[flower_index].get_value(
                    v) + Constants.FP_GAMMA_CONSTANT * Constants.FP_LEVY_CONSTANT() * (
                                        best_wrt_objective.get_value(v) - self.flowers[flower_index].get_value(v))
                self.flowers[flower_index].safe_set_value(v, new_value)

    def local_pollination(self, flower_index):
        for o in range(len(self.flowers[flower_index].get_objective_values())):
            best_wrt_objective = get_best_wrt_objective(self.best, o)
            for v in range(self.flowers[flower_index].num_variables()):
                new_value = self.flowers[flower_index].get_value(v) + Random.random_float_between_0_and_1() * (
                            best_wrt_objective.get_value(v) - self.flowers[flower_index].get_value(v))
                self.flowers[flower_index].safe_set_value(v, new_value)

    def num_flowers(self):
        return len(self.flowers)
