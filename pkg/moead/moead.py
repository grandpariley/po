from copy import deepcopy

from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.family import generate_child
from pkg.moead.individual import Individual
from pkg.moead.sort import euclidean_distance_mapping
from pkg.problem.solver import Solver


def is_non_dominated(y, neighbourhood):
    for n in neighbourhood:
        if n.does_dominate(y):
            return False
    return True


def get_non_dominated(x):
    nd = set()
    for i in range(len(x)):
        if is_non_dominated(x[i], x):
            nd.add(x[i])
    return list(nd)


def solve_helper(parent_population, data):
    Log.log("timestamp")
    b = euclidean_distance_mapping(parent_population)
    Log.log("timestamp")
    for t in range(Constants.NUM_GENERATIONS):
        Log.log("Generation: " + str(t))
        for i in range(len(parent_population)):
            y = generate_child([parent_population[i] for i in b[i]], data)
            neighbourhood = [parent_population[index] for index in b[i]]
            if is_non_dominated(y, neighbourhood):
                parent_population[i] = y
    return get_non_dominated(parent_population)


class Moead(Solver):

    def solve(self):
        Log.begin_debug("moead")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population, self.data)
        Log.end_debug()
        return [s.problem for s in solutions]
