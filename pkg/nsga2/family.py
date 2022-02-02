from pkg.consts import Constants
from pkg.nsga2.crowding_distance import crowding_distance_assignment, special_crowding_distance_assignment
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_by_crowding_distance
from pkg.nsga2.tournament import get_tournament_pool
from pkg.random.random import Random


def get_children(mum, dad):
    daughter = Individual(individual=mum)
    son = Individual(individual=dad)
    son.swap_half_genes(mum)
    daughter.swap_half_genes(dad)
    return son, daughter


def get_parents(parent_population, improved):
    tournament_pool = get_tournament_pool(parent_population)
    if improved:
        gf1 = Random.random_choice(tournament_pool)
        gf2 = Random.random_choice(tournament_pool)
        mum = compare_partners(gf1, gf2)
        bf1 = Random.random_choice(tournament_pool)
        bf2 = Random.random_choice(tournament_pool)
        dad = compare_partners(bf1, bf2)
    else:
        mum = Random.random_choice(tournament_pool)
        dad = Random.random_choice(tournament_pool)
    return mum, dad


def compare_partners(partner1, partner2):
    if partner1.get_inverse_tournament_rank() > partner2.get_inverse_tournament_rank() or (
            partner1.get_inverse_tournament_rank() == partner2.get_inverse_tournament_rank() and
            get_scd(partner1) > get_scd(partner2)
    ):
        return partner1
    return partner2


# TODO
def get_scd(individual):
    return 0


def generate_children(parent_population, improved=False):
    children, mum, dad = [], None, None
    while len(children) < len(parent_population):
        mum, dad = get_parents(parent_population, improved)
        son, daughter = get_children(mum, dad)
        son.emo_phase()
        daughter.emo_phase()
        children += [son, daughter]
    return children


def fill_parent_population_traditional(sorted_population):
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


def fill_parent_population_improved(sorted_population):
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
            special_crowding_distance_assignment(sorting_group, sorted_population)
            parent_population += sort_by_crowding_distance(
                sorting_group
            )[Constants.NSGA2_NUM_INDIVIDUALS - len(parent_population):-1]
            break
    return parent_population
