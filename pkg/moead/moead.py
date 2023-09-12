from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.individual import Individual
from pkg.moead.sort import euclidean_distance_mapping
from pkg.problem.solver import Solver


def solve_helper(parent_population, data):
    ep = set()
    b = euclidean_distance_mapping(parent_population)[:Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS]
    for t in range(Constants.NSGA2_NUM_GENERATIONS):
        
    return parent_population


class Moead(Solver):

    def solve(self):
        Constants.MOEAD_NUM_INDIVIDUALS = len(self.problems)
        Log.begin_debug("moead")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population, self.data)
        Log.end_debug()
        return [s.problem for s in solutions]
