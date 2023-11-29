

def sort_individuals(individuals, obj_index):
    return sorted(individuals, key=lambda i: i.get_objective_values()[obj_index])


def sort_by_crowding_distance(individuals):
    return sorted(individuals, key=lambda i: i.get_crowding_distance())


def sort_by_special_crowding_distance(individuals):
    return sorted(individuals, key=lambda i: i.get_special_crowding_distance())


def fast_non_dominated_sort(individuals):
    if not individuals:
        return
    for p in individuals:
        p.reset_domination_count()
        for q in individuals:
            if q.does_dominate(p):
                p.increment_dominated()
    return individuals
