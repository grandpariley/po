import json

from pkg.consts import Constants


def check_domination(non_dominated, parent_population):
    for nd in range(len(non_dominated)):
        for p in range(len(parent_population)):
            if non_dominated[nd]['objectives'] == parent_population[p]['objectives']:
                continue
            if all([non_dominated[nd]['objectives'][i] >= parent_population[p]['objectives'][i] for i in range(len(non_dominated[nd]['objectives']))]) \
                    and any([non_dominated[nd]['objectives'][i] > parent_population[p]['objectives'][i] for i in range(len(non_dominated[nd]['objectives']))]):
                continue
            print('DOMINATION FAILED FOR ' + str(nd) + ' vs ' + str(p))


def check_budget(solutions, data, print_all=False):
    total_spent = 0
    for s in range(len(solutions)):
        for key, value in solutions[s]['variables'].items():
            total_spent += value * data[key]['price']
        if print_all:
            print('solution ' + str(s) + ' spent $' + str(total_spent) + ' which is ' + ('UNDER' if Constants.BUDGET >= total_spent else 'OVER') + ' budget')
        # if Constants.BUDGET < total_spent:
        #     raise ValueError('SOLUTION ' + str(s) + ' IS OVER BUDGET: ' + str(total_spent))


def main():
    # for t in range(Constants.NUM_GENERATIONS):
    for t in range(1):
        with (open('run-2024-08-03 16:24:29.124061/arch2-' + str(t) + '-parent-pop.json', 'r') as parent_pop_file,
          open('run-2024-08-03 16:24:29.124061/arch2-' + str(t) + '-non-dominated.json', 'r') as non_dominated_file,
          open('data.json', 'r') as data_file):
            parent_pop = json.load(parent_pop_file)
            non_dominated = json.load(non_dominated_file)
            data = json.load(data_file)
            print('checking population budget constraint')
            check_budget(parent_pop, data, print_all=True)
            print('checking non-dominated budget constraint')
            check_budget(non_dominated, data, print_all=True)
            print('checking domination')
            check_domination(non_dominated, parent_pop)


if __name__ == '__main__':
    main()
