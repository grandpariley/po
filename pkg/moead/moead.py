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
    for d in dominated_by_y:
        ep.remove(d)
    ep.add(y)
    for e in ep:
        if e.does_dominate(y):
            ep.remove(y)
            break


def solve_helper(parent_population, data):
    ep = set()
    b = euclidean_distance_mapping(parent_population)
    p = set(parent_population)
    previous_p = p
    for t in range(Constants.MOEAD_NUM_GENERATIONS):
        Log.log("generation " + str(t) + " | " + str(len(b)) + " | " + str(len(parent_population)) + " | " + str(
            previous_p == p))
        for i in range(len(b)):
            y = generate_child(list(p), b[i], data)
            Log.log("---> str(y in p) " + str(y in p) + " | " + str(b[i]))
            p.add(y)
            b = euclidean_distance_mapping(list(p))
            refresh_ep(ep, y)
    return list(ep)


class Moead(Solver):

    def solve(self):
        Log.begin_debug("moead")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population, self.data)
        Log.end_debug()
        return [s.problem for s in solutions]
