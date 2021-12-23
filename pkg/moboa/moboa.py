from pkg.consts import Constants
from pkg.log import Log
from pkg.problem.solver import Solver


class Moboa(Solver):

    def solve(self):
        Constants.MOBOA_NUM_INDIVIDUALS = len(self.problems)
        Log.begin_debug("moboa")
        # parent_population = [Individual(problem=p) for p in self.problems]
        # solutions = solve_helper(parent_population)
        Log.end_debug()
        # return solutions
