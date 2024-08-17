import csv
import json
import math
import os.path

import matplotlib.pyplot as plt
from numpy.ma.extras import average
from itertools import cycle, combinations

from main import PROBLEMS
from pkg.consts import Constants

COLOURS = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'aquamarine', 'mediumseagreen', 'burlywood', 'coral']
MARKERS = ['.', 'o', 'v', '^', '<', '>', 's', 'x', 'd', '|', '_']
INDEX_TO_LABEL = ['risk', 'return', 'environment', 'governance', 'social']
LABELS = {
    'arch2': 'Architecture 2',
    'arch1-sam': 'Sam',
    'arch1-jars': 'Jars',
    'arch1-alice': 'Alice'
}


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


def graph_solution_bigraph(name, solutions):
    if len(solutions[0][0]['objectives']) <= 1:
        return
    markers = cycle(MARKERS)
    colours = cycle(COLOURS)
    for run in range(Constants.NUM_RUNS):
        for (objective_index1, objective_index2) in combinations(range(len(INDEX_TO_LABEL)), 2):
            if objective_index1 == objective_index2:
                continue
            plt.scatter(
                x=[solution['objectives'][objective_index1] for solution in solutions[run]],
                y=[solution['objectives'][objective_index2] for solution in solutions[run]],
                marker=next(markers),
                color=next(colours)
            )
            plt.savefig(name + '/' +
                        str(run) + '/' +
                        INDEX_TO_LABEL[objective_index1] + '-' + INDEX_TO_LABEL[objective_index2] + '.png')
            plt.clf()


def graph_generations(name, generations):
    markers = cycle(MARKERS)
    colours = cycle(COLOURS)
    for run in range(Constants.NUM_RUNS):
        for objective_index in range(len(generations[0][0][0]['objectives'])):
            plt.scatter(
                x=range(len(generations)),
                y=[flatten(generation, objective_index) for generation in generations[run]],
                color=next(colours),
                marker=next(markers)
            )
    plt.savefig(name + '/generations.png')
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


def get_csv_portfolios(solution_index, solution):
    portfolios = []
    for variable, amount in solution['variables'].items():
        portfolios.append([solution_index, variable, amount])
    return portfolios


def get_table_portfolio(solutions):
    portfolios = []
    for solution_index in range(len(solutions)):
        portfolios.extend(get_csv_portfolios(solution_index, solutions[solution_index]))
    return portfolios


def table_portfolio(name, solutions_by_run):
    for run in range(len(solutions_by_run)):
        with open(name + '/' + str(run) + '/portfolio.csv', 'w') as csv_file:
            csv.writer(csv_file).writerows(get_table_portfolio(solutions_by_run[run]))


def csv_to_latex(row):
    s = '\\hline\n'
    for datum in row:
        s += str(datum) + ' & '
    return (s[:-3]) + ' \\\\\n'


def csv_to_latex_table(csv_filename, output_filename, caption, label, latex_rows):
    with open(csv_filename, 'r') as csv_file, open(output_filename, 'w') as output_file:
        output_file.write('\\begin{table}[ht]\n\\centering\\begin{tabular}{ ' + latex_rows + ' }\n')
        for row in csv.reader(csv_file):
            output_file.write(csv_to_latex(row))
        output_file.write('\\hline\n\\end{tabular}\\caption{' + caption + '}\n\\label{tab:' + label + '}\n\\end{table}')


def main():
    for name in PROBLEMS.keys():
        graph_generations(name, [get_generations(name, run) for run in range(Constants.NUM_RUNS)])
        solutions_by_run = [get_solutions(name, run) for run in range(Constants.NUM_RUNS)]
        graph_solution_bigraph(name, solutions_by_run)
        table_vs_benchmark(name, solutions_by_run)
        table_portfolio(name, solutions_by_run)
        # uses too much mem in overleaf lol
        # for run in range(Constants.NUM_RUNS):
        #     csv_to_latex_table(name + '/' + str(run) + '/portfolio.csv',
        #                        name + '/' + str(run) + '/portfolio.txt',
        #                        'Portfolio for run ' + str(run) + ' of ' + LABELS[name],
        #                        name + '-' + str(run) + '-portfolio',
        #                        '|l|c|c|')
        # csv_to_latex_table(name + '/benchmark-comparison.csv', name + '/benchmark-comparison.txt', 'Benchmark comparison for ' + name, name + '-benchmark')


if __name__ == '__main__':
    main()
