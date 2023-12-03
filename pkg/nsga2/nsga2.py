from pkg.consts import Constants
from pkg.log import Log
from pkg.nsga2.family import generate_children, fill_parent_population_traditional
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import fast_non_dominated_sort
from pkg.problem.solver import Solver


def solve_helper(parent_population, data):
    for generation in range(Constants.NUM_GENERATIONS):
        Log.log("Generation: " + str(generation))
        child_population = generate_children(parent_population, data)
        sorted_population = set(parent_population + child_population)
        sorted_population = fast_non_dominated_sort(sorted_population)
        parent_population = fill_parent_population_traditional(list(set(sorted_population)))
    fast_non_dominated_sort(parent_population)
    front = []
    for i in parent_population:
        if i.get_domination_count() == 0:
            front.append(i)
    return front


class Nsga2(Solver):

    def solve(self):
        Constants.NSGA2_NUM_INDIVIDUALS = len(self.problems)
        Log.begin_debug("nsga2")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = solve_helper(parent_population, self.data)
        Log.end_debug()
        return [s.problem for s in solutions]
