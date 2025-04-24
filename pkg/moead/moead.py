import asyncio
import json
import os

import db
from po.pkg.consts import Constants
from po.pkg.log import Log
from po.pkg.moead.family import generate_child
from po.pkg.moead.individual import Individual, individual_encoder_fn
from po.pkg.moead.sort import euclidean_distance_mapping
from po.pkg.problem.solver import Solver
from po.progress import ProgressBar


def is_non_dominated(x, population):
    for individual in population:
        if individual.does_dominate(x):
            return False
    return True


def get_non_dominated(population):
    nd = set()
    for individual in population:
        if is_non_dominated(individual, population):
            nd.add(individual)
    return list(nd)


def get_neighbourhood(parent_population, neighbourhood_indexes):
    return [parent_population[index] for index in neighbourhood_indexes]


async def save_generation(tag, generation, non_dominated_solutions):
    await db.save_generation(tag, generation, list(map(individual_encoder_fn, non_dominated_solutions)))


async def solve_helper(tag, parent_population):
    Log.log('Euclidean distance mapping...')
    b = euclidean_distance_mapping(parent_population)
    Log.log('Euclidean distance mapping complete! Starting solving...')
    ProgressBar.begin(Constants.NUM_GENERATIONS)
    for t in range(Constants.NUM_GENERATIONS):
        Log.log("Generation: " + str(t) + "/" + str(Constants.NUM_GENERATIONS) + " started with length " + str(len(parent_population)))
        for i in range(len(parent_population)):
            neighbourhood = get_neighbourhood(parent_population, b[i])
            y = await generate_child(neighbourhood)
            if is_non_dominated(y, neighbourhood):
                parent_population[i] = y
        await save_generation(tag, str(t), get_non_dominated(parent_population))
        ProgressBar.update(t)
    ProgressBar.end()
    solution = get_non_dominated(parent_population)
    Log.log('Solving complete! Solution has length ' + str(len(solution)))
    return solution


class Moead(Solver):

    async def solve(self):
        Log.begin_debug("moead")
        parent_population = [Individual(problem=p) for p in self.problems]
        solutions = await solve_helper(self.tag, parent_population)
        Log.end_debug()
        return [s.problem for s in solutions]
