from pkg.moead.individual import Individual
from pkg.moead.sort import euclidean_distance_mapping
from pkg.problem.tests.default_problems import default_consistent_problem_set_values, default_consistent_problem


def default_individual():
    return Individual(problem=default_consistent_problem_set_values())


def default_b():
    input_b = []
    for i in range(len(default_individuals())):
        input_b.append([])
        for _ in range(len(default_individuals()[i].get_objective_values())):
            input_b[i].append(1.00 / len(default_individuals()[i].get_objective_values()))
    return euclidean_distance_mapping(input_b)


def default_individuals():
    individuals = []
    for i in range(4):
        individual = default_individual()
        individual.problem.set_value("0", i)
        individual.problem.set_value("1", i + 1)
        individual.problem.set_value("2", i + 1)
        individuals.append(individual)
    return individuals


def default_other_dominating_individual():
    problem = default_consistent_problem()
    problem.set_value("0", 1)
    problem.set_value("1", 3)
    problem.set_value("2", 1)
    individual = Individual(problem=problem)
    return individual


def default_dominating_individual():
    problem = default_consistent_problem()
    problem.set_value("0", 1)
    problem.set_value("1", 2)
    problem.set_value("2", 1)
    individual = Individual(problem=problem)
    return individual


def default_dominated_individual():
    problem = default_consistent_problem()
    problem.set_value("0", 1)
    problem.set_value("1", 0)
    problem.set_value("2", 1)
    individual = Individual(problem=problem)
    return individual


def default_individual_with_values():
    problem = default_consistent_problem()
    problem.set_value("0", 1)
    problem.set_value("1", 1)
    problem.set_value("2", 1)
    individual = Individual(problem=problem)
    return individual

def get_test_data():
    return {
        "0": {},
        "1": {},
        "2": {}
    }
