import unittest
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.nsga2.individual import Individual

class IndividualTest(unittest.TestCase):
    def defaultIndividual(self):
        problem = default_consistent_problem()
        problem.set_value(0, 1)
        problem.set_value(1, 1)
        problem.set_value(2, 1)
        return Individual(problem)

    def defaultDominatingIndividual(self):
        other_problem = default_consistent_problem()
        other_problem.set_value(0, 1)
        other_problem.set_value(1, 2)
        other_problem.set_value(2, 1)
        return Individual(other_problem)

    def test_does_dominate(self):
        self.assertTrue(self.defaultDominatingIndividual().does_dominate(self.defaultIndividual()))

    def test_add_dominated(self):
        individual = self.defaultDominatingIndividual()
        other_individual = self.defaultIndividual()
        individual.add_dominated(other_individual)
        self.assertEqual(individual.get_dominated(), set([other_individual]))

    def test_increment_dominated(self):
        individual = self.defaultDominatingIndividual()
        self.assertEqual(individual.domination_count, 0)
        individual.increment_dominated()
        self.assertEqual(individual.domination_count, 1)

    def test_set_rank(self):
        individual = self.defaultDominatingIndividual()
        self.assertIsNone(individual.rank)
        individual.set_rank(3)
        self.assertEqual(individual.rank, 3)

    def test_is_dominated(self):
        individual = self.defaultDominatingIndividual()
        self.assertFalse(individual.is_dominated())
        individual.increment_dominated()
        self.assertTrue(individual.is_dominated())

    def test_decrement_dominated(self):
        individual = self.defaultDominatingIndividual()
        self.assertEqual(individual.domination_count, 0)
        individual.increment_dominated()
        self.assertEqual(individual.domination_count, 1)
        individual.decrement_dominated()
        self.assertEqual(individual.domination_count, 0)
        individual.decrement_dominated()
        self.assertEqual(individual.domination_count, 0)

    def test_set_get_crowding_distance(self):
        individual = self.defaultDominatingIndividual()
        self.assertEqual(individual.get_crowding_distance(), 0)
        individual.set_crowding_distance(3.14)
        self.assertEqual(individual.get_crowding_distance(), 3.14)

    