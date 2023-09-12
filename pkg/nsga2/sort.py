from pkg.sort.sort import default_partition, sort


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
