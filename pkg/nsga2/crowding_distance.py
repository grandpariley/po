from pkg.nsga2.sort import sort_individuals, sort_by_special_crowding_distance


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
    average_crowding_distance_decision_space = sum([i.get_crowding_distance() for i in individuals][1:-1]) / len(
        individuals)
    for i in individuals:
        i.set_average_crowding_distance_decision_space(average_crowding_distance_decision_space)


def special_crowding_distance_assignment(population):
    population_crowding_distance_assignment(population)
    for p in population:
        front = get_all_with_rank(population, p.get_domination_count())
        crowding_distance_assignment(front)
    average_crowding_distance_object_space = sum([i.get_population_crowding_distance() for i in population][1:-1]) / \
                                             len(population)
    for p in population:
        if p.get_crowding_distance() > p.get_average_crowding_distance_decision_space() or p.get_population_crowding_distance() > average_crowding_distance_object_space:
            p.set_special_crowding_distance(max(p.get_crowding_distance(), p.get_population_crowding_distance()))
        else:
            p.set_special_crowding_distance(min(p.get_crowding_distance(), p.get_population_crowding_distance()))
    sort_by_special_crowding_distance(population)


def population_crowding_distance_assignment(population):
    for o in range(len(population[0].get_objective_values())):
        population = sort_individuals(population, o)
        population[0].set_population_crowding_distance(float('inf'))
        population[-1].set_population_crowding_distance(float('inf'))
        denominator = population[0].get_objective_values()[o] - population[-1].get_objective_values()[o]
        if denominator == 0.0:
            for i in range(1, len(population) - 1):
                population[i].set_population_crowding_distance(float('inf'))
        else:
            for i in range(1, len(population) - 1):
                numerator = population[i + 1].get_objective_values()[o] - population[i - 1].get_objective_values()[o]
                population[i].set_population_crowding_distance(
                    population[i].get_population_crowding_distance() + (numerator / denominator))


def get_all_with_rank(population, rank):
    front = []
    for p in population:
        if p.get_domination_count() == rank:
            front.append(p)
    return front
