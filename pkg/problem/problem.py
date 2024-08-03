import json.encoder
from math import floor

from pkg.consts import Constants
from pkg.problem.constraint import constraint_encoder_fn
from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.variable import Variable, variable_encoder_fn


def problem_encoder_fn(obj):
    if not isinstance(obj, Problem):
        return obj
    return {
        "variables": json.JSONDecoder().decode(json.JSONEncoder(default=variable_encoder_fn).encode(obj.variables)),
        "constraints": json.JSONDecoder().decode(json.JSONEncoder(default=constraint_encoder_fn).encode(obj.constraints)),
        "objectives": list(obj.objective_values())
    }


class Problem:
    def __init__(self, variables, constraints, objective_funcs):
        self.variables = variables
        self.constraints = constraints
        self.objective_funcs = objective_funcs

    def __str__(self):
        return str(problem_encoder_fn(self))

    def __repr__(self):
        return str(self)

    def consistent(self):
        for constraint in self.constraints:
            if not constraint.holds(self.variables):
                return False
        return True

    def set_value(self, variable_index, value, info=None):
        if variable_index not in self.variables.keys() and info is not None:
            self.variables[variable_index] = Variable(
                DiscreteDomain(floor(Constants.BUDGET / info.price), 0.00), info)
        self.variables[variable_index].set_value(value)

    def get_value(self, variable_index):
        if variable_index in self.keys():
            return self.variables[variable_index].get_value()
        return None

    def keys(self):
        return list(self.variables.keys())

    def objective_values(self):
        if self.objective_funcs is None:
            return None
        return tuple([obj_func(self.variables) for obj_func in self.objective_funcs])
