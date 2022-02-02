from pkg.nsga2.sort import sort_by_crowding_distance


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
