from pkg.problem.compare import dominates

def sort(population, low, high, partition):
    if low < high:
        i = partition(population, low, high)
        sort(population, low, i, partition)
        sort(population, i + 1, high, partition)

def sort_population_by_domination(population):
    def partition(population, low, high):
        i = low - 1
        pivot = population[high].get_objective_values()
        for j in range(low, high):
            if dominates(population[j].get_objective_values(), pivot):
                i += 1
                population[high], population[j] = population[j], population[high]
        i += 1
        population[high], population[i] = population[i], population[high]
        return i
    sort(population, 0, len(population) - 1, partition)
    return population