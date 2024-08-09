from pkg.consts import Constants
from pkg.problem.compare import euclidean_distance
from progress import ProgressBar


def euclidean_distance_mapping(individuals):
    b = []
    ProgressBar.begin(len(individuals) * len(individuals))
    for i in range(len(individuals)):
        b.append([])
        for j in range(len(individuals)):
            b[i].append(
                (j, euclidean_distance(individuals[i].get_objective_values(), individuals[j].get_objective_values()))
            )
            ProgressBar.update((i * len(individuals)) + j)
        b[i] = sorted(b[i], key=lambda k: k[1])[:Constants.MOEAD_NUM_WEIGHT_VECTORS_T]
    ProgressBar.end()
    return [[j[0] for j in b[i]] for i in range(len(b))]
