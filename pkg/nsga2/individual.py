from copy import deepcopy
from pkg.random.random import Random
from pkg.problem.compare import dominates
from pkg.consts import Constants
from math import floor


def trim_for_remaining_budget(problem, v):
    p = deepcopy(problem)
    new_domain = []
    for d in p.variables[v].domain:
        p.set_value(v, d)
        if p.consistent():
            new_domain.append(d)
    return new_domain


class Individual:
    def __init__(self, problem=None, individual=None):
        if problem is None and individual is None:
            raise ValueError("must have a problem or an individual")
        elif problem is not None and individual is not None:
            raise ValueError("must have one of a problem or an individual")
        if problem is not None:
            self.problem = problem
            self.dominates = []
            self.domination_count = 0
            self.crowding_distance = 0
            self.inverse_tournament_rank = 0
            self.rank = None
        elif individual is not None:
            self.problem = individual.problem
            self.dominates = individual.dominates
            self.domination_count = individual.domination_count
            self.crowding_distance = individual.crowding_distance
            self.inverse_tournament_rank = individual.inverse_tournament_rank
            self.rank = individual.rank

    def __str__(self):
        return str(self.problem)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def does_dominate(self, q):
        return dominates(self.problem.objective_values(), q.problem.objective_values())

    def add_dominated(self, q):
        if q not in self.dominates:
            self.dominates.append(q)

    def get_dominates(self):
        return self.dominates

    def increment_dominated(self):
        self.domination_count += 1

    def set_rank(self, rank):
        self.rank = rank

    def is_dominated(self):
        return self.domination_count != 0

    def get_dominated(self):
        return self.dominates

    def get_problem(self):
        return self.problem

    def decrement_dominated(self):
        if self.domination_count > 0:
            self.domination_count -= 1

    def set_crowding_distance(self, crowding_distance):
        self.crowding_distance = crowding_distance

    def get_crowding_distance(self):
        return self.crowding_distance

    def get_objective_values(self):
        return self.problem.objective_values()

    def set_inverse_tournament_rank(self, inverse_tournament_rank):
        self.inverse_tournament_rank = inverse_tournament_rank

    def get_inverse_tournament_rank(self):
        return self.inverse_tournament_rank

    def swap_half_genes(self, other):
        give_up = 0
        while give_up < Constants.GIVE_UP_MAX:
            problem = deepcopy(self.problem)
            for _ in range(floor(problem.num_variables() / 2)):
                random_index = Random.random_int_between_a_and_b(
                    0, problem.num_variables() - 1)
                problem.set_value(
                    random_index, other.problem.get_value(random_index))
            if problem.consistent():
                self.problem = problem
                break
            else:
                give_up += 1

    def emo_phase(self):
        for _ in range(Constants.NSGA2_NUM_GENES_MUTATING):
            random_variable = Random.random_int_between_a_and_b(0, self.problem.num_variables() - 1)
            d = trim_for_remaining_budget(self.problem, random_variable)
            new_value = Random.random_choice(d)
            self.problem.set_value(random_variable, new_value)
