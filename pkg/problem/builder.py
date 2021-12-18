from copy import deepcopy
from math import floor

from pkg.client.stock_client import stock_names, default_stock_data
from pkg.consts import Constants
from pkg.problem.constraint import Constraint
from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.random.random import Random


def default_portfolio_optimization_problem():
    def convert_stock_data_to_variable(vsd):
        return Variable(DiscreteDomain([i for i in range(floor(float(Constants.BUDGET) / vsd['price']))], 0), vsd)

    budget_constraint = Constraint(tuple(i for i in range(len(stock_names))), lambda vsds: Constants.BUDGET > sum(
        [(0.0 if vsd.get_value() is None else vsd.get_value()) * vsd.objective_info['price'] for vsd in vsds]))

    def risk_objective(vsds):
        return -sum(
            [(1.0 if vsd.get_value() is None else vsd.get_value()) * vsd.objective_info['risk'] for vsd in vsds]
        )

    def reward_objective(vsds):
        return sum(
            [(1.0 if vsd.get_value() is None else vsd.get_value()) * vsd.objective_info['reward'] for vsd in vsds]
        )

    stock_data = default_stock_data()
    return Problem(
        [convert_stock_data_to_variable(stock_data[vsd]) for vsd in stock_data],
        [budget_constraint],
        [risk_objective, reward_objective]
    )


def trim_for_remaining_budget(problem, v):
    p = deepcopy(problem)
    new_domain = []
    for d in p.variables[v].domain:
        p.set_value(v, d)
        if p.consistent():
            new_domain.append(d)
    return new_domain


def generate_solutions_discrete_domain(problem, population_size):
    solutions = set()
    give_up = False
    while not give_up and len(solutions) < population_size:
        solution = deepcopy(problem)
        for v in range(solution.num_variables()):
            d = trim_for_remaining_budget(solution, v)
            if len(d) == 0:
                give_up = True
                break
            new_value = Random.random_choice(d)
            solution.set_value(v, new_value)
        if not give_up:
            solutions.add(solution)
    return solutions
