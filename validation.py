import json
from math import ceil

from pkg.consts import Constants
from pkg.problem.compare import dominates


def is_dominated(x, population):
    for individual in population:
        if dominates(individual['objectives'], x['objectives']):
            return True
    return False


def check_domination(non_dominated, parent_population):
    for nd in non_dominated:
        if is_dominated(nd, parent_population):
            raise ValueError("non-dominated solution is dominated!")


def check_budget(solutions):
    for s in range(len(solutions)):
        total_spent = 0
        for key, value in solutions[s]['variables'].items():
            total_spent += value * Constants.DATA[key]['price']
        if ceil(Constants.BUDGET) < total_spent:
            raise ValueError('SOLUTION ' + str(s) + ' IS OVER BUDGET: ' + str(total_spent))


def main():
    with (open('generated-solutions.json', 'r') as solutions_file,
          open('generated-solutions-nd.json', 'r') as non_dominated_file):
        solutions = json.load(solutions_file)
        non_dominated = json.load(non_dominated_file)
        check_domination(non_dominated, solutions)
    for t in range(Constants.NUM_GENERATIONS):
        with (open(Constants.RUN_FOLDER + '/arch2-' + str(t) + '-parent-pop.json', 'r') as parent_pop_file,
              open(Constants.RUN_FOLDER + '/arch2-' + str(t) + '-non-dominated.json', 'r') as non_dominated_file):
            parent_pop = json.load(parent_pop_file)
            non_dominated = json.load(non_dominated_file)
            check_budget(parent_pop)
            check_domination(non_dominated, parent_pop)
    print('passes validation!!')


if __name__ == '__main__':
    main()
