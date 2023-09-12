import unittest

from pkg.nsga2.tests.test_util import default_individuals
from pkg.nsga2.tournament import get_tournament_pool, assign_tournament_probabilities


class TournamentTest(unittest.TestCase):
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
