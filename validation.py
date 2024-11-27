import json
from math import ceil

from main import PROBLEMS
from po.pkg.consts import Constants
from po.pkg.data import fetch


def check_budget(solutions):
    for s in range(len(solutions)):
        total_spent = 0
        for key, value in solutions[s]['variables'].items():
            total_spent += value * fetch(key)['price']
        if ceil(Constants.BUDGET) < total_spent:
            raise ValueError('SOLUTION ' + str(s) + ' IS OVER BUDGET: ' + str(total_spent))


def main():
    for t in range(Constants.NUM_RUNS):
        for name in PROBLEMS.keys():
            with open(name + '/' + str(t) + '/solutions.json', 'r') as solutions_file:
                solutions = json.load(solutions_file)
                check_budget(solutions)
    print('passes validation!!')


if __name__ == '__main__':
    main()
