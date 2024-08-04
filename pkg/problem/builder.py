from copy import deepcopy
from math import floor

from pkg.consts import Constants
from pkg.log import Log
from pkg.problem.constraint import Constraint
from pkg.problem.problem import Problem
from pkg.random.random import Random


def default_portfolio_optimization_problem_arch_2():
    return Problem(
        {},
        [Constraint(under_budget)],
        [
            get_objective_by_criteria('cvar'),
            get_objective_by_criteria('var'),
            get_objective_by_criteria('return'),
            get_objective_by_criteria('environment'),
            get_objective_by_criteria('governance'),
            get_objective_by_criteria('social')
        ]
    )


def default_portfolio_optimization_problem_arch_1(investor):
    return Problem(
        {},
        [Constraint(under_budget)],
        [get_weight_sensitive_objective(investor)]
    )


def under_budget(variables):
    total_spent = 0
    for key, value in variables.items():
        total_spent += value * value.objective_info[key]['price']
    return total_spent <= Constants.BUDGET


def weight(investor, criteria):
    for i in Constants.INVESTORS:
        if i['person'] == investor:
            return i['weights'][criteria]
    return 0


def get_weight_sensitive_objective(investor):
    return lambda options: sum([
        get_objective_by_criteria('cvar')(options) * weight(investor, 'cvar'),
        get_objective_by_criteria('var')(options) * weight(investor, 'var'),
        get_objective_by_criteria('return')(options) * weight(investor, 'return'),
        get_objective_by_criteria('environment')(options) * weight(investor, 'environment'),
        get_objective_by_criteria('governance')(options) * weight(investor, 'governance'),
        get_objective_by_criteria('social')(options) * weight(investor, 'social')
    ])


def get_objective_by_criteria(criteria):
    return lambda variables: objective_value(variables, criteria)


def objective_value(variables, criteria):
    total = 0
    for key, value in variables.items():
        total += value.get_value() * value.objective_info[criteria]
    return total


def generate_solutions_discrete_domain(population_size, portfolio_options, problem):
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


def get_new_solution(data, problem):
    solution = deepcopy(problem)
    current_budget = Constants.BUDGET
    possible_variables = list(data.keys())
    while len(possible_variables) > 0:
        rand_variable_index = Random.random_choice(possible_variables)
        possible_variables.remove(rand_variable_index)
        domain = [i for i in range(floor(current_budget / data[rand_variable_index]['price']))]
        if len(domain) == 0:
            continue
        new_value = Random.random_choice(domain)
        current_budget -= new_value * data[rand_variable_index]['price']
        solution.set_value(rand_variable_index, new_value, data[rand_variable_index])
    return solution
