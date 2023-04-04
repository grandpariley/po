import json
from copy import deepcopy
from math import floor
from pathlib import Path

from pkg.consts import Constants
from pkg.parse.parse import parse_from_importer
from pkg.problem.constraint import Constraint
from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.problem import Problem
from pkg.problem.variable import Variable
from pkg.random.random import Random

GENERATED_SOLUTIONS_FILE = 'generated-solutions.json'


def default_portfolio_optimization_problem():
    def var_objective(pos):
        return sum(
            [(0.0 if not po.get_value() else po.get_value()) * po.objective_info.var for po in pos]
        )

    def cvar_objective(pos):
        return sum(
            [(0.0 if not po.get_value() else po.get_value()) * po.objective_info.cvar for po in pos]
        )

    def return_objective(pos):
        return sum(
            [(0.0 if not po.get_value() else po.get_value()) * po.objective_info.ret for po in pos]
        )

    def environment_objective(pos):
        return sum(
            [(0.0 if not po.get_value() else po.get_value()) * po.objective_info.environment for po in pos]
        )

    def governance_objective(pos):
        return sum(
            [(0.0 if not po.get_value() else po.get_value()) * po.objective_info.governance for po in pos]
        )

    def social_objective(pos):
        return sum(
            [(0.0 if not po.get_value() else po.get_value()) * po.objective_info.social for po in pos]
        )

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


def generate_solutions_discrete_domain(problem, population_size):
    if not Path(GENERATED_SOLUTIONS_FILE).exists():
        solution_hashes = set()
        solutions = []
        with open(GENERATED_SOLUTIONS_FILE, 'a') as file:
            while len(solution_hashes) < population_size:
                solution = deepcopy(problem)
                current_budget = Constants.BUDGET
                possible_variables = [i for i in range(solution.num_variables())]
                while len(possible_variables) > 0:
                    rand_variable_index = Random.random_choice(possible_variables)
                    possible_variables.remove(rand_variable_index)
                    d = get_max_domain(
                        solution.variables[rand_variable_index].domain.values,
                        solution.variables[rand_variable_index].objective_info.price,
                        current_budget
                    )
                    if len(d) == 0:
                        break
                    new_value = Random.random_normal(d)
                    current_budget -= new_value * solution.variables[rand_variable_index].objective_info.price
                    solution.set_value(
                        rand_variable_index,
                        new_value
                    )
                solution_hash = hash(solution)
                if solution_hash not in solution_hashes:
                    solution_hashes.add(solution_hash)
                    solutions.append(solution)
                    print(str(len(solution_hashes)) + " / " + str(population_size))
            json.dump(solutions, file)
    with open(GENERATED_SOLUTIONS_FILE) as file:
        return json.load(file)


def get_max_domain(domain, price, budget_remaining):
    new_domain = []
    for d in domain:
        if d != 0 and (d * price) < budget_remaining:
            new_domain.append(d)
    return new_domain
