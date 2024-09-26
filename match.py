import json
import math

from po.pkg.consts import Constants

MOO_PROBLEMS = ['arch2']


def get_final_solutions_combined(problem):
    solutions = []
    for run in range(Constants.NUM_RUNS):
        with open(problem + '/' + str(run) + '/gen-' + str(Constants.NUM_GENERATIONS - 1) + '.json',
                  'r') as solutions_file:
            data = json.load(solutions_file)
            solutions.extend(data)
    return solutions


def get_value(solution, weights):
    print(weights)
    print(weights.values())
    if len(solution['objectives']) != len(weights.values()):
        raise ValueError('Illegal shape! ' + str(len(solution['objectives'])) + ' != ' + str(len(weights)))
    return sum([solution['objectives'][i] * list(weights.values())[i] for i in range(len(weights))])


def main():
    for problem in MOO_PROBLEMS:
        solutions = get_final_solutions_combined(problem)
        for investor in Constants.INVESTORS:
            max_solution = match_portfolio(investor['weights'], solutions)
            with open(problem + '/' + investor['person'].lower() + '.json', 'w') as solution_file:
                json.dump(max_solution, solution_file)


def match_portfolio(weights, solutions):
    max_solution = None
    max_value = -math.inf
    for solution in solutions:
        if max_solution is None or get_value(solution, weights) > max_value:
            max_solution = solution
    return max_solution



if __name__ == '__main__':
    main()
