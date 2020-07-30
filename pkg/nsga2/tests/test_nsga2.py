import unittest
from pkg.nsga2.nsga2 import Nsga2
from pkg.nsga2.individual import Individual
from pkg.random.random import Random
from pkg.problem.tests.default_problems import default_consistent_problem, default_consistent_problem_set_values


class Nsga2Test(unittest.TestCase):
    def default_individual(self):
        return Individual(default_consistent_problem_set_values())

    def test_fast_non_dominating_sort(self):
        nsga2 = Nsga2(default_consistent_problem())
        individuals = [None for _ in range(4)]
        for i in range(4):
            individuals[i] = self.default_individual()
            individuals[i].problem.set_value(0, i)
            individuals[i].problem.set_value(1, i + 1)
            individuals[i].problem.set_value(2, i + 1)
        front = nsga2.fast_non_dominated_sort(individuals)
        self.assertEqual(front, [set([individuals[i]]) for i in range(3, -1, -1)] + [set()])

    def test_crowding_distance_assignment(self):
        nsga2 = Nsga2(default_consistent_problem())
        individuals = [None for _ in range(4)]
        for i in range(4):
            individuals[i] = self.default_individual()
            individuals[i].problem.set_value(0, i)
            individuals[i].problem.set_value(1, i + 1)
            individuals[i].problem.set_value(2, i + 1)
        for individual in individuals:
            self.assertEqual(individual.get_crowding_distance(), 0)
        crowding_distance_individuals = nsga2.crowding_distance_assignment(individuals)
        self.assertEqual(crowding_distance_individuals[0].get_crowding_distance(), float('inf'))
        self.assertEqual(crowding_distance_individuals[1].get_crowding_distance(), 3.3333333333333335)
        self.assertEqual(crowding_distance_individuals[2].get_crowding_distance(), float('inf'))
        self.assertEqual(crowding_distance_individuals[3].get_crowding_distance(), float('inf'))


    def test_generate_children(self):
        nsga2 = Nsga2(default_consistent_problem())
        individuals = [None for _ in range(4)]
        for i in range(4):
            individuals[i] = self.default_individual()
            individuals[i].problem.set_value(0, i)
            individuals[i].problem.set_value(1, i + 1)
            individuals[i].problem.set_value(2, i + 1)
        children = nsga2.generate_children(individuals)
        self.assertEqual(len(children), 4)

    def test_get_parents(self):
        Random.begin_test()
        nsga2 = Nsga2(default_consistent_problem())
        individuals = [None for _ in range(4)]
        for i in range(4):
            individuals[i] = self.default_individual()
            individuals[i].problem.set_value(0, i)
            individuals[i].problem.set_value(1, i + 1)
            individuals[i].problem.set_value(2, i + 1)
        tournament_pool = nsga2.get_tournament_pool(individuals)
        Random.set_test_value_for("random_choice", tournament_pool[0])
        Random.set_test_value_for("random_choice", tournament_pool[-1])
        Random.set_test_value_for("random_choice", tournament_pool[-1])
        mum, dad = nsga2.get_parents(individuals)
        self.assertEqual(mum, tournament_pool[-1])
        self.assertEqual(dad, tournament_pool[0])

    def test_get_children(self):
        Random.begin_test()
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        Random.set_test_value_for("random_int_between_a_and_b", 2)
        nsga2 = Nsga2(default_consistent_problem())
        individuals = [None for _ in range(4)]
        for i in range(2):
            individuals[i] = self.default_individual()
            individuals[i].problem.set_value(0, i)
            individuals[i].problem.set_value(1, i + 1)
            individuals[i].problem.set_value(2, i + 1)
        son, daughter = nsga2.get_children(individuals[0], individuals[1])
        son_values = [son.problem.get_value(i) for i in range(son.problem.num_variables())]
        daughter_values = [daughter.problem.get_value(i) for i in range(daughter.problem.num_variables())]
        self.assertEqual(son_values, [1, 2, 1])
        self.assertEqual(daughter_values, [0, 2, 1])
        Random.end_test()

    def test_tournament_pool(self):
        nsga2 = Nsga2(default_consistent_problem())
        individuals = [None for _ in range(4)]
        for i in range(4):
            individuals[i] = self.default_individual()
            individuals[i].problem.set_value(0, i)
            individuals[i].problem.set_value(1, i + 1)
            individuals[i].problem.set_value(2, i + 1)
        tournament_pool = nsga2.get_tournament_pool(individuals)
        self.assertEqual([individuals[0] for i in range(4)], tournament_pool[0:4])
        self.assertEqual([individuals[1] for i in range(3)], tournament_pool[4:7])
        self.assertEqual([individuals[2] for i in range(2)], tournament_pool[7:9])
        self.assertEqual([individuals[3] for i in range(1)], tournament_pool[9:10])

    def test_assign_tournament_probabilities(self):
        nsga2 = Nsga2(default_consistent_problem())
        individuals = [None for _ in range(4)]
        for i in range(4):
            individuals[i] = self.default_individual()
            individuals[i].problem.set_value(0, i)
            individuals[i].problem.set_value(1, i + 1)
            individuals[i].problem.set_value(2, i + 1)
        for individual in individuals:
            self.assertEqual(individual.get_inverse_tournament_rank(), 0)
        tournament_individuals = nsga2.assign_tournament_probabilities(individuals)
        self.assertEqual(tournament_individuals[0].get_inverse_tournament_rank(), 4)
        self.assertEqual(tournament_individuals[1].get_inverse_tournament_rank(), 3)
        self.assertEqual(tournament_individuals[2].get_inverse_tournament_rank(), 2)
        self.assertEqual(tournament_individuals[3].get_inverse_tournament_rank(), 1)

    def test_solve(self):
        nsga2 = Nsga2(default_consistent_problem())
        # nsga2.solve()
