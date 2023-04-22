from copy import deepcopy
from math import floor

from pkg.consts import Constants
from pkg.log import Log
from pkg.parse.parse import parse_from_importer
from pkg.problem.constraint import Constraint
from pkg.problem.problem import Problem
from pkg.random.random import Random

GENERATED_SOLUTIONS_FILE = 'generated-solutions.json'


def var_objective(pos):
    return sum(
        [(0.0 if not pos[po].get_value() else pos[po].get_value()) * pos[po].objective_info.var for po in pos]
    )


def cvar_objective(pos):
    return sum(
        [(0.0 if not pos[po].get_value() else pos[po].get_value()) * pos[po].objective_info.cvar for po in pos]
    )


def return_objective(pos):
    return sum(
        [(0.0 if not pos[po].get_value() else pos[po].get_value()) * pos[po].objective_info.ret for po in pos]
    )


def environment_objective(pos):
    return sum(
        [(0.0 if not pos[po].get_value() else pos[po].get_value()) * pos[po].objective_info.environment for po in pos]
    )


def governance_objective(pos):
    return sum(
        [(0.0 if not pos[po].get_value() else pos[po].get_value()) * pos[po].objective_info.governance for po in pos]
    )


def social_objective(pos):
    return sum(
        [(0.0 if not pos[po].get_value() else pos[po].get_value()) * pos[po].objective_info.social for po in pos]
    )


def default_portfolio_optimization_problem():
    portfolio_options = parse_from_importer()
    budget_constraint = Constraint(
        None,
        lambda variables: Constants.BUDGET > sum(
            [(0.0 if variable.get_value() is None else variable.get_value()) * variable.objective_info.price for
             variable in variables.values()]
        ))
    return Problem(
        {},
        [budget_constraint],
        [var_objective, cvar_objective, return_objective, environment_objective, governance_objective, social_objective]
    ), portfolio_options


def generate_solutions_discrete_domain(problem, portfolio_options, population_size):
    solution_hashes = set()
    solutions = []
    while len(solution_hashes) < population_size:
        solution = get_new_solution(portfolio_options, problem)
        solution_hash = hash(solution)
        if solution_hash not in solution_hashes:
            solution_hashes.add(solution_hash)
            solutions.append(solution)
            Log.log(str(len(solution_hashes)) + " / " + str(population_size))
    return solutions


def get_new_solution(portfolio_options, problem):
    solution = deepcopy(problem)
    current_budget = Constants.BUDGET
    possible_variables = list(portfolio_options.keys())
    while len(possible_variables) > 0:
        domain, rand_variable_index = get_potential_variable_data(current_budget, portfolio_options, possible_variables)
        if len(domain) == 0:
            continue
        new_value = Random.random_normal(domain)
        current_budget -= new_value * portfolio_options[rand_variable_index].price
        solution.set_value(rand_variable_index, new_value, portfolio_options[rand_variable_index])
        if current_budget / Constants.BUDGET > Constants.BUDGET_UTILIZATION:
            break
    return solution


def get_potential_variable_data(current_budget, portfolio_options, possible_variables):
    rand_variable_index = Random.random_choice(possible_variables)
    possible_variables.remove(rand_variable_index)
    price = portfolio_options[rand_variable_index].price
    domain = get_max_domain(
        [i for i in range(floor(Constants.BUDGET / price))],
        price,
        current_budget
    )
    return domain, rand_variable_index


def get_max_domain(domain, price, budget_remaining):
    new_domain = []
    for d in domain:
        if d != 0 and (d * price) < budget_remaining:
            new_domain.append(d)
    return new_domain
