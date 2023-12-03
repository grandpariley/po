from math import floor

from pkg.consts import Constants
from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.variable import Variable


class Problem:
    def __init__(self, variables, constraints, objective_funcs):
        self.variables = variables
        self.constraints = constraints
        self.objective_funcs = objective_funcs

    def __str__(self):
        return "Problem: \n\tvariables: " + str([str(var) for var in self.variables]) + "\n\tconstraints: " + \
            str([str(con) for con in self.constraints]) + "\n\tobjective values: " + \
            str([str(obj) for obj in self.objective_values()]) + "\n"

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
