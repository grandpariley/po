import json
import math

import matplotlib.pyplot as plt

from pkg.problem.compare import dominates

ORDER_OF_COLOURS = ['ko', 'ro', 'bo']
INDEX_TO_LABEL = ['VaR', 'CVaR', 'Return', 'Environment', 'Governance', 'Social']


def euclidean_distance(obj1, obj2):
    if obj1 is obj2:
        return 0
    if len(obj1) != len(obj2):
        return math.inf
    return math.sqrt(sum([pow(obj1[o] - obj2[o], 2) for o in range(len(obj1))]))


def get_pairwise_domination_counts(solutions1, solutions2):
    dominated_in_1 = 0
    dominated_in_2 = 0
    for s1 in solutions1:
        for s2 in solutions2:
            if dominates(s1.objective_values(), s2.objective_values()):
                dominated_in_2 += 1
            if dominates(s2.objective_values(), s1.objective_values()):
                dominated_in_1 += 1
    return dominated_in_1, dominated_in_2


def find_closest_solution_distance(s, all_solutions):
    closest_distance = math.inf
    for a in all_solutions:
        if s.objective_values() == a.objective_values():
            return 0
        d = euclidean_distance(s.objective_values(), a.objective_values())
        if d < closest_distance:
            closest_distance = d
    return closest_distance


def get_euclidean_distance_to_nearest(solutions, all_solutions):
    d_metric = []
    for s in solutions:
        d_metric.append(find_closest_solution_distance(s, all_solutions))
    return d_metric


def get_d_metric(solutions):
    all_solutions = get_all_solutions(solutions)
    d_metric = []
    for key in solutions:
        ed = get_euclidean_distance_to_nearest(solutions[key], all_solutions)
        if ed == 0:
            continue
        d_metric.append({key: ed})
    return d_metric


def get_c_metric(solutions):
    c_metric = []
    done = []
    for key in solutions:
        for key2 in solutions:
            if key == key2 or (key, key2) in done or (key2, key) in done:
                continue
            done.append((key, key2))
            key2_dominates_key, key_dominates_key2 = get_pairwise_domination_counts(solutions[key], solutions[key2])
            c_metric.append({key: key_dominates_key2, key2: key2_dominates_key})
    return c_metric


def get_all_solutions(solutions):
    all_solutions = []
    for k in solutions:
        all_solutions = all_solutions + solutions[k]
    for a in all_solutions:
        for b in all_solutions:
            if dominates(a.objective_values(), b.objective_values()):
                all_solutions.remove(b)
            if dominates(b.objective_values(), a.objective_values()):
                all_solutions.remove(a)
    return all_solutions


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
    def __init__(self, solutions, timer):
        self.solutions = solutions
        self.timer = timer

    def dump_graph(self, objective_indexes, nrows=None, ncols=None):
        if nrows is None or ncols is None:
            nrows = 2
            ncols = int(math.comb(len(objective_indexes), 2) / 2)
        figure, axis = plt.subplots(nrows, ncols, figsize=(28, 12))
        plot(self.solutions, axis, ncols, nrows, objective_indexes)
        # plt.savefig('Figure_1.png')
        plt.show()

    def dump_solutions(self):
        for key in self.solutions:
            with open(key + '-solutions.json', 'w') as file:
                json.dump([{
                    "objectiveValues": s.objective_values(),
                    "variables": [{
                        "ticker": v,
                        "amount": s.variables[v].get_value()
                    } for v in s.variables]
                } for s in self.solutions[key]], file)

    def dump_time(self):
        with open('times.json', 'w') as file:
            json.dump(self.timer.times, file)

    def dump_metrics(self):
        with open('metrics.json', 'w') as file:
            json.dump({
                "c_metric": get_c_metric(self.solutions),
                "d_metric": get_d_metric(self.solutions)
            }, file)
