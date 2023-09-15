from pkg.consts import Constants
from pkg.moead.individual import Individual
from pkg.random.random import Random


def generate_child(parent_population, b, data):
    mum, dad = get_parents(parent_population, b)
    son = Individual(individual=dad)
    son.swap_half_genes(mum, data)
    return son


def get_parents(parent_population, b):
    return (parent_population[Random.random_int_between_a_and_b(0, len(b) - 1)],
            parent_population[Random.random_int_between_a_and_b(0,
                                                                Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS if Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS < len(
                                                                    b) - 1 else len(b) - 1)])
