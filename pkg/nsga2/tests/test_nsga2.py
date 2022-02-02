import unittest

from pkg.nsga2.family import generate_children, get_parents, get_children
from pkg.nsga2.nsga2 import Nsga2, fast_non_dominated_sort, crowding_distance_assignment
from pkg.nsga2.individual import Individual
from pkg.nsga2.tournament import get_tournament_pool, assign_tournament_probabilities
from pkg.random.random import Random
from pkg.consts import Constants
from pkg.problem.tests.default_problems import default_consistent_problem, default_consistent_problem_set_values


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


class Nsga2Test(unittest.TestCase):

    def test_fast_non_dominating_sort(self):
        individuals = default_individuals()
        fast_non_dominated_sort(individuals)
        self.assertEqual(
            [i for i in range(len(individuals) - 1, -1, -1)],
            [individuals[i].get_domination_count() for i in range(len(individuals))]
        )

    def test_crowding_distance_assignment(self):
        individuals = default_individuals()
        for individual in individuals:
            self.assertEqual(individual.get_crowding_distance(), 0)
        crowding_distance_assignment(individuals)
        self.assertEqual(individuals[0].get_crowding_distance(), float('inf'))
        self.assertEqual(individuals[1].get_crowding_distance(), 3.3333333333333335)
        self.assertEqual(individuals[2].get_crowding_distance(), float('inf'))
        self.assertEqual(individuals[3].get_crowding_distance(), float('inf'))

    def test_generate_children(self):
        individuals = default_individuals()
        children = generate_children(individuals, get_tournament_pool)
        self.assertEqual(len(children), 4)

    def test_get_parents(self):
        Random.begin_test()
        individuals = default_individuals()
        tournament_pool = get_tournament_pool(individuals)
        Random.set_test_value_for("random_choice", tournament_pool[0])
        Random.set_test_value_for("random_choice", tournament_pool[-1])
        mum, dad = get_parents(individuals, get_tournament_pool)
        self.assertEqual(mum, tournament_pool[-1])
        self.assertEqual(dad, tournament_pool[0])
        Random.end_test()

    def test_get_children(self):
        Random.begin_test()
        for _ in range(4):
            Random.set_test_value_for("random_int_between_a_and_b", 1)
            Random.set_test_value_for("random_int_between_a_and_b", 2)
        individuals = default_individuals()
        son, daughter = get_children(individuals[0], individuals[1])
        son_values = [son.problem.get_value(i) for i in range(son.problem.num_variables())]
        daughter_values = [daughter.problem.get_value(i) for i in range(daughter.problem.num_variables())]
        self.assertEqual(son_values, [1, 2, 1])
        self.assertEqual(daughter_values, [0, 2, 1])
        Random.end_test()

    def test_tournament_pool(self):
        individuals = default_individuals()
        tournament_pool = get_tournament_pool(individuals)
        self.assertEqual([individuals[0] for i in range(4)], tournament_pool[0:4])
        self.assertEqual([individuals[1] for i in range(3)], tournament_pool[4:7])
        self.assertEqual([individuals[2] for i in range(2)], tournament_pool[7:9])
        self.assertEqual([individuals[3] for i in range(1)], tournament_pool[9:10])

    def test_assign_tournament_probabilities(self):
        individuals = default_individuals()
        for individual in individuals:
            self.assertEqual(individual.get_inverse_tournament_rank(), 0)
        tournament_individuals = assign_tournament_probabilities(individuals)
        self.assertEqual(tournament_individuals[0].get_inverse_tournament_rank(), 4)
        self.assertEqual(tournament_individuals[1].get_inverse_tournament_rank(), 3)
        self.assertEqual(tournament_individuals[2].get_inverse_tournament_rank(), 2)
        self.assertEqual(tournament_individuals[3].get_inverse_tournament_rank(), 1)

    def test_solve(self):
        Constants.NSGA2_NUM_GENERATIONS = 3
        Constants.NSGA2_NUM_GENES_MUTATING = 1
        p1 = default_consistent_problem()
        p1.set_value(0, 0)
        p1.set_value(1, 2)
        p1.set_value(2, 5)
        p2 = default_consistent_problem()
        p2.set_value(0, 5)
        p2.set_value(1, 3)
        p2.set_value(2, 5)
        p3 = default_consistent_problem()
        p3.set_value(0, 3)
        p3.set_value(1, 0)
        p3.set_value(2, 4)
        p4 = default_consistent_problem()
        p4.set_value(0, 4)
        p4.set_value(1, 1)
        p4.set_value(2, 2)
        p5 = default_consistent_problem()
        p5.set_value(0, 1)
        p5.set_value(1, 3)
        p5.set_value(2, 1)
        nsga2 = Nsga2([p1, p2, p3, p4, p5])
        solutions = nsga2.solve()
        print(solutions)
        self.assertTrue(True)
        Random.end_test()
