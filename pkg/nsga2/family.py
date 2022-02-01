from pkg.consts import Constants
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_by_crowding_distance
from pkg.random.random import Random


def get_children(mum, dad):
    daughter = Individual(individual=mum)
    son = Individual(individual=dad)
    son.swap_half_genes(mum)
    daughter.swap_half_genes(dad)
    return son, daughter


def get_parents(parent_population, get_tournament_pool):
    tournament_pool = get_tournament_pool(parent_population)
    mum = Random.random_choice(tournament_pool)
    dad = Random.random_choice(tournament_pool)
    return mum, dad


def generate_children(parent_population, get_tournament_pool):
    children = []
    while len(children) < len(parent_population):
        mum, dad = get_parents(parent_population, get_tournament_pool)
        son, daughter = get_children(mum, dad)
        son.emo_phase()
        daughter.emo_phase()
        children += [son, daughter]
    return children


def fill_parent_population_traditional(sorted_population, crowding_distance_assignment):
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


def fill_parent_population_improved(sorted_population, crowding_distance_assignment):
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
