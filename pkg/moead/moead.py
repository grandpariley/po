from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.family import generate_child
from pkg.moead.individual import Individual
from pkg.moead.sort import euclidean_distance_mapping
from pkg.problem.solver import Solver


def get_best_value_all_objectives(population):
    z = []
    for individual in population:
        for o in range(len(individual.problem.objective_values())):
            if not (0 <= o < len(z)):
                z.append(0)
            if z[o] < individual.problem.objective_values()[o]:
                z[o] = individual.problem.objective_values()[o]
    return z


def get_dominated(ep, l):
    d = []
    for e in ep:
        if l.does_dominate(e):
            d.append(e)
    return d


def refresh_ep(ep, y):
    dominated_by_y = get_dominated(ep, y)
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
    for t in range(Constants.NSGA2_NUM_GENERATIONS):
        y = generate_child(parent_population, b, data)
        parent_population.append(y)
        b = euclidean_distance_mapping(parent_population)
        refresh_ep(ep, y)
    return list(ep)


class Moead(Solver):

    def solve(self):
        Constants.MOEAD_NUM_INDIVIDUALS = len(self.problems)
        Log.begin_debug("moead")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population, self.data)
        Log.end_debug()
        return [s.problem for s in solutions]
