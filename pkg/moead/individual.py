from pkg.problem.discrete_domain import DiscreteDomain
from pkg.random.random import Random
from pkg.problem.compare import dominates
from pkg.consts import Constants
from math import floor


class Individual:
    def __init__(self, problem=None, individual=None):
        if problem is None and individual is None:
            raise ValueError("must have a problem or an individual")
        elif problem is not None and individual is not None:
            raise ValueError("must have one of a problem or an individual")
        if problem is not None:
            self.problem = problem
        elif individual is not None:
            self.problem = individual.problem

    def __str__(self):
        return str(self.problem) + "\n"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if len(self.problem.keys()) != len(other.problem.keys()):
            return False
        for k in self.problem.keys():
            if self.problem.get_value(k) != other.problem.get_value(k):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str([self.problem.get_value(v) for v in self.problem.keys()]))

    def does_dominate(self, q):
        return dominates(self.problem.objective_values(), q.problem.objective_values())

    def swap_half_genes(self, other, data):
        variables = set()
        while len(variables) < len(self.problem.keys()) / 2:
            variables.add(Random.random_int_between_a_and_b(0, len(self.problem.keys()) - 1))
        for v in variables:
            if self.problem.get_value(v) == other.problem.get_value(v):
                continue
            original = self.problem.get_value(v)
            self.problem.set_value(v, other.problem.get_value(v), data[v])
            if not self.problem.consistent():
                self.problem.set_value(v, original)

    def get_new_value(self, data, random_variable):
        if random_variable in self.problem.variables.keys():
            new_value = self.problem.variables[random_variable].domain.get_random()
        else:
            new_value = DiscreteDomain(floor(Constants.BUDGET / data[random_variable].price), 0.00).get_random()
        return new_value

    def get_objective_values(self):
        return self.problem.objective_values()
