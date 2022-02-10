from copy import deepcopy
from math import floor

from pkg.client.stock_client import stock_names, default_stock_data
from pkg.consts import Constants
from pkg.parse.parse import parse_from_importer
from pkg.problem.constraint import Constraint
from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.random.random import Random


def default_portfolio_optimization_problem():
    def convert_stock_data_to_variable(portfolio_option):
        return Variable(DiscreteDomain([i for i in range(floor(float(Constants.BUDGET) / portfolio_option.price))], 0),
                        portfolio_option)

    budget_constraint = Constraint(
        tuple(i for i in range(len(stock_names))),
        lambda variables: Constants.BUDGET > sum(
            [(0.0 if variable.get_value() is None else variable.get_value()) * variable.objective_info.price for
             variable in variables]
        ))

    def var_objective(pos):
        return sum(
            [(0.0 if po.get_value() is None else po.get_value()) * po.objective_info.var for po in pos]
        )

    def cvar_objective(pos):
        return sum(
            [(0.0 if po.get_value() is None else po.get_value()) * po.objective_info.cvar for po in pos]
        )

    def return_objective(pos):
        return sum(
            [(0.0 if po.get_value() is None else po.get_value()) * po.objective_info.ret for po in pos]
        )

    def environment_objective(pos):
        return sum(
            [(0.0 if po.get_value() is None else po.get_value()) * po.objective_info.environment for po in pos]
        )

    def governance_objective(pos):
        return sum(
            [(0.0 if po.get_value() is None else po.get_value()) * po.objective_info.governance for po in pos]
        )

    def social_objective(pos):
        return sum(
            [(0.0 if po.get_value() is None else po.get_value()) * po.objective_info.social for po in pos]
        )

    portfolio_options = parse_from_importer()
    return Problem(
        [convert_stock_data_to_variable(portfolio_option) for portfolio_option in portfolio_options],
        [budget_constraint],
        [var_objective, cvar_objective, return_objective, environment_objective, governance_objective, social_objective]
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
    while len(solutions) < population_size:
        solution = deepcopy(problem)
        for v in range(solution.num_variables()):
            d = trim_for_remaining_budget(solution, v)
            if len(d) == 0:
                break
            new_value = Random.random_choice(d)
            solution.set_value(v, new_value)
        solutions.add(solution)
    return solutions
