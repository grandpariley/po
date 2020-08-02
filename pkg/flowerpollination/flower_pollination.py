from pkg.problem.solver import Solver
from pkg.flowerpollination.flower import Flower
from pkg.flowerpollination.bouquet import Bouquet
from pkg.problem.builder import generate_many_random_solutions
from pkg.consts import Constants


class FlowerPollination(Solver):
    def solve_helper(self, bouquet):
        bouquet.calculate_best()
        for _ in range(Constants.FP_MAX_GENERATIONS):
            for f in range(bouquet.num_flowers()):
                bouquet.pollinate(f)
            bouquet.calculate_best()
        return [flower.get_problem() for flower in bouquet.get_best()]

    def solve(self):
        return self.solve_helper(Bouquet([Flower(p) for p in generate_many_random_solutions(self.problem, Constants.FP_NUMBER_OF_FLOWERS)]))
