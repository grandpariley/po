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


def get_b(parent_population):
    input_b = []
    for i in range(len(parent_population)):
        input_b.append([])
        for _ in range(len(parent_population[i].get_objective_values())):
            input_b[i].append(1.00 / len(parent_population[i].get_objective_values()))
    b = euclidean_distance_mapping(input_b)
    return b


def solve_helper(parent_population, data):
    ep = set()
    b = get_b(parent_population)
    for t in range(Constants.MOEAD_NUM_GENERATIONS):
        for i in range(len(parent_population)):
            y = generate_child(parent_population, b[i], data)
            parent_population.append(y)
            neighbourhood = [parent_population[index] for index in b[i]]
            for n in neighbourhood:
                if y.does_dominate(n):
                    parent_population.remove(n)
                elif n.does_dominate(y):
                    parent_population.remove(y)
                    break
            b = get_b(parent_population)
            refresh_ep(ep, y)
    return list(ep)


class Moead(Solver):

    def solve(self):
        Log.begin_debug("moead")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population, self.data)
        Log.end_debug()
        return [s.problem for s in solutions]
