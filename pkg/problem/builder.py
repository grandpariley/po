from copy import deepcopy
from math import floor
from pkg.random.random import Random
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint
from pkg.client.stock_client import StockClient, stock_names
from pkg.consts import Constants


def default_portfolio_optimization_problem():
    def convert_stock_data_to_variable(vsd):
        return Variable([i for i in range(floor(float(Constants.BUDGET) / vsd['price']))], vsd)
    
    def get_budget_constraint():
        return Constraint(tuple(i for i in range(len(stock_names))), lambda vsds: Constants.BUDGET > sum([vsd.get_value() * vsd.get_objective_info()['price'] for vsd in vsds]))
    
    def get_risk_objective():
        return lambda vsds: -sum([vsd.get_value() * vsd.get_objective_info()['risk'] for vsd in vsds])

    
    def get_reward_objective():
        return lambda vsds: sum([vsd.get_value() * vsd.get_objective_info()['reward'] for vsd in vsds])

    stock_data = StockClient().get_stock_data()
    thing = {sd: [str(key) + ": " + str(stock_data[sd][key]) for key in stock_data[sd]] for sd in stock_data}
    for t in thing:
        print(t)
        for j in thing[t]:
            print("\t" + str(j))
    return Problem([convert_stock_data_to_variable(stock_data[vsd]) for vsd in stock_data], [get_budget_constraint()], [get_risk_objective(), get_reward_objective()])


def generate_many_random_solutions(problem, population_size):
    individuals = set()
    while len(individuals) < population_size:
        p = deepcopy(problem)
        give_up = 0
        while not p.consistent() or give_up > population_size:
            give_up += 1
            for v in range(p.num_variables()):
                p.set_value(v, Random.random_choice(p.get_domain(v)))
        if p.consistent() and p.variable_assignments() not in [i.variable_assignments() for i in individuals]:
            individuals.add(p)
    return individuals
