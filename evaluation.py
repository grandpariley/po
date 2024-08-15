import csv
import itertools
import json
import math
import os.path

import matplotlib.pyplot as plt
from numpy.ma.extras import average

from main import PROBLEMS
from pkg.consts import Constants

ORDER_OF_COLOURS = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
INDEX_TO_LABEL = ['risk', 'return', 'environment', 'governance', 'social']


def flatten(solutions, i=0):
    max_objective = -math.inf
    for solution in solutions:
        if solution['objectives'][i] > max_objective:
            max_objective = solution['objectives'][i]
    return max_objective


def get_weight_sensitive_objective_value(solution, investor):
    weights = list(investor['weights'])
    total = 0
    assert len(weights) == len(solution['objectives'])
    for i in range(len(weights)):
        total += weights[i] * solution['objectives'][i]
    return total


def graph_solution_bigraph(name, run, solutions):
    for (objective_index1, objective_index2) in itertools.combinations(range(len(INDEX_TO_LABEL)), 2):
        if objective_index1 == objective_index2:
            continue
        plt.scatter(
            x=[solution['objectives'][objective_index1] for solution in solutions],
            y=[solution['objectives'][objective_index2] for solution in solutions]
        )
        plt.savefig(
            name + '/' + run + '/' + INDEX_TO_LABEL[objective_index1] + '-' + INDEX_TO_LABEL[objective_index2] + '.png')
        plt.clf()


def graph_generations(name, run, generations):
    for objective_index in range(len(generations[0][0]['objectives'])):
        plt.scatter(
            x=range(len(generations)),
            y=[flatten(generation, objective_index) for generation in generations],
            color=next(ORDER_OF_COLOURS)
        )
    plt.savefig(name + '/' + run + '/generation.png')
    plt.clf()


def get_generations(name, run):
    generations = []
    for generation in range(Constants.NUM_GENERATIONS):
        if not os.path.exists(name + '/' + str(run) + '/gen-' + str(generation) + '.json'):
            continue
        with open(name + '/' + str(run) + '/gen-' + str(generation) + '.json', 'r') as json_file:
            generations.append(json.load(json_file))
    return generations


def get_solutions(name, run):
    with open(name + '/' + str(run) + '/solutions.json', 'r') as json_file:
        return json.load(json_file)


def calculate_one(solution, objective):
    return sum([
        value * Constants.DATA[name][objective] for name, value in solution['variables'].items()
    ]) / sum([
        value for value in solution['variables'].values()
    ])


def calculate_all(solutions, objective):
    return max([
        calculate_one(solution, objective) for solution in solutions
    ])


def calculate_average(solutions_by_run, objective):
    return average([
        calculate_all(solutions, objective) for solutions in solutions_by_run
    ])


def get_benchmark():
    with open('index-data.json', 'r') as json_file:
        return json.load(json_file)['^GSPTSE']


def get_table_vs_benchmark(solutions_by_run):
    benchmark = get_benchmark()
    return [
        ['return', calculate_average(solutions_by_run, 'return'), benchmark['return']],
        ['var', calculate_average(solutions_by_run, 'var'), benchmark['var']],
        ['cvar', calculate_average(solutions_by_run, 'cvar'), benchmark['cvar']],
        ['environment', calculate_average(solutions_by_run, 'environment'), 'N/A'],
        ['social', calculate_average(solutions_by_run, 'social'), 'N/A'],
        ['governance', calculate_average(solutions_by_run, 'governance'), 'N/A']
    ]


def table_vs_benchmark(name, solutions_by_run):
    with open(name + '/benchmark-comparison.csv', 'w') as csv_file:
        csv.writer(csv_file).writerows(get_table_vs_benchmark(solutions_by_run))


def main():
    for name in PROBLEMS.keys():
        # for run in range(Constants.NUM_RUNS):
        #     graph_generations(name, str(run), get_generations(name, run))
        #     solutions = get_solutions(name, run)
        #     if len(solutions[0]['objectives']) > 1:
        #         graph_solution_bigraph(name, str(run), solutions)
        table_vs_benchmark(name, [get_solutions(name, run) for run in range(Constants.NUM_RUNS)])


if __name__ == '__main__':
    main()
