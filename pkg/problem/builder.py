from copy import deepcopy
from math import ceil, floor

from po.pkg.data import fetch, keys
from po.pkg.log import Log
from po.progress import ProgressBar
from po.pkg.consts import Constants
from po.pkg.problem.constraint import Constraint
from po.pkg.problem.problem import Problem
from po.pkg.random.random import Random


def default_portfolio_optimization_problem_arch_2():
    return Problem(
        {},
        [Constraint(under_budget, 'budget')],
        [
            get_objective_by_criteria('cvar'),
            get_objective_by_criteria('var'),
            get_objective_by_criteria('return'),
            get_objective_by_criteria('environment'),
            get_objective_by_criteria('governance'),
            get_objective_by_criteria('social')
        ],
        combination_strategy=portfolio_optimization_combination_strategy
    )


def default_portfolio_optimization_problem_arch_1(investor):
    return default_portfolio_optimization_problem_arch_1(get_weights(investor))


def default_portfolio_optimization_problem_by_weights(weights):
    return Problem(
        {},
        [Constraint(under_budget, 'budget')],
        [get_weight_sensitive_objective(weights)],
        combination_strategy=portfolio_optimization_combination_strategy
    )


def under_budget(variables):
    return budget_used(variables) <= Constants.BUDGET


def budget_used(variables):
    total_spent = 0
    for key, variable in variables.items():
        total_spent += variable.get_value() * variable.objective_info['price']
    return total_spent


def get_weights(investor):
    for i in Constants.INVESTORS:
        if i['person'] == investor:
            return i['weights']
    return 0


def get_weight_sensitive_objective(weights):
    return lambda options: sum([
        get_objective_by_criteria('cvar')(options) * weights['cvar'],
        get_objective_by_criteria('var')(options) * weights['var'],
        get_objective_by_criteria('return')(options) * weights['return'],
        get_objective_by_criteria('environment')(options) * weights['environment'],
        get_objective_by_criteria('governance')(options) * weights['governance'],
        get_objective_by_criteria('social')(options) * weights['social']
    ])


def get_objective_by_criteria(criteria):
    return lambda variables: objective_value(variables, criteria)


def objective_value(variables, criteria):
    total = 0
    for key, value in variables.items():
        Log.log("key: " + str(key) + " value: " + str(value) + " criteria: " + str(criteria) + " info: " + str(value.objective_info))
        total += value.get_value() * value.objective_info[criteria]
    return total


def portfolio_optimization_combination_strategy(child, parent):
    for name, variable in parent.variables.items():
        new_value = variable.get_value()
        if child.get_value(name) is not None:
            new_value += child.get_value(name)
        child.set_value(name, new_value, info=parent.variables[name].objective_info)
    halve_solution(child, list(child.variables.keys()))
    refill(child)


def halve_solution(child, variables_keys):
    for name in variables_keys:
        consistent_value = floor(child.get_value(name) / 2)
        if consistent_value:
            child.set_value(name, consistent_value)
        else:
            child.reset_value(name)


def refill(child):
    variables_keys = list(child.variables.keys())
    spent = budget_used(child.variables)
    while len(variables_keys) > 0:
        name = Random.random_choice(variables_keys)
        variables_keys.remove(name)
        if child.variables[name].objective_info['price'] < (Constants.BUDGET - spent):
            child.set_value(name, child.get_value(name) + 1)
            spent = budget_used(child.variables)


async def generate_solutions_discrete_domain(problem):
    solutions = []
    ProgressBar.begin(Constants.NUM_INDIVIDUALS)
    while len(solutions) < Constants.NUM_INDIVIDUALS:
        solutions.append(await get_new_solution(deepcopy(problem)))
        Log.log("created solution: " + str(len(solutions)) + " / " + str(Constants.NUM_INDIVIDUALS))
        ProgressBar.update(len(solutions))
    ProgressBar.end()
    return solutions


async def get_new_solution(solution):
    current_budget = Constants.BUDGET
    possible_variables = await keys()
    while len(possible_variables) > 0 and current_budget > Constants.BUDGET * (1 - Constants.BUDGET_UTILIZATION):
        rand_variable_index = Random.random_choice(possible_variables)
        possible_variables.remove(rand_variable_index)
        info = await fetch(rand_variable_index)
        domain = [i for i in range(1, floor(current_budget / info['price']))]
        if len(domain) == 0:
            continue
        new_value = Random.random_choice(domain)
        current_budget -= new_value * info['price']
        if current_budget > Constants.BUDGET:
            current_budget += new_value * info['price']
            continue
        solution.set_value(rand_variable_index, new_value, info=info)
    return solution
