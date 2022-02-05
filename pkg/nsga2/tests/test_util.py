from pkg.nsga2.individual import Individual
from pkg.problem.tests.default_problems import default_consistent_problem_set_values, default_consistent_problem


def default_individual():
    return Individual(problem=default_consistent_problem_set_values())


def default_individuals():
    individuals = [None for _ in range(4)]
    for i in range(4):
        individuals[i] = default_individual()
        individuals[i].problem.set_value(0, i)
        individuals[i].problem.set_value(1, i + 1)
        individuals[i].problem.set_value(2, i + 1)
    return individuals


def default_other_dominating_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 3)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(3)
    return individual


def default_dominating_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 2)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(2)
    return individual


def default_dominated_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 0)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(0)
    return individual


def default_individual():
    problem = default_consistent_problem()
    problem.set_value(0, 1)
    problem.set_value(1, 1)
    problem.set_value(2, 1)
    individual = Individual(problem=problem)
    individual.set_crowding_distance(1)
    return individual
