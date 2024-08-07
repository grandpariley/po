from itertools import cycle
import json
import math
import os.path

import matplotlib.pyplot as plt
from numpy import floor

from pkg.consts import Constants
from pkg.parse.portfolio_option import PortfolioOption
from pkg.problem.builder import default_portfolio_optimization_problem_arch_1
from pkg.problem.compare import dominates
from pkg.problem.problem import problem_encoder_fn

ORDER_OF_COLOURS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
INDEX_TO_LABEL = ['risk', 'return', 'environment', 'governance', 'social']


def get_index_expected_return(investor):
    if not investor:
        raise ValueError
    with open('index-data.json', 'r') as json_file:
        index_data = json.load(json_file)['^GSPTSE']
        problem = default_portfolio_optimization_problem_arch_1(investor)
        problem.set_value('^GSPTSE', floor(Constants.BUDGET / index_data['price']), info=PortfolioOption(index_data))
        return problem.objective_values()[0]


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


def plot_one(solutions, axis, objective_index, objective_index2):
    colour = iter(cycle(ORDER_OF_COLOURS))
    for s in solutions:
        axis.scatter(
            s.objective_values()[objective_index],
            s.objective_values()[objective_index2],
            c=next(colour)
        )
    axis.set_title(
        INDEX_TO_LABEL[objective_index] + " compared to " + INDEX_TO_LABEL[objective_index2]
    )


def plot(solutions, axis, cols, rows, objective_indexes):
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
            plot_one(solutions, axis[axis_count_rows][axis_count_cols], objective_index, objective_index2)
            axis_count_rows = (axis_count_rows + 1) % rows
            axis_count_cols = (axis_count_cols + 1) % cols


class Evaluation:
    def __init__(self, prefix, solutions, timer):
        self.prefix = str(prefix)
        self.solutions = solutions
        self.timer = timer

    def dump_graph(self, objective_indexes_dict, rows=None, cols=None, investor=None):
        for objective_indexes_key in objective_indexes_dict:
            if len(objective_indexes_dict[objective_indexes_key]) > 1:
                if rows is None or cols is None:
                    rows = 2
                    cols = int(math.comb(len(objective_indexes_dict[objective_indexes_key]), 2) / 2)
                figure, axis = plt.subplots(rows, cols, figsize=(28, 12))
                plot(self.solutions['arch2'], axis, cols, rows, objective_indexes_dict[objective_indexes_key])
                if not os.path.exists(objective_indexes_key):
                    os.mkdir(objective_indexes_key)
            else:
                plt.bar([objective_indexes_key, 'benchmark'],
                        [self.solutions['arch1'][0].objective_values()[0], get_index_expected_return(investor)])
            plt.savefig(objective_indexes_key + '/' + self.prefix + '/figure.png')
            plt.clf()
        # plt.show()

    def dump_time(self):
        if len(self.timer.times) != 0:
            with open(self.prefix + '-times.json', 'w') as file:
                json.dump(self.timer.times, file)
