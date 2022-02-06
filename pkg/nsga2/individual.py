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
            self.domination_count = 0
            self.crowding_distance = 0
            self.special_crowding_distance = 0
            self.population_crowding_distance = 0
            self.average_crowding_distance_decision_space = 0
            self.inverse_tournament_rank = 0
        elif individual is not None:
            self.problem = individual.problem
            self.domination_count = individual.domination_count
            self.crowding_distance = individual.crowding_distance
            self.special_crowding_distance = individual.special_crowding_distance
            self.population_crowding_distance = individual.population_crowding_distance
            self.average_crowding_distance_decision_space = individual.average_crowding_distance_decision_space
            self.inverse_tournament_rank = individual.inverse_tournament_rank

    def __str__(self):
        return str(self.problem) + "\tcrowding distance: " + str(self.crowding_distance) + \
               "\n\tdomination_count: " + str(self.domination_count) + "\n"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if self.problem.num_variables() != other.problem.num_variables():
            return False
        for i in range(self.problem.num_variables()):
            if self.problem.get_value(i) != other.problem.get_value(i):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str([self.problem.get_value(v) for v in range(self.problem.num_variables())]))

    def does_dominate(self, q):
        return dominates(self.problem.objective_values(), q.problem.objective_values())

    def increment_dominated(self):
        self.domination_count += 1

    def reset_domination_count(self):
        self.domination_count = 0

    def is_dominated(self):
        return self.domination_count != 0

    def get_domination_count(self):
        return self.domination_count

    def decrement_dominated(self):
        if self.domination_count > 0:
            self.domination_count -= 1

    def set_crowding_distance(self, crowding_distance):
        self.crowding_distance = crowding_distance

    def get_crowding_distance(self):
        return self.crowding_distance

    def set_special_crowding_distance(self, special_crowding_distance):
        self.special_crowding_distance = special_crowding_distance

    def get_special_crowding_distance(self):
        return self.special_crowding_distance

    def set_population_crowding_distance(self, population_crowding_distance):
        self.population_crowding_distance = population_crowding_distance

    def get_population_crowding_distance(self):
        return self.population_crowding_distance

    def set_average_crowding_distance_decision_space(self, average_crowding_distance_decision_space):
        self.average_crowding_distance_decision_space = average_crowding_distance_decision_space

    def get_average_crowding_distance_decision_space(self):
        return self.average_crowding_distance_decision_space

    def get_objective_values(self):
        return self.problem.objective_values()

    def set_inverse_tournament_rank(self, inverse_tournament_rank):
        self.inverse_tournament_rank = inverse_tournament_rank

    def get_inverse_tournament_rank(self):
        return self.inverse_tournament_rank

    def swap_half_genes(self, other):
        give_up = 0
        while give_up < Constants.NSGA2_GIVE_UP_MAX:
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
