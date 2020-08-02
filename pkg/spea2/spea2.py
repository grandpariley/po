from copy import deepcopy
from pkg.random.random import Random
from pkg.problem.solver import Solver
from pkg.consts import Constants
from pkg.spea2.sort import sort_population_by_domination
from pkg.spea2.individual import Individual
from pkg.problem.builder import generate_many_random_solutions
from pkg.problem.compare import dominates


class Spea2(Solver):
    def get_non_dominated(self, population):
        dominated = []
        for i in population:
            for j in population:
                if j not in dominated and dominates(i.get_objective_values(), j.get_objective_values()):
                    dominated.append(j)
                elif i not in dominated and dominates(j.get_objective_values(), i.get_objective_values()):
                    dominated.append(i)
        return list(set(population) - set(dominated)), dominated

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
            for _ in range(ppopulation_sizeet_inverse_tournament_rank()):
                population_pool.append(population[i])
        return population_pool

    def assign_tournament_probabilities(self, population):
        population = sort_population_by_domination(population)
        for i in range(len(population)):
            population[i].set_inverse_tournament_rank(len(population) - i)
        return population

    def solve_helper(self, population, archive, generation):
        if generation == Constants.SPEA2_MAX_GENERATIONS:
            return self.get_non_dominated(archive)[0]
        non_dominated, dominated = self.get_non_dominated(new_archive)
        new_archive = deepcopy(non_dominated)
        while len(new_archive) != Constants.SPEA2_MAX_ARCHIVE_SIZE:
            if len(new_archive) > Constants.SPEA2_MAX_ARCHIVE_SIZE:
                new_archive = self.truncate_archive(new_archive)
            elif len(new_archive) < Constants.SPEA2_MAX_ARCHIVE_SIZE:
                new_archive = new_archive + dominated
        return self.solve_helper(self.binary_tournament_selection(population), new_archive, generation + 1)

    def solve(self):
        return self.solve_helper([Individual(p) for p in generate_many_random_solutions(self.problem, Constants.SPEA2_INITIAL_POPULATION)], [], 0)
