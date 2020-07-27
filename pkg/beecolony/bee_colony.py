from pkg.problem.solver import Solver
from pkg.consts import Constants
from pkg.beecolony.colony import Colony
from pkg.beecolony.bee import Bee
from pkg.problem.builder import generate_many_random_solutions


class BeeColony(Solver):
    def solve_helper(self, colony):
        for _ in range(Constants.BC_MAX_CYCLE_NUMBER):
            colony.assign_employed_bees()
            colony.send_onlooker_bees()
            colony.send_scout()
        return colony.get_solutions()

    def solve(self):
        return self.solve_helper(Colony([Bee(p) for p in generate_many_random_solutions(self.problem, Constants.BC_POPULATION_SIZE)]))
