from pkg.nsga2.sort import sort_individuals


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
