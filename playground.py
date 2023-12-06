import csv
import json
import math

import matplotlib.pyplot as plt
import argparse
from pkg.consts import Constants
from pkg.evaluation.evaluation import INDEX_TO_LABEL
from pkg.problem.compare import dominates


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--Cmetric", help="C metric graph", action='store_true')
    parser.add_argument("-d", "--Dmetric", help="D metric graph", action='store_true')
    parser.add_argument("-t", "--Times", help="Time graph graph", action='store_true')
    parser.add_argument("-w", "--Weights", help="Compute the portfolio for given weights", action='store_true')
    parser.add_argument("-q", "--TableWeights", help="Take the computed weights and make a csv table", action='store_true')

    args = parser.parse_args()
    todo = []
    if args.Cmetric:
        todo.append("c")
    if args.Times:
        todo.append("t")
    if args.Dmetric:
        todo.append("d")
    if args.Weights:
        todo.append("w")
    if args.TableWeights:
        todo.append("q")

    return todo


def main():
    todo = args_parse()
    if 't' in todo:
        moead_times, nsga2_times = get_times()
        show_times(moead_times, nsga2_times)
    if 'c' in todo:
        moead_c_metrics, nsga2_c_metrics = get_c_metrics()
        show_c_metrics(moead_c_metrics, nsga2_c_metrics)
    if 'd' in todo:
        moead_d_metrics = get_d_metrics('moead')
        show_d_metrics(moead_d_metrics, 'ro')
        nsga2_d_metrics = get_d_metrics('nsga2')
        show_d_metrics(nsga2_d_metrics, 'ko')
    if 'w' in todo:
        print_best_portfolio_for_weights()
    if 'q' in todo:
        convert_weight_json_to_csv('Bob', 'moead')
        convert_weight_json_to_csv('Alice', 'moead')
        convert_weight_json_to_csv('Sam', 'moead')
        convert_weight_json_to_csv('Sarah', 'moead')
        convert_weight_json_to_csv('Bob', 'nsga2')
        convert_weight_json_to_csv('Alice', 'nsga2')
        convert_weight_json_to_csv('Sam', 'nsga2')
        convert_weight_json_to_csv('Sarah', 'nsga2')


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
    moead_solutions, nsga2_solutions = get_best_solutions_by_weights()
    with open('nsga2-best_portfolios.json', 'w') as json_file:
        json.dump(nsga2_solutions, json_file)
    with open('moead-best_portfolios.json', 'w') as json_file:
        json.dump(moead_solutions, json_file)


def get_best_solutions_by_weights():
    nsga2_solutions = []
    moead_solutions = []
    with open('weights.json') as json_file:
        investors = json.load(json_file)
        for investor in investors:
            moead_best, moead_best_value = get_best_solution_for_weight(investor['weights'], 'moead')
            moead_solutions.append({
                "investor": investor['person'],
                "investor_description": investor['description'],
                "best": moead_best,
                "best_value": moead_best_value
            })
            nsga2_best, nsga2_best_value = get_best_solution_for_weight(investor['weights'], 'nsga2')
            nsga2_solutions.append({
                "investor": investor['person'],
                "investor_description": investor['description'],
                "best": nsga2_best,
                "best_value": nsga2_best_value
            })
    return moead_solutions, nsga2_solutions


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


def get_d_metrics(key):
    d_metrics = []
    for i in range(Constants.NUM_RUNS):
        with open('runs/' + str(i) + '-metrics.json') as json_file:
            data = json.load(json_file)
            metrics = []
            for d in range(len(data['d_metric'])):
                if key in data['d_metric'][d].keys():
                    metrics = data['d_metric'][d][key]
            if len(metrics) > 0:
                d_metrics.append(sum(metrics) * 1.000 / len(metrics))
            else:
                d_metrics.append(0)
    return d_metrics


def show_d_metrics(d_metrics, colour):
    plt.plot([i for i in range(Constants.NUM_RUNS)], d_metrics, colour)
    plt.xlabel("Generation")
    plt.ylabel("Average euclidean distance from approximated Pareto front")
    plt.show()


def get_c_metrics():
    nsga2_c_metrics = []
    moead_c_metrics = []
    for i in range(Constants.NUM_RUNS):
        moead_solutions_count = get_number_of_solutions_by_run_and_alg(i, 'moead')
        nsga2_solutions_count = get_number_of_solutions_by_run_and_alg(i, 'nsga2')
        with open('runs/' + str(i) + '-metrics.json') as json_file:
            data = json.load(json_file)
            # FIXME - I calculated this backwards
            nsga2_c_metrics.append(data['c_metric'][0]['moead'] / nsga2_solutions_count)
            moead_c_metrics.append(data['c_metric'][0]['nsga2'] / moead_solutions_count)
    return moead_c_metrics, nsga2_c_metrics


def get_number_of_solutions_by_run_and_alg(i, alg):
    with open('runs/' + str(i) + '-' + alg + '-solutions.json') as json_file:
        return len(json.load(json_file))


def show_c_metrics(moead_c_metric, nsga2_c_metric):
    plt.plot([i for i in range(Constants.NUM_RUNS)], nsga2_c_metric, 'ko')
    plt.plot([i for i in range(Constants.NUM_RUNS)], moead_c_metric, 'ro')
    plt.xlabel("Generation")
    plt.ylabel("Number of dominated solutions")
    plt.show()


def show_times(moead_times, nsga2_times):
    plt.plot([i for i in range(Constants.NUM_RUNS)], nsga2_times, 'ko')
    plt.plot([i for i in range(Constants.NUM_RUNS)], moead_times, 'ro')
    plt.xlabel("Generation")
    plt.ylabel("Time (in ms)")
    plt.show()


def get_times():
    nsga2_times = []
    moead_times = []
    for i in range(Constants.NUM_RUNS):
        with open('runs/' + str(i) + '-times.json') as json_file:
            data = json.load(json_file)
            nsga2_times.append(data['nsga2'] / 1000000)
            moead_times.append(data['moead'] / 1000000)
    return moead_times, nsga2_times


if __name__ == '__main__':
    main()
