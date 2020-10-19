from pkg.random.random import Random
from pkg.problem.solver import Solver
from pkg.consts import Constants
from pkg.spea2.sort import sort_population_by_domination
from pkg.spea2.individual import Individual
from pkg.problem.builder import generate_many_random_solutions
from pkg.problem.compare import get_dominated
from pkg.log import Log


def get_non_dominated(population):
    dominated = get_dominated(population)
    return list(set(population) - set(dominated)), dominated


def truncate_archive(population):
    population = sort_population_by_domination(population)
    return population[0:Constants.SPEA2_MAX_ARCHIVE_SIZE]


def assign_tournament_probabilities(population):
    population = sort_population_by_domination(population)
    for i in range(len(population)):
        population[i].set_inverse_tournament_rank(len(population) - i)
    return population


def get_tournament_pool(population):
    population = assign_tournament_probabilities(population)
    population_pool = []
    for i in range(len(population)):
        for _ in range(population[i].get_inverse_tournament_rank()):
            population_pool.append(population[i])
    return population_pool


def binary_tournament_selection(population):
    tournament_pool = get_tournament_pool(population)
    return [Random.random_choice(tournament_pool) for _ in range(Constants.SPEA2_INITIAL_POPULATION)]


def solve_helper(population, archive):
    for _ in range(Constants.SPEA2_MAX_GENERATIONS):
        population = binary_tournament_selection(population)
        non_dominated, dominated = get_non_dominated(archive + population)
        archive = non_dominated
        if len(archive) != Constants.SPEA2_MAX_ARCHIVE_SIZE:
            archive = truncate_archive(archive + dominated)
    return [individual.get_problem() for individual in get_non_dominated(archive)[0]]


class Spea2(Solver):

    def solve(self):
        Log.begin_debug("spea2")
        solns = solve_helper(
            [Individual(p) for p in generate_many_random_solutions(self.problem, Constants.SPEA2_INITIAL_POPULATION)],
            [])
        Log.end_debug()
        return solns
