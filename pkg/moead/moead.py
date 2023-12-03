from copy import deepcopy

from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.family import generate_child
from pkg.moead.individual import Individual
from pkg.moead.sort import euclidean_distance_mapping
from pkg.problem.solver import Solver


def refresh_ep(ep, y):
    dominated_by_y = []
    for e in ep:
        if y.does_dominate(e):
            dominated_by_y.append(e)
    ep = ep.difference(dominated_by_y)
    ep.add(y)
    for e in ep:
        if e.does_dominate(y):
            ep.remove(y)
            break


def solve_helper(parent_population, data):
    ep = set()
    Log.log("timestamp")
    b = euclidean_distance_mapping(parent_population)
    Log.log("timestamp")
    x = deepcopy(parent_population)
    for t in range(Constants.NUM_GENERATIONS):
        Log.log("Generation: " + str(t))
        for i in range(len(parent_population)):
            y = generate_child(parent_population, data)
            x.append(y)
            neighbourhood = [parent_population[index] for index in b[i]]
            for n in neighbourhood:
                if n not in x:
                    continue
                if y.does_dominate(n):
                    x.remove(n)
                elif n.does_dominate(y):
                    x.remove(y)
                    break
            x = list(set(x))
            refresh_ep(ep, y)
    return list(ep)


class Moead(Solver):

    def solve(self):
        Log.begin_debug("moead")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population, self.data)
        Log.end_debug()
        return [s.problem for s in solutions]
