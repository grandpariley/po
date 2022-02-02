def sort(individuals, low, high, partition):
    if low < high:
        i = partition(individuals, low, high)
        sort(individuals, low, i, partition)
        sort(individuals, i + 1, high, partition)


def default_partition(getter):
    def partition(individuals, low, high):
        i = low - 1
        pivot = getter(individuals[high])
        for j in range(low, high):
            if getter(individuals[j]) < pivot:
                i += 1
                individuals[high], individuals[j] = individuals[j], individuals[high]
        i += 1
        individuals[high], individuals[i] = individuals[i], individuals[high]
        return i

    return partition


def sort_individuals(individuals, obj_index):
    partition = default_partition(lambda i: i.get_objective_values()[obj_index])
    sort(individuals, 0, len(individuals) - 1, partition)
    return individuals


def sort_by_crowding_distance(individuals):
    partition = default_partition(lambda i: i.get_crowding_distance())
    sort(individuals, 0, len(individuals) - 1, partition)
    return individuals


def sort_by_special_crowding_distance(individuals):
    partition = default_partition(lambda i: i.get_special_crowding_distance())
    sort(individuals, 0, len(individuals) - 1, partition)
    return individuals


def fast_non_dominated_sort(individuals):
    if not individuals:
        return
    for p in individuals:
        p.reset_domination_count()
        for q in individuals:
            if q.does_dominate(p):
                p.increment_dominated()
    return individuals
