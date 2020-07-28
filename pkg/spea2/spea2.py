import copy
from pkg.random.random import Random
from pkg.problem.solver import Solver
from pkg.consts import Constants
from pkg.spea2.sort import sort_population_by_domination
from pkg.problem.compare import get_non_dominated


class Spea2(Solver):
    # TODO
    def calculate_fitness(self, population):
        pass

    def truncate_archive(self, population):
        population = sort_population_by_domination(population)
        return population[0:Constants.SPEA2_MAX_ARCHIVE_SIZE]

    def binary_tournament_selection(self, population):
        tournament_pool = self.get_tournament_pool(population)
        return [Random.random_choice(tournament_pool) for _ in range(Constants.SPEA2_INITIAL_POPULATION)]

    def get_tournament_pool(self, population):
        population = self.assign_tournament_probabilities(population)
        population_pool = []
        for i in range(len(population)):
            for _ in range(population[i].get_inverse_tournament_rank()):
                population_pool.append(population[i])
        return population_pool

    def assign_tournament_probabilities(self, population):
        population = sort_population_by_domination(population)
        for i in range(len(population)):
            population[i].set_inverse_tournament_rank(len(population) - i)
        return population

    def solve_helper(self, population, archive, generation):
        if generation == Constants.SPEA2_MAX_GENERATIONS:
            return get_non_dominated([individual.get_objective_values() for individual in archive])[0]
        self.calculate_fitness(population)
        self.calculate_fitness(archive)
        non_dominated, dominated = get_non_dominated([individual.get_objective_values() for individual in population + archive])
        new_archive = copy.deepcopy(non_dominated)
        while len(new_archive) != Constants.SPEA2_MAX_ARCHIVE_SIZE:
            if len(new_archive) > Constants.SPEA2_MAX_ARCHIVE_SIZE:
                new_archive = self.truncate_archive(new_archive)
            elif len(new_archive) < Constants.SPEA2_MAX_ARCHIVE_SIZE:
                new_archive = new_archive + dominated
        return self.solve_helper(self.binary_tournament_selection(population), new_archive, generation + 1)

    def solve(self):
        return self.problem
