import json
from math import ceil

from pkg.consts import Constants


def check_budget(solutions):
    for s in range(len(solutions)):
        total_spent = 0
        for key, value in solutions[s]['variables'].items():
            total_spent += value * Constants.DATA[key]['price']
        if ceil(Constants.BUDGET) < total_spent:
            raise ValueError('SOLUTION ' + str(s) + ' IS OVER BUDGET: ' + str(total_spent))


def main():
    for t in range(Constants.NUM_RUNS):
        with (open('arch2/' + str(t) + '/solutions.json', 'r') as arch2_solutions_file,
              open('arch1/' + str(t) + '/solutions.json', 'r') as arch1_solutions_file):
            arch2_solutions = json.load(arch2_solutions_file)
            arch1_solutions = json.load(arch1_solutions_file)
            check_budget(arch2_solutions)
            check_budget(arch1_solutions)
    print('passes validation!!')


if __name__ == '__main__':
    main()
