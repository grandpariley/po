import json

from po.pkg.data import keys, count, fetch
from po.pkg.problem.discrete_domain import DiscreteDomain
from po.pkg.problem.problem import problem_encoder_fn
from po.pkg.random.random import Random
from po.pkg.problem.compare import dominates
from po.pkg.consts import Constants
from math import floor


def individual_encoder_fn(obj):
    if not isinstance(obj, Individual):
        return obj
    return json.JSONDecoder().decode(json.JSONEncoder(default=problem_encoder_fn).encode(obj.problem))


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
        return str(individual_encoder_fn(self))

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

    async def swap_half_genes(self, other):
        if self.problem.combination_strategy:
            self.problem.combination_strategy(self.problem, other.problem)
            return
        variables = set()
        while len(variables) < len(self.problem.keys()) / 2:
            variables.add(Random.random_choice(other.problem.keys()))
        for v in variables:
            await self.safe_set_value(v, other.problem.get_value(v))

    async def safe_set_value(self, v, new_value):
        if not new_value:
            return
        original = self.problem.get_value(v)
        self.problem.set_value(v, new_value)
        if not self.problem.consistent():
            if original:
                self.problem.set_value(v, original)
            else:
                self.problem.reset_value(v)

    async def get_new_value(self, random_variable):
        if random_variable in self.problem.variables.keys():
            new_value = self.problem.variables[random_variable].domain.get_random()
        else:
            new_value = DiscreteDomain(
                floor(Constants.BUDGET / (await fetch(random_variable))['price']),
                1
            ).get_random()
        return new_value

    async def emo_phase(self):
        for _ in range(
                Random.random_int_between_a_and_b(0, floor(Constants.GENES_MUTATING * await count()))):
            random_variable = Random.random_choice(await keys())
            await self.safe_set_value(random_variable, await self.get_new_value(random_variable))

    def get_objective_values(self):
        return self.problem.objective_values()
