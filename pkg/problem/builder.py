import copy
from pkg.random.random import Random
from pkg.problem.problem import Problem
from pkg.client.stock_client import StockClient


def default_portfolio_optimization_problem():
    # TODO
    def convert_stock_data_to_variable(stock_data):
        pass
    
    # TODO
    def get_budget_constraint():
        pass
    
    # TODO
    def get_risk_objective():
        pass
    
    # TODO
    def get_reward_objective():
        pass
    
    return Problem([convert_stock_data_to_variable(vsd) for vsd in StockClient().get_stock_data()], [get_budget_constraint()], [get_risk_objective(), get_reward_objective()])


def generate_many_random_solutions(problem, populationSize):
    individuals = set()
    while len(individuals) < populationSize:
        p = copy.deepcopy(problem)
        while not p.consistent():
            for v in range(p.num_variables()):
                p.set_value(v, Random.random_choice(p.get_domain(v)))
        if p.variable_assignments() not in [i.variable_assignments() for i in individuals]:
            individuals.add(p)
    return individuals
