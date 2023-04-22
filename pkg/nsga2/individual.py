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

    def swap_half_genes(self, other, data):
        variables = [Random.random_int_between_a_and_b(0, len(self.problem.keys()) - 1) for _ in
                     range(floor(len(self.problem.keys()) / 2))]
        for v in variables:
            if self.problem.get_value(v) != other.problem.get_value(v):
                original = self.problem.get_value(v)
                self.problem.set_value(v, other.problem.get_value(v), data[v])
                if not self.problem.consistent():
                    self.problem.set_value(v, original)
                original = other.problem.get_value(v)
                other.problem.set_value(v, self.problem.get_value(v), data[v])
                if not other.problem.consistent():
                    other.problem.set_value(v, original)

    def emo_phase(self, data):
        for _ in range(Random.random_int_between_a_and_b(0, floor(Constants.NSGA2_NUM_GENES_MUTATING * len(data.keys())))):
            random_variable = Random.random_choice(list(data.keys()))
            self.problem.set_value(random_variable, self.get_new_value(data, random_variable), data[random_variable])

    def get_new_value(self, data, random_variable):
        if random_variable in self.problem.variables.keys():
            new_value = self.problem.variables[random_variable].domain.get_random()
        else:
            new_value = DiscreteDomain(floor(Constants.BUDGET / data[random_variable].price), 0.00).get_random()
        return new_value
