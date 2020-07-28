import unittest
from pkg.nsga2.nsga2 import Nsga2
from pkg.nsga2.individual import Individual
from pkg.problem.tests.default_problems import default_consistent_problem, default_consistent_problem_set_values


class Nsga2Test(unittest.TestCase):
    def default_individual(self):
        return Individual(default_consistent_problem_set_values())

    # TODO
    def test_fast_non_dominating_sort(self):
        pass

    # TODO
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


    # TODO
    def test_generate_children(self):
        pass

    # TODO
    def test_get_parents(self):
        pass

    # TODO
    def test_get_children(self):
        pass

    # TODO
    def test_tournament(self):
        pass

    # TODO
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
        crowding_distance_individuals = nsga2.assign_tournament_probabilities(individuals)
        self.assertEqual(crowding_distance_individuals[0].get_inverse_tournament_rank(), 0)
        self.assertEqual(crowding_distance_individuals[1].get_inverse_tournament_rank(), 0)
        self.assertEqual(crowding_distance_individuals[2].get_inverse_tournament_rank(), 0)
        self.assertEqual(crowding_distance_individuals[3].get_inverse_tournament_rank(), 0)

    def test_solve(self):
        nsga2 = Nsga2(default_consistent_problem())
        # nsga2.solve()
