from pkg.consts import Constants
from pkg.moead.individual import Individual
from pkg.random.random import Random


def generate_children(parent_population, b, data):
    children, mum, dad = [], None, None
    while len(children) < len(parent_population):
        mum, dad = get_parents(parent_population, b)
        son, daughter = get_children(mum, dad, data)
        children += [son, daughter]
    return children


def get_parents(parent_population, b):
    return (parent_population[Random.random_int_between_a_and_b(0, len(b) - 1)],
            parent_population[Random.random_int_between_a_and_b(0, Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS)])


def get_children(mum, dad, data):
    daughter = Individual(individual=mum)
    son = Individual(individual=dad)
    son.swap_half_genes(mum, data)
    daughter.swap_half_genes(dad, data)
    return son, daughter

