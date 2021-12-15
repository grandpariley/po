from pkg.consts import Constants
from pkg.log import Log
from pkg.nsga2.individual import Individual
from pkg.nsga2.sort import sort_by_crowding_distance, sort_individuals
from pkg.problem.builder import generate_many_random_solutions
from pkg.problem.solver import Solver
from pkg.random.random import Random
from pkg.problem.builder import stock_names


def fast_non_dominated_sort_front(individuals, rank):
    front = []
    for p in individuals:
        for q in individuals:
            if p.does_dominate(q):
                p.add_dominated(q)
            elif q.does_dominate(p):
                p.increment_dominated()
        if not p.is_dominated():
            p.set_rank(rank)
            front.append(p)
    return front


def fast_non_dominated_sort(individuals):
    first_front = fast_non_dominated_sort_front(individuals, 0)
    front = [first_front]
    front_count = 0
    while front[front_count] and sum(len(f) for f in front) < len(individuals):
        next_front = fast_non_dominated_sort_front(front[front_count], front_count + 1)
        front.append(next_front)
        front_count += 1
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
    def solve_helper(self, parent_population):
        for _ in range(Constants.NSGA2_NUM_GENERATIONS):
            child_population = generate_children(parent_population)
            front = fast_non_dominated_sort(set(parent_population + child_population))
            parent_population = []
            i = 0
            while i < len(front) and len(parent_population) + len(front[i]) < Constants.NSGA2_NUM_INDIVIDUALS:
                parent_population += front[i]
                i += 1
            if i < len(front):
                front[i] = crowding_distance_assignment(front[i])
                parent_population += sort_by_crowding_distance(front[i])[Constants.NSGA2_NUM_INDIVIDUALS - len(parent_population):-1]
            
        front = fast_non_dominated_sort(parent_population)
        return [individual.get_problem() for individual in front[0]]

    def solve(self):
        problems = generate_many_random_solutions(self.problem, Constants.NSGA2_NUM_INDIVIDUALS)
        self.print_problems(problems)
        Log.begin_debug("nsga2")
        parent_population = [Individual(problem=p) for p in problems]
        solns = self.solve_helper(parent_population)
        Log.end_debug()
        return solns

    def print_problems(self, problems):
        print("Problems: ")
        for p in problems:
            print("\trisk: " + str(p.objective_values()[0]))
            print("\treward: " + str(p.objective_values()[1]))
            print("\tbudget: " + str(sum([s.get_value() * s.get_objective_info()['price'] for s in p.variables])))
            for i in range(len(stock_names)):
                print("\t\t" + stock_names[i] + ": " + str(p.variable_assignments()[i]))
            print()
