from typing import Set, List, Any

from pkg.consts import Constants
from pkg.log import Log
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_by_crowding_distance, sort_individuals
from pkg.problem.builder import generate_many_random_solutions
from pkg.problem.solver import Solver
from pkg.random.random import Random


def fast_non_dominated_sort(individuals):
    first_front = set()
    for p in individuals:
        for q in individuals:
            if p.does_dominate(q):
                p.add_dominated(q)
            elif q.does_dominate(p):
                p.increment_dominated()
        if not p.is_dominated():
            p.set_rank(0)
            first_front.add(p)
    front_count = 0
    front = [first_front]
    while front[front_count] and len(front) < len(individuals):
        next_front = set()
        for p in front[front_count]:
            for q in p.get_dominates():
                q.decrement_dominated()
                if not q.is_dominated():
                    q.set_rank(front_count + 1)
                    next_front.add(q)
        front_count += 1
        front.append(next_front)
    return front


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


def get_children(mum, dad):
    daughter = Individual(individual=mum)
    son = Individual(individual=dad)
    son.swap_half_genes(mum)
    daughter.swap_half_genes(dad)
    return son, daughter


def assign_tournament_probabilities(individuals):
    individuals = sort_by_crowding_distance(individuals)
    for i in range(len(individuals)):
        individuals[i].set_inverse_tournament_rank(len(individuals) - i)
    return individuals


def get_tournament_pool(individuals):
    individuals = assign_tournament_probabilities(individuals)
    population_pool = []
    for i in range(len(individuals)):
        for _ in range(individuals[i].get_inverse_tournament_rank()):
            population_pool.append(individuals[i])
    return population_pool


def get_parents(parent_population):
    tournament_pool = get_tournament_pool(parent_population)
    mum = Random.random_choice(tournament_pool)
    dad = Random.random_choice(tournament_pool)
    return mum, dad


def generate_children(parent_population):
    children = []
    while len(children) < len(parent_population):
        mum, dad = get_parents(parent_population)
        son, daughter = get_children(mum, dad)
        son.emo_phase()
        daughter.emo_phase()
        children += [son, daughter]
    return children


class Nsga2(Solver):

    def solve_helper(self, parent_population, child_population):
        for j in range(Constants.NSGA2_NUM_GENERATIONS):
            front = fast_non_dominated_sort(parent_population + child_population)
            parent_population = []
            i = 0
            while i < len(front) and len(parent_population) + len(front[i]) < Constants.NSGA2_NUM_INDIVIDUALS:
                parent_population += front[i]
                i += 1
            if i < len(front):
                front[i] = crowding_distance_assignment(list(front[i]))
                parent_population += sort_by_crowding_distance(list(front[i]))[
                                     Constants.NSGA2_NUM_INDIVIDUALS - len(parent_population):-1]
            child_population = generate_children(parent_population)
        front = fast_non_dominated_sort(parent_population + child_population)
        return [individual.get_problem() for individual in set(front[0])]

    def solve(self):
        parent_population = [Individual(problem=p) for p in generate_many_random_solutions(
            self.problem, Constants.NSGA2_NUM_INDIVIDUALS)]
        Log.begin_debug("nsga2")
        solns = self.solve_helper(parent_population, [])
        Log.end_debug()
        return solns
