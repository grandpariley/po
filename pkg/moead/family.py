from pkg.moead.individual import Individual
from pkg.random.random import Random


def generate_child(parent_population, data):
    mum, dad = get_parents(parent_population)
    son = Individual(individual=dad)
    son.swap_half_genes(mum, data)
    son.emo_phase(data)
    return son


def get_parents(parent_population):
    index_mum = Random.random_int_between_a_and_b(0, len(parent_population) - 1)
    index_dad = index_mum
    while index_mum == index_dad:
        index_dad = Random.random_int_between_a_and_b(0, len(parent_population) - 1)
    return (
        parent_population[index_mum],
        parent_population[index_dad]
    )
