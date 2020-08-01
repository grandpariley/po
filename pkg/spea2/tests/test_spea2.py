import unittest
from copy import deepcopy
from pkg.spea2.spea2 import Spea2
from pkg.spea2.individual import Individual
from pkg.random.random import Random
from pkg.consts import Constants
from pkg.problem.tests.default_problems import default_consistent_problem, default_consistent_problem_set_values


class Spea2Test(unittest.TestCase):
    def default_individual(self):
        return Individual(default_consistent_problem_set_values())

    def test_get_non_dominated(self):
        spea2 = Spea2(default_consistent_problem())
        population = [None for _ in range(6)]
        for i in range(5):
            population[i] = self.default_individual()
            population[i].problem.set_value(0, i)
            population[i].problem.set_value(1, i + 1)
            population[i].problem.set_value(2, i + 1)
        population[5] = deepcopy(population[4])
        non_dominated, dominated = spea2.get_non_dominated(population)
        self.assertEqual(population[4:5], non_dominated)
        self.assertEqual(population[:4], dominated)

    def test_truncate(self):
        Constants.SPEA2_MAX_ARCHIVE_SIZE = 3
        spea2 = Spea2(default_consistent_problem())
        population = [None for _ in range(5)]
        for i in range(5):
            population[i] = self.default_individual()
            population[i].problem.set_value(0, i)
            population[i].problem.set_value(1, i + 1)
            population[i].problem.set_value(2, i + 1)
        archive = spea2.truncate_archive(population)
        formatted_population = [[i.problem.get_value(j) for j in range(i.problem.num_variables())] for i in population]
        formatted_archive = [[i.problem.get_value(j) for j in range(i.problem.num_variables())] for i in archive]
        self.assertEqual(formatted_population[:3], formatted_archive)

    def test_binary_tournament_selection(self):
        Random.begin_test()
        Constants.SPEA2_INITIAL_POPULATION = 4
        spea2 = Spea2(default_consistent_problem())
        population = [None for _ in range(5)]
        for i in range(5):
            population[i] = self.default_individual()
            population[i].problem.set_value(0, i)
            population[i].problem.set_value(1, i + 1)
            population[i].problem.set_value(2, i + 1)
        tournament_pool = spea2.get_tournament_pool(population)
        Random.set_test_value_for("random_choice", tournament_pool[0])
        Random.set_test_value_for("random_choice", tournament_pool[6])
        Random.set_test_value_for("random_choice", tournament_pool[11])
        Random.set_test_value_for("random_choice", tournament_pool[14])
        winners = spea2.binary_tournament_selection(population)
        self.assertEqual([tournament_pool[14], tournament_pool[11], tournament_pool[6], tournament_pool[0]], winners)
        Random.end_test()


    def test_get_tournament_pool(self):
        spea2 = Spea2(default_consistent_problem())
        population = [None for _ in range(5)]
        for i in range(5):
            population[i] = self.default_individual()
            population[i].problem.set_value(0, i)
            population[i].problem.set_value(1, i + 1)
            population[i].problem.set_value(2, i + 1)
        tournament_pool = spea2.get_tournament_pool(population)
        self.assertEqual([population[0] for i in range(5)], tournament_pool[0:5])
        self.assertEqual([population[1] for i in range(4)], tournament_pool[5:9])
        self.assertEqual([population[2] for i in range(3)], tournament_pool[9:12])
        self.assertEqual([population[3] for i in range(2)], tournament_pool[12:14])
        self.assertEqual([population[4] for i in range(1)], tournament_pool[14:15])


    def test_assign_tournament_probabilities(self):
        spea2 = Spea2(default_consistent_problem())
        population = [None for _ in range(5)]
        for i in range(5):
            population[i] = self.default_individual()
            population[i].problem.set_value(0, i)
            population[i].problem.set_value(1, i + 1)
            population[i].problem.set_value(2, i + 1)
        for individual in population:
            self.assertEqual(individual.get_inverse_tournament_rank(), 0)
        tournament_individuals = spea2.assign_tournament_probabilities(population)
        self.assertEqual(tournament_individuals[0].get_inverse_tournament_rank(), 5)
        self.assertEqual(tournament_individuals[1].get_inverse_tournament_rank(), 4)
        self.assertEqual(tournament_individuals[2].get_inverse_tournament_rank(), 3)
        self.assertEqual(tournament_individuals[3].get_inverse_tournament_rank(), 2)
        self.assertEqual(tournament_individuals[4].get_inverse_tournament_rank(), 1)

    def test_solve(self):
        spea2 = Spea2(default_consistent_problem())
        # spea2.solve()
