import asyncio
import csv
import math
from itertools import cycle, combinations

import matplotlib.pyplot as plt

import db
from match import match_portfolio
from po.pkg.consts import Constants
from po.pkg.data import fetch

COLOURS = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'aquamarine', 'mediumseagreen', 'burlywood', 'coral']
MARKERS = ['.', 'o', 'v', '^', '<', '>', 's', 'x', 'd', '|', '_']
INDEX_TO_LABEL = ['cvar', 'var', 'return', 'environment', 'governance', 'social']
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
    for (objective_index1, objective_index2) in combinations(range(len(INDEX_TO_LABEL)), 2):
        if objective_index1 == objective_index2:
            continue
        colours = cycle(COLOURS)
        for run in range(Constants.NUM_RUNS):
            colour = next(colours)
            for s in range(len(solutions[run])):
                plt.scatter(
                    x=[solutions[run][s]['objectives'][objective_index2]],
                    y=[solutions[run][s]['objectives'][objective_index1]],
                    marker='$' + str(s) + '$',
                    color=colour,
                )
        plt.xlabel(INDEX_TO_LABEL[objective_index2])
        plt.ylabel(INDEX_TO_LABEL[objective_index1])
        filename = name + '/' + INDEX_TO_LABEL[objective_index1] + '-' + INDEX_TO_LABEL[objective_index2] + '.png'
        plt.savefig(filename)
        plt.clf()
        db.insert_image(filename)


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
    filename = name + '/generations.png'
    plt.savefig(name + '/generations.png')
    plt.clf()
    db.insert_image(filename)


def get_generations(name, run):
    generations = []
    for generation in range(Constants.NUM_GENERATIONS):
        generations.append(asyncio.run(db.get_generation(name + "-" + str(run), generation)))
    return generations


def get_solutions(name, run):
    if name == 'arch2':
        return asyncio.run(db.get_arch2_portfolios(run))
    return asyncio.run(db.get_portfolio(str(name) + '-' + str(run)))


def calculate_one(solution, objective):
    return sum([
        value * fetch(name)[objective] for name, value in solution['variables'].items()
    ]) / sum([
        value for value in solution['variables'].values()
    ])


def get_benchmark():
    return asyncio.run(fetch(''))


def get_table_vs_benchmark_one_solution(solution):
    benchmark = get_benchmark()
    return {
        'return': {'solution': calculate_one(solution, 'return'), 'benchmark': benchmark['return']},
        'var': {'solution': calculate_one(solution, 'var'), 'benchmark': benchmark['var']},
        'cvar': {'solution': calculate_one(solution, 'cvar'), 'benchmark': benchmark['cvar']},
        'environment': {'solution': calculate_one(solution, 'environment'), 'benchmark': 'N/A'},
        'social': {'solution': calculate_one(solution, 'social'), 'benchmark': 'N/A'},
        'governance': {'solution': calculate_one(solution, 'governance'), 'benchmark': 'N/A'}
    }


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
        output_file.write(
            '\\hline\n\\end{tabular}\\caption{' + caption + '}\n\\label{tab:' + label + '}\n\\end{table}')


def get_solution_for_investor(investor, run):
    weights = get_weight_from_investor(investor)
    solutions = asyncio.run(db.get_arch2_portfolios(run=run))
    return match_portfolio(weights, solutions)


def get_weight_from_investor(investor):
    for i in Constants.INVESTORS:
        if i['person'] == investor:
            return i['weights']
    return None


def table_vs_benchmark_one_solution(investor, run):
    solution = get_solution_for_investor(investor, run)
    asyncio.run(db.save_table_vs_benchmark('arch2-' + str(run), get_table_vs_benchmark_one_solution(solution)))


def main(arch1_names):
    for name in arch1_names:
        graph_generations(name, [get_generations(name, run) for run in range(Constants.NUM_RUNS)])
        graph_solution_bigraph(name, [get_solutions(name, run) for run in range(Constants.NUM_RUNS)])
    for run in range(Constants.NUM_RUNS):
        for investor in Constants.INVESTORS:
            table_vs_benchmark_one_solution(investor, run)
        # uses too much mem in overleaf lol
        # for run in range(Constants.NUM_RUNS):
        #     csv_to_latex_table(name + '/' + str(run) + '/portfolio.csv',
        #                        name + '/' + str(run) + '/portfolio.txt',
        #                        'Portfolio for run ' + str(run) + ' of ' + LABELS[name],
        #                        name + '-' + str(run) + '-portfolio',
        #                        '|l|c|c|')
        # csv_to_latex_table(name + '/benchmark-comparison.csv', name + '/benchmark-comparison.txt', 'Benchmark comparison for ' + name, name + '-benchmark')


if __name__ == '__main__':
    main(['Alice', 'Sam', 'Jars'])
