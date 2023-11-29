from pkg.consts import Constants
from pkg.problem.compare import euclidean_distance


def euclidean_distance_mapping(individuals):
    b = []
    for i in range(len(individuals)):
        b.append([])
        for j in range(len(individuals)):
            b[i].append((j, euclidean_distance(individuals[i], individuals[j])))
        sorted(b[i], key=lambda k: k[1])
        b[i] = b[i][:Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS]
    return [[j[0] for j in b[i]] for i in range(len(b))]
