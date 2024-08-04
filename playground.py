import json
from math import ceil

from pkg.consts import Constants

FOLDER = 'run-2024-08-04 12:16:58.297320'


def check_domination(non_dominated, parent_population):
    for nd in range(len(non_dominated)):
        for p in range(len(parent_population)):
            if non_dominated[nd]['objectives'] == parent_population[p]['objectives']:
                continue
            if all([non_dominated[nd]['objectives'][i] >= parent_population[p]['objectives'][i] for i in
                    range(len(non_dominated[nd]['objectives']))]) \
                    and any([non_dominated[nd]['objectives'][i] > parent_population[p]['objectives'][i] for i in
                             range(len(non_dominated[nd]['objectives']))]):
                continue
            print('DOMINATION FAILED FOR ' + str(nd) + ' vs ' + str(p))


def check_budget(solutions):
    for s in range(len(solutions)):
        total_spent = 0
        for key, value in solutions[s]['variables'].items():
            total_spent += value * Constants.DATA[key]['price']
        if ceil(Constants.BUDGET) < total_spent:
            raise ValueError('SOLUTION ' + str(s) + ' IS OVER BUDGET: ' + str(total_spent))


def main():
    for t in range(Constants.NUM_GENERATIONS):
        with (open(FOLDER + '/arch2-' + str(t) + '-parent-pop.json', 'r') as parent_pop_file,
              open(FOLDER + '/arch2-' + str(t) + '-non-dominated.json', 'r') as non_dominated_file):
            parent_pop = json.load(parent_pop_file)
            non_dominated = json.load(non_dominated_file)
            print('checking population budget constraint')
            check_budget(parent_pop)
            print('checking domination')
            check_domination(non_dominated, parent_pop)


if __name__ == '__main__':
    main()
