import itertools
import json
import math
import os.path

import matplotlib.pyplot as plt

from main import PROBLEMS
from pkg.consts import Constants

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
    # 'arch1-alice': arch1_flatten,
    # 'arch1-jars': arch1_flatten,
    # 'arch1-sam': arch1_flatten,
    'arch2': arch2_flatten
}


def graph_solution_bigraph(name, run, solutions):
    for (objective_index1, objective_index2) in itertools.combinations(range(len(INDEX_TO_LABEL)), 2):
        plt.scatter(
            x=[solution['objectives'][objective_index1] for solution in solutions],
            y=[solution['objectives'][objective_index2] for solution in solutions]
        )
        plt.savefig(name + '/' + run + '/' + INDEX_TO_LABEL[objective_index1] + '-' + INDEX_TO_LABEL[objective_index2] + '.png')
        plt.clf()

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


def graph_generations(name, run, generations):
    plt.scatter(
        x=range(len(generations)),
        y=[FLATTENERS[name](generation) for generation in generations]
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


def main():
    for run in range(Constants.NUM_RUNS):
        for name in PROBLEMS.keys():
            # graph_generations(name, str(run), get_generations(name, run))
            graph_solution_bigraph(name, str(run), get_solutions(name, run))


if __name__ == '__main__':
    main()
