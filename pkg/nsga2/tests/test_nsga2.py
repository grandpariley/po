import unittest
from pkg.nsga2.nsga2 import Nsga2, fast_non_dominated_sort, crowding_distance_assignment, get_tournament_pool, \
    generate_children, get_parents, get_children, assign_tournament_probabilities
from pkg.nsga2.individual import Individual
from pkg.random.random import Random
from pkg.consts import Constants
from pkg.log import Log
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
        front = fast_non_dominated_sort(individuals)
        self.assertEqual(front, [[individuals[i]] for i in range(3, -1, -1)] + [[]])

    def test_crowding_distance_assignment(self):
        individuals = default_individuals()
        for individual in individuals:
            self.assertEqual(individual.get_crowding_distance(), 0)
        crowding_distance_individuals = crowding_distance_assignment(individuals)
        self.assertEqual(crowding_distance_individuals[0].get_crowding_distance(), float('inf'))
        self.assertEqual(crowding_distance_individuals[1].get_crowding_distance(), 3.3333333333333335)
        self.assertEqual(crowding_distance_individuals[2].get_crowding_distance(), float('inf'))
        self.assertEqual(crowding_distance_individuals[3].get_crowding_distance(), float('inf'))

    def test_generate_children(self):
        Random.begin_test()
        individuals = default_individuals()
        tournament_pool = get_tournament_pool(individuals)
        Constants.NSGA2_NUM_GENES_MUTATING = 3
        for _ in range(2):
            for _ in range(2):
                Random.set_test_value_for("random_int_between_a_and_b", 2)
                Random.set_test_value_for("random_int_between_a_and_b", 1)
                Random.set_test_value_for("random_int_between_a_and_b", 0)
                Random.set_test_value_for("random_float_between_a_and_b", 1)
                Random.set_test_value_for("random_float_between_a_and_b", 1)
                Random.set_test_value_for("random_float_between_a_and_b", 1)
            Random.set_test_value_for("random_choice", tournament_pool[1])
            Random.set_test_value_for("random_choice", tournament_pool[0])
        children = generate_children(individuals)
        self.assertEqual(len(children), 4)
        Random.end_test()

    def test_get_parents(self):
        Random.begin_test()
        individuals = default_individuals()
        tournament_pool = get_tournament_pool(individuals)
        Random.set_test_value_for("random_choice", tournament_pool[0])
        Random.set_test_value_for("random_choice", tournament_pool[-1])
        mum, dad = get_parents(individuals)
        self.assertEqual(mum, tournament_pool[-1])
        self.assertEqual(dad, tournament_pool[0])

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
        Constants.NSGA2_NUM_INDIVIDUALS = 4
        Constants.NSGA2_NUM_GENERATIONS = 20
        Constants.NSGA2_NUM_GENES_MUTATING = 2
        nsga2 = Nsga2(default_consistent_problem())
        solutions = nsga2.solve()
        Log.newline()
        Log.log([str(s) for s in solutions], context="test-nsga2")
