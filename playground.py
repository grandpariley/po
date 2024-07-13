import csv
import json
import math

import matplotlib.pyplot as plt
import argparse
from pkg.consts import Constants
from pkg.evaluation.evaluation import INDEX_TO_LABEL

WEIGHTS_FILE = 'response.json'
BUCKETS_FILE = 'buckets.json'


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--Times", help="Time graph graph", action='store_true')
    parser.add_argument("-w", "--Weights", help="Compute the portfolio for given weights", action='store_true')
    parser.add_argument("-q", "--TableWeights", help="Take the computed weights and make a csv table",
                        action='store_true')

    args = parser.parse_args()
    todo = []
    if args.Times:
        todo.append("t")
    if args.Weights:
        todo.append("w")
    if args.TableWeights:
        todo.append("q")

    return todo


def main():
    todo = args_parse()
    if 't' in todo:
        moead_times = get_times()
        show_times(moead_times)
    if 'w' in todo:
        print_best_portfolio_for_weights()
    if 'q' in todo:
        convert_weight_json_to_csv('Bob', 'moead')
        convert_weight_json_to_csv('Alice', 'moead')
        convert_weight_json_to_csv('Sam', 'moead')
        convert_weight_json_to_csv('Sarah', 'moead')


def find_investors_best(data, investor):
    for d in data:
        if d['investor'] == investor:
            return d['best']
    return []


def convert_weight_json_to_csv(investor, alg):
    with open(alg + '-best_portfolios.json') as json_file:
        data = json.load(json_file)
        best = find_investors_best(data, investor)
        with open(alg + '-' + investor + '.csv', 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for b in best:
                writer.writerow([b['ticker'], b['amount']])


def get_all_solutions(alg):
    all_solutions = []
    for i in range(Constants.NUM_RUNS):
        with open('runs/' + str(i) + '-' + alg + '-solutions.json') as json_file:
            data = json.load(json_file)
            all_solutions = all_solutions + data
    return all_solutions


def print_best_portfolio_for_weights():
    moead_solutions = get_best_solutions_by_weights()
    with open('moead-best_portfolios.json', 'w') as json_file:
        json.dump(moead_solutions, json_file)


def get_best_solutions_by_weights():
    moead_solutions = []
    with open(WEIGHTS_FILE) as json_file:
        investors = json.load(json_file)
        for investor in investors:
            moead_best, moead_best_value = get_best_solution_for_weight(investor, 'moead')
            moead_solutions.append({
                "investor": investor['person'],
                "investor_description": investor['description'],
                "best": moead_best,
                "best_value": moead_best_value
            })
    return moead_solutions


def remove_zero_amounts(portfolio):
    filtered_portfolio = []
    for v in portfolio:
        if v['amount'] > 0:
            filtered_portfolio.append(v)
    return filtered_portfolio


def get_best_solution_for_weight(weights, alg):
    all_solutions = get_all_solutions(alg)
    best = None
    best_value = -math.inf
    for s in all_solutions:
        value = sum(
            [s["objectiveValues"][o] * weights[INDEX_TO_LABEL[o]] for o in range(len(s["objectiveValues"]))]
        )
        if value > best_value:
            best_value = value
            best = s["variables"]
    return remove_zero_amounts(best), best_value


def get_number_of_solutions_by_run_and_alg(i, alg):
    with open('runs/' + str(i) + '-' + alg + '-solutions.json') as json_file:
        return len(json.load(json_file))


def show_times(moead_times):
    plt.plot([i for i in range(Constants.NUM_RUNS)], moead_times, 'ro')
    plt.xlabel("Generation")
    plt.ylabel("Time (in ms)")
    plt.show()


def get_times():
    moead_times = []
    for i in range(Constants.NUM_RUNS):
        with open('runs/' + str(i) + '-times.json') as json_file:
            data = json.load(json_file)
            moead_times.append(data['moead'] / 1000000)
    return moead_times


if __name__ == '__main__':
    main()
