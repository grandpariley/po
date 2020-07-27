import copy
from pkg.problem.solver import Solver
from pkg.consts import Constants


class Spea2(Solver):
    # TODO
    def calculate_fitness(self, population):
        pass

    # TODO
    def get_non_dominated(self, population):
        return [], []

    # TODO
    def truncate(self, population):
        return []

    # TODO
    def binary_tournament_selection(self, population):
        return []

    def solve_helper(self, population, archive, generation):
        self.calculate_fitness(population)
        self.calculate_fitness(archive)
        non_dominated, dominated = self.get_non_dominated(population + archive)
        new_archive = copy.deepcopy(non_dominated)
        while len(new_archive) != Constants.SPEA2_MAX_ARCHIVE_SIZE:
            if len(new_archive) > Constants.SPEA2_MAX_ARCHIVE_SIZE:
                new_archive = self.truncate(new_archive)
            elif len(new_archive) < Constants.SPEA2_MAX_ARCHIVE_SIZE:
                new_archive = new_archive + dominated
        generation += 1
        if generation == Constants.SPEA2_MAX_GENERATIONS:
            return self.get_non_dominated(new_archive)[0]
        return self.solve_helper(self.binary_tournament_selection(population), new_archive, generation)

    def solve(self):
        return self.problem
