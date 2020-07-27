def sort(individuals, low, high, partition):
    if low < high:
        i = partition(individuals, low, high)
        sort(individuals, low, i, partition)
        sort(individuals, i + 1, high, partition)


def sort_individuals(individuals, obj_index):
    def partition(individuals, low, high):
        i = low - 1
        pivot = individuals[high].get_objective_values()[obj_index]
        for j in range(low, high):
            if individuals[j].get_objective_values()[obj_index] <= pivot:
                i += 1
                individuals[high], individuals[j] = individuals[j], individuals[high]
        i += 1
        individuals[high], individuals[i] = individuals[i], individuals[high]
        return i
    sort(individuals, 0, len(individuals) - 1, partition)
    return individuals


def sort_by_crowding_distance(individuals):
    def partition(individuals, low, high):
        i = low - 1
        pivot = individuals[high].get_crowding_distance()
        for j in range(low, high):
            if individuals[j].get_crowding_distance() <= pivot:
                i += 1
                individuals[high], individuals[j] = individuals[j], individuals[high]
        i += 1
        individuals[high], individuals[i] = individuals[i], individuals[high]
        return i
    sort(individuals, 0, len(individuals) - 1, partition)
    return individuals
