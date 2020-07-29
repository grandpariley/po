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

    def global_pollination(self, flower_index):
        for o in range(self.flowers[flower_index].num_variables()):
            best_wrt_objective = self.get_best_wrt_objective(self.best, objective_index)
            new_value = self.flowers[flower_index].get_value(o) + Constants.FP_GAMMA_CONSTANT * Constants.FP_LEVY_CONSTANT * (best_wrt_objective.get_value(o) - self.flowers[flower_index].get_value(o))
            self.flowers[flower_index].safe_set_value(o, new_value)

    def local_pollination(self, flower_index):
        for o in range(self.flowers[flower_index].num_variables()):
            best_wrt_objective = self.get_best_wrt_objective(self.best, objective_index)
            new_value = self.flowers[flower_index].get_value(o) + Random.random_float_between_0_and_1() * (best_wrt_objective.get_value(o) - self.flowers[flower_index].get_value(o))
            self.flowers[flower_index].safe_set_value(o, new_value)

    def num_flowers(self):
        return len(self.flowers)

    def get_best_wrt_objective(self, flowers, objective_index):
        if not flowers:
            return None
        best = flowers[0]
        for f in flowers:
            if best.get_objective_values()[objective_index] < f.get_objective_values()[objective_index]:
                best = f
        return best
