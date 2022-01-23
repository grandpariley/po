from pkg.consts import Constants
from pkg.log import Log
from pkg.nsga2.family import generate_children, fill_parent_population_traditional
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_individuals, fast_non_dominated_sort
from pkg.nsga2.tournament import get_traditional_tournament_pool
from pkg.problem.solver import Solver


def crowding_distance_assignment(individuals):
    if not individuals:
        return
    for o in range(len(individuals[0].get_objective_values())):
        individuals = sort_individuals(individuals, o)
        individuals[0].set_crowding_distance(float('inf'))
        individuals[-1].set_crowding_distance(float('inf'))
        denominator = individuals[0].get_objective_values()[o] - individuals[-1].get_objective_values()[o]
        if denominator == 0.0:
            for i in range(1, len(individuals) - 1):
                individuals[i].set_crowding_distance(float('inf'))
        else:
            for i in range(1, len(individuals) - 1):
                numerator = individuals[i + 1].get_objective_values()[o] - individuals[i - 1].get_objective_values()[o]
                individuals[i].set_crowding_distance(individuals[i].get_crowding_distance() + (numerator / denominator))
    return individuals


def solve_helper(parent_population):
    for _ in range(Constants.NSGA2_NUM_GENERATIONS):
        child_population = generate_children(parent_population, get_traditional_tournament_pool)
        sorted_population = set(parent_population + child_population)
        sorted_population = fast_non_dominated_sort(sorted_population)
        parent_population = fill_parent_population_traditional(set(sorted_population), crowding_distance_assignment)
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
        solutions = solve_helper(parent_population)
        Log.end_debug()
        return [s.problem for s in solutions]
