import copy
import random
from pkg.problem.problem import Problem

def defaultPortfolioOptimizationProblem():
    return Problem([], [], None)

def generateManyRandomSolutions(problem, populationSize):
    individuals = set()
    while len(individuals) < populationSize:
        p = copy.deepcopy(problem)
        while not p.consistent():
            for v in range(p.num_variables()):
                p.set_value(v, random.choice(p.get_domain(v)))
        if p.variable_assignments() not in [i.variable_assignments() for i in individuals]:
            individuals.add(p)
    return individuals