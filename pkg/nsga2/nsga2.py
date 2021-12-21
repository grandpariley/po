from pkg.consts import Constants
from pkg.log import Log
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_by_crowding_distance, sort_individuals
from pkg.problem.solver import Solver
from pkg.random.random import Random


def fast_non_dominated_sort(individuals):
    if not individuals:
        return
    for p in individuals:
        p.reset_domination_count()
        for q in individuals:
            if q.does_dominate(p):
                p.increment_dominated()


def crowding_distance_assignment(individuals):
    if not individuals:
        return
    for o in range(len(individuals[0].get_objective_values())):
        individuals = sort_individuals(individuals, o)
        individuals[0].set_crowding_distance(float('inf'))
        individuals[-1].set_crowding_distance(float('inf'))
        denominator = individuals[0].get_objective_values()[o] - individuals[-1].get_objective_values()[o]
        if denominator == 0.0:
            for i in range(1, len(individuals) - 1):
                individuals[i].set_crowding_distance(float('inf'))
        else:
            for i in range(1, len(individuals) - 1):
                numerator = individuals[i + 1].get_objective_values()[o] - individuals[i - 1].get_objective_values()[o]
                individuals[i].set_crowding_distance(individuals[i].get_crowding_distance() + (numerator / denominator))
    return individuals


def get_children(mum, dad):
    daughter = Individual(individual=mum)
    son = Individual(individual=dad)
    son.swap_half_genes(mum)
    daughter.swap_half_genes(dad)
    return son, daughter


def assign_tournament_probabilities(individuals):
    individuals = sort_by_crowding_distance(individuals)
    for i in range(len(individuals)):
        individuals[i].set_inverse_tournament_rank(len(individuals) - i)
    return individuals


def get_tournament_pool(individuals):
    individuals = assign_tournament_probabilities(individuals)
    population_pool = []
    for i in range(len(individuals)):
        for _ in range(individuals[i].get_inverse_tournament_rank()):
            population_pool.append(individuals[i])
    return population_pool


def get_parents(parent_population):
    tournament_pool = get_tournament_pool(parent_population)
    mum = Random.random_choice(tournament_pool)
    dad = Random.random_choice(tournament_pool)
    return mum, dad


def generate_children(parent_population):
    children = []
    while len(children) < len(parent_population):
        mum, dad = get_parents(parent_population)
        son, daughter = get_children(mum, dad)
        son.emo_phase()
        daughter.emo_phase()
        children += [son, daughter]
    return children


def fill_parent_population(sorted_population):
    parent_population = []
    rank = 0
    while True:
        sorting_group = []
        for i in sorted_population:
            if i.get_domination_count() == rank:
                sorting_group.append(i)
        if len(parent_population + sorting_group) < Constants.NSGA2_NUM_INDIVIDUALS:
            parent_population += sorting_group
            rank += 1
        elif len(parent_population + sorting_group) == Constants.NSGA2_NUM_INDIVIDUALS:
            parent_population += sorting_group
            break
        else:
            crowding_distance_assigned = crowding_distance_assignment(sorting_group)
            parent_population += sort_by_crowding_distance(
                crowding_distance_assigned
            )[Constants.NSGA2_NUM_INDIVIDUALS - len(parent_population):-1]
            break
        return parent_population


def solve_helper(parent_population):
    for _ in range(Constants.NSGA2_NUM_GENERATIONS):
        child_population = generate_children(parent_population)
        sorted_population = set(parent_population + child_population)
        fast_non_dominated_sort(sorted_population)
        parent_population = fill_parent_population(sorted_population)
    fast_non_dominated_sort(parent_population)
    front = []
    for i in parent_population:
        if i.get_domination_count() == 0:
            front.append(i)
    return front


class Nsga2(Solver):

    def solve(self):
        Constants.NSGA2_NUM_INDIVIDUALS = len(self.problems)
        Log.begin_debug("nsga2")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population)
        Log.end_debug()
        return solutions
