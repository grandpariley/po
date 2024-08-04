from copy import deepcopy
from math import ceil

from progress import ProgressBar
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
            get_objective_by_criteria('cvar', minimize=True),
            get_objective_by_criteria('var', minimize=True),
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
    for key, variable in variables.items():
        total_spent += variable.get_value() * variable.objective_info['price']
    return total_spent <= Constants.BUDGET


def weight(investor, criteria):
    for i in Constants.INVESTORS:
        if i['person'] == investor:
            return i['weights'][criteria]
    return 0


def get_weight_sensitive_objective(investor):
    return lambda options: sum([
        get_objective_by_criteria('cvar', minimize=True)(options) * weight(investor, 'cvar'),
        get_objective_by_criteria('var', minimize=True)(options) * weight(investor, 'var'),
        get_objective_by_criteria('return')(options) * weight(investor, 'return'),
        get_objective_by_criteria('environment')(options) * weight(investor, 'environment'),
        get_objective_by_criteria('governance')(options) * weight(investor, 'governance'),
        get_objective_by_criteria('social')(options) * weight(investor, 'social')
    ])


def get_objective_by_criteria(criteria, minimize=False):
    return lambda variables: objective_value(variables, criteria, minimize)


def objective_value(variables, criteria, minimize):
    total = 0
    for key, value in variables.items():
        total += value.get_value() * value.objective_info[criteria]
    return total if not minimize else -total


def generate_solutions_discrete_domain(problem):
    solutions = []
    ProgressBar.begin(Constants.NUM_INDIVIDUALS)
    while len(solutions) < Constants.NUM_INDIVIDUALS:
        solutions.append(get_new_solution(deepcopy(problem)))
        ProgressBar.update(len(solutions))
    ProgressBar.end()
    return solutions


def get_new_solution(solution):
    current_budget = Constants.BUDGET
    possible_variables = list(Constants.DATA.keys())
    while len(possible_variables) > 0:
        rand_variable_index = Random.random_choice(possible_variables)
        possible_variables.remove(rand_variable_index)
        domain = [i for i in range(1, ceil(current_budget / Constants.DATA[rand_variable_index]['price']))]
        if len(domain) == 0:
            continue
        new_value = Random.random_choice(domain)
        current_budget -= new_value * Constants.DATA[rand_variable_index]['price']
        solution.set_value(rand_variable_index, new_value, info=Constants.DATA[rand_variable_index])
    return solution
