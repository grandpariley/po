import json

from pkg.consts import Constants


def check_domination(non_dominated, parent_population):
    for nd in non_dominated:
        for p in parent_population:
            if nd['objectives'] == p['objectives']:
                continue
            if all([nd['objectives'][i] >= p['objectives'][i] for i in range(len(nd['objectives']))]) \
                    and any([nd['objectives'][i] > p['objectives'][i] for i in range(len(nd['objectives']))]):
                continue
            raise ValueError('DOMINATION FAILED FOR ' + str(nd) + ' vs ' + str(p))


def check_budget(solutions, data, print_all=False):
    total_spent = 0
    for s in solutions:
        for key, value in s['variables'].items():
            total_spent += value * data[key]['price']
        if print_all:
            print('solution ' + str(s) + ' spent $' + str(total_spent))
        if Constants.BUDGET < total_spent:
            raise ValueError('SOLUTION ' + str(s) + ' IS OVER BUDGET: ' + str(total_spent))


def main():
    for t in range(Constants.NUM_GENERATIONS):
        with (open('run-2024-08-03 13:32:31.092658/arch2-' + str(t) + '-parent-pop.json', 'r') as parent_pop_file,
              open('run-2024-08-03 13:32:31.092658/arch2-' + str(t) + '-non-dominated.json', 'r') as non_dominated_file,
              open('data.json', 'r') as data_file):
            parent_pop = json.load(parent_pop_file)
            non_dominated = json.load(non_dominated_file)
            data = json.load(data_file)
            print('checking population budget constraint')
            check_budget(parent_pop, data)
            print('checking non-dominated budget constraint')
            check_budget(non_dominated, data, print_all=True)
            print('checking domination')
            check_domination(non_dominated, parent_pop)


if __name__ == '__main__':
    main()
