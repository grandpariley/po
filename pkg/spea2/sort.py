from pkg.problem.compare import dominates


def sort(population, low, high, partition):
    if low < high:
        i = partition(population, low, high)
        sort(population, low, i, partition)
        sort(population, i + 1, high, partition)


def sort_population_by_domination(population):
    def partition(pop, low, high):
        i = low - 1
        pivot = pop[high].get_objective_values()
        for j in range(low, high):
            if dominates(pop[j].get_objective_values(), pivot):
                i += 1
                pop[high], pop[j] = pop[j], pop[high]
        i += 1
        pop[high], pop[i] = pop[i], pop[high]
        return i

    sort(population, 0, len(population) - 1, partition)
    return population
