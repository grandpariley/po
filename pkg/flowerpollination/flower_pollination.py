import random
from pkg.problem.solver import Solver
from pkg.flowerpollination.flower import Flower
from pkg.flowerpollination.bouquet import Bouquet
from pkg.problem.builder import generateManyRandomSolutions
from pkg.consts import Constants

class FlowerPollination(Solver):
    def solve_helper(self, bouquet):
        bouquet.set_best()
        for _ in range(Constants.FP_MAX_GENERATIONS):
            bouquet.pollinate()
            bouquet.set_best()
        return bouquet.get_best()

    def solve(self):
        return self.solve_helper(Bouquet([Flower(p) for p in generateManyRandomSolutions(self.problem, Constants.FP_NUMBER_OF_FLOWERS)]))