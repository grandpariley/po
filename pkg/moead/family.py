from po.pkg.moead.individual import Individual
from po.pkg.random.random import Random


def generate_child(dating_pool):
    mum, dad = get_parents(dating_pool)
    son = Individual(individual=dad)
    son.swap_half_genes(mum)
    son.emo_phase()
    return son


def get_parents(dating_pool):
    index_mum = Random.random_int_between_a_and_b(0, len(dating_pool) - 1)
    index_dad = index_mum
    while index_mum == index_dad:
        index_dad = Random.random_int_between_a_and_b(0, len(dating_pool) - 1)
    return (
        dating_pool[index_mum],
        dating_pool[index_dad]
    )
