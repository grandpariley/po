from pkg.consts import Constants
from pkg.moead.individual import Individual
from pkg.random.random import Random


def generate_child(parent_population, b, data):
    mum, dad = get_parents(parent_population, b)
    return get_child(mum, dad, data)


def get_parents(parent_population, b):
    return (parent_population[Random.random_int_between_a_and_b(0, len(b) - 1)],
            parent_population[Random.random_int_between_a_and_b(0, Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS)])


def get_child(mum, dad, data):
    son = Individual(individual=dad)
    son.swap_half_genes(mum, data)
    return son

