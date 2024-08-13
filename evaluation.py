from itertools import cycle
import json
import math
import os.path

import matplotlib.pyplot as plt
from numpy import floor

from main import PROBLEMS
from pkg.consts import Constants
from pkg.parse.portfolio_option import PortfolioOption
from pkg.problem.builder import default_portfolio_optimization_problem_arch_1
from pkg.problem.compare import dominates

INVESTOR = 'Alice'
ORDER_OF_COLOURS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
INDEX_TO_LABEL = ['risk', 'return', 'environment', 'governance', 'social']


def arch1_flatten(generation):
    max_objective = -math.inf
    for solution in generation:
        if solution['objectives'][0] > max_objective:
            max_objective = solution['objectives'][0]
    return max_objective


def arch2_flatten(generation):
    max_objective = -math.inf
    for solution in generation:
        this_objective = get_weight_sensitive_objective_value(solution)
        if this_objective > max_objective:
            max_objective = this_objective
    return max_objective


FLATTENERS = {
    'arch1': arch1_flatten,
    'arch2': arch2_flatten
}


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


def dump_graph(solutions, objective_indexes_dict, rows=None, cols=None, investor=None):
    for run in range(Constants.NUM_RUNS):
        for objective_indexes_key in objective_indexes_dict:
            if len(objective_indexes_dict[objective_indexes_key]) > 1:
                if rows is None or cols is None:
                    rows = 2
                    cols = int(math.comb(len(objective_indexes_dict[objective_indexes_key]), 2) / 2)
                figure, axis = plt.subplots(rows, cols, figsize=(28, 12))
                plot(solutions['arch2'], axis, cols, rows, objective_indexes_dict[objective_indexes_key])
                if not os.path.exists(objective_indexes_key):
                    os.mkdir(objective_indexes_key)
            else:
                plt.bar([objective_indexes_key, 'benchmark'],
                        [solutions['arch1'][0].objective_values()[0], get_index_expected_return(investor)])
            plt.savefig(objective_indexes_key + '/' + str(run) + '/figure.png')
            plt.clf()
    # plt.show()


def get_weights():
    for investor in Constants.INVESTORS:
        if investor['person'] != INVESTOR:
            continue
        return investor['weights']
    return None


def get_weight_sensitive_objective_value(solution):
    weights = list(get_weights().values())
    total = 0
    assert len(weights) == len(solution['objectives'])
    for i in range(len(weights)):
        total += weights[i] * solution['objectives'][i]
    return total


def graph_generations(name, run, generations, flatten):
    plt.scatter(
        x=range(len(generations)),
        y=[flatten(generation) for generation in generations]
    )
    plt.savefig(name + '/' + run + '/figure.png')
    plt.clf()


def main():
    for run in range(Constants.NUM_RUNS):
        for name in PROBLEMS.keys():
            generations = []
            for generation in range(Constants.NUM_GENERATIONS):
                if not os.path.exists(name + '/' + str(run) + '/gen-' + str(generation) + '.json'):
                    continue
                with open(name + '/' + str(run) + '/gen-' + str(generation) + '.json', 'r') as json_file:
                    generations.append(json.load(json_file))
            graph_generations(name, str(run), generations, FLATTENERS[name])


if __name__ == '__main__':
    main()
