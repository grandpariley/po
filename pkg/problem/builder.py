from copy import deepcopy
from math import floor

from pkg.client.stock_client import stock_names, default_stock_data
from pkg.consts import Constants
from pkg.problem.constraint import Constraint
from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable


def default_portfolio_optimization_problem():
    def convert_stock_data_to_variable(vsd):
        return Variable(DiscreteDomain([i for i in range(floor(float(Constants.BUDGET) / vsd['price']))], 0), vsd)

    budget_constraint = Constraint(tuple(i for i in range(len(stock_names))), lambda vsds: Constants.BUDGET > sum(
        [(0.0 if vsd.get_value() is None else vsd.get_value()) * vsd.get_objective_info()['price'] for vsd in vsds]))

    risk_objective = lambda vsds: -sum(
        [(1.0 if vsd.get_value() is None else vsd.get_value()) * vsd.get_objective_info()['risk'] for vsd in vsds]
    )

    reward_objective = lambda vsds: sum(
        [(1.0 if vsd.get_value() is None else vsd.get_value()) * vsd.get_objective_info()['reward'] for vsd in vsds]
    )

    stock_data = default_stock_data()
    return Problem(
        [convert_stock_data_to_variable(stock_data[vsd]) for vsd in stock_data],
        [budget_constraint],
        [risk_objective, reward_objective]
    )


def generate_many_random_solutions(problem, population_size):
    individuals = set()
    give_up = 0
    while len(individuals) < population_size and give_up < Constants.GIVE_UP_MAX:
        p = deepcopy(problem)
        for v in range(p.num_variables()):
            p.set_value(v, p.get_random_from_variable(v))
        if p.consistent() and p.variable_assignments() not in [i.variable_assignments() for i in individuals]:
            individuals.add(p)
        else:
            give_up += 1
    return list(individuals)


def generate_solutions_discrete_domain(problem, population_size):
    solutions = set()
    while len(solutions) < population_size:
        solution = deepcopy(problem)
        for v in range(solution.num_variables()):
            for d in solution.get_domain(v):
                if solution.will_be_consistent(v, d):
                    solution.set_value(v, d)
        solutions.add(solution)
