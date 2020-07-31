import copy
from pkg.random.random import Random
from pkg.problem.problem import Problem

def default_portfolio_optimization_problem():
    return Problem([], [], None)


def generate_many_random_solutions(problem, populationSize):
    individuals = set()
    while len(individuals) < populationSize:
        p = copy.deepcopy(problem)
        while not p.consistent():
            for v in range(p.num_variables()):
                p.set_value(v, Random.random_choice(p.get_domain(v)))
        if p.variable_assignments() not in [i.variable_assignments() for i in individuals]:
            individuals.add(p)
    return individuals
