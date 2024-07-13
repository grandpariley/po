import json
import math

import matplotlib.pyplot as plt

from pkg.problem.compare import dominates

ORDER_OF_COLOURS = ['ko', 'ro', 'bo']
INDEX_TO_LABEL = ['risk', 'return', 'environment', 'governance', 'social']


def get_all_solutions(solutions):
    all_solutions = set()
    dominated = set()
    for k in solutions:
        all_solutions = all_solutions.union(set(solutions[k]))
    for a in all_solutions:
        for b in all_solutions:
            if dominates(a.objective_values(), b.objective_values()):
                dominated.add(b)
            if dominates(b.objective_values(), a.objective_values()):
                dominated.add(a)
    return all_solutions.difference(dominated)


def plot_one(solutions, axis, axis_count_cols, axis_count_rows, objective_index, objective_index2):
    colour = iter(ORDER_OF_COLOURS)
    for key in solutions:
        axis[axis_count_rows, axis_count_cols].plot(
            [s.objective_values()[objective_index] for s in solutions[key]],
            [s.objective_values()[objective_index2] for s in solutions[key]],
            next(colour),
            label=key
        )
    axis[axis_count_rows, axis_count_cols].set_title(
        INDEX_TO_LABEL[objective_index] + " compared to " + INDEX_TO_LABEL[objective_index2]
    )


def plot(solutions, axis, ncols, nrows, objective_indexes):
    done = []
    axis_count_rows = 0
    axis_count_cols = 0
    for objective_index in objective_indexes:
        for objective_index2 in objective_indexes:
            if (objective_index == objective_index2 or
                    (objective_index, objective_index2) in done or
                    (objective_index2, objective_index) in done):
                continue
            done.append((objective_index, objective_index2))
            plot_one(solutions, axis, axis_count_cols, axis_count_rows, objective_index, objective_index2)
            axis_count_rows = (axis_count_rows + 1) % nrows
            axis_count_cols = (axis_count_cols + 1) % ncols


class Evaluation:
    def __init__(self, prefix, solutions, timer):
        self.prefix = str(prefix)
        self.solutions = solutions
        self.timer = timer

    def dump_graph(self, objective_indexes, nrows=None, ncols=None):
        if nrows is None or ncols is None:
            nrows = 2
            ncols = int(math.comb(len(objective_indexes), 2) / 2)
        figure, axis = plt.subplots(nrows, ncols, figsize=(28, 12))
        plot(self.solutions, axis, ncols, nrows, objective_indexes)
        plt.savefig(self.prefix + '-Figure_1.png')
        # plt.show()

    def dump_solutions(self):
        for key in self.solutions:
            with open(self.prefix + "-" + key + '-solutions.json', 'w') as file:
                json.dump([{
                    "objectiveValues": s.objective_values(),
                    "variables": [{
                        "ticker": v,
                        "amount": s.variables[v].get_value()
                    } for v in s.variables]
                } for s in self.solutions[key]], file)

    def dump_time(self):
        if len(self.timer.times) != 0:
            with open(self.prefix + '-times.json', 'w') as file:
                json.dump(self.timer.times, file)
