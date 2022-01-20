from pkg.consts import Constants
from pkg.log import Log
from pkg.moboa.bayesian_network import BayesianNetwork
from pkg.moboa.individual import Individual
from pkg.problem.solver import Solver


def filter_populations(parent_population, child_population):
    return list(set(child_population + parent_population))[:Constants.MOBOA_NUM_INDIVIDUALS]


def get_promising(population):
    promising = []
    for p in population:
        for q in population:
            if p.does_dominate(q):
                promising.append(p)
            elif q.does_dominate(p):
                promising.append(q)
    return promising


def solve_helper(parent_population):
    for _ in range(Constants.MOBOA_NUM_GENERATIONS):
        promising = get_promising(parent_population)
        network = BayesianNetwork(promising)
        network.generate()
        child_population = network.get_children()
        parent_population = filter_populations(parent_population, child_population)
    return parent_population


class Moboa(Solver):

    def solve(self):
        Constants.MOBOA_NUM_INDIVIDUALS = len(self.problems)
        Log.begin_debug("moboa")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population)
        Log.end_debug()
        return solutions
