from pkg.log import Log
from pkg.moead.individual import Individual
from pkg.random.random import Random


def generate_child(parent_population, bi, data):
    mum, dad = get_parents(parent_population, bi)
    son = Individual(individual=dad)
    son.swap_half_genes(mum, data)
    Log.log("---> str(son == dad) " + str(son == dad))
    return son


def get_parents(parent_population, bi):
    index_mum = Random.random_choice(bi)
    index_dad = index_mum
    while index_mum == index_dad:
        index_dad = Random.random_choice(bi)
    return (
        parent_population[index_mum],
        parent_population[index_dad]
    )
