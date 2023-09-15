from pkg.consts import Constants
from pkg.problem.compare import euclidean_distance
from pkg.sort.sort import sort, default_partition


def euclidean_distance_mapping(individuals):
    b = []
    for i in range(len(individuals)):
        b.append([])
        for j in range(len(individuals)):
            b[i].append((j, euclidean_distance(individuals[i].get_objective_values(), individuals[j].get_objective_values())))
        sort(b[i], 0, len(b[i]) - 1, default_partition(lambda k: k[1]))
        b[i] = b[i][:Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS]
    return [[j[0] for j in b[i]] for i in range(len(b))][:Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS]
