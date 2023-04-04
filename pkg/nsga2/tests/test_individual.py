import unittest

from pkg.nsga2.tests.test_util import default_dominating_individual, default_individual, \
    default_other_dominating_individual, default_individual_with_values
from pkg.random.random import Random
from pkg.consts import Constants


class IndividualTest(unittest.TestCase):

    def test_does_dominate(self):
        self.assertTrue(default_dominating_individual().does_dominate(default_individual_with_values()))

    def test_increment_dominated(self):
        individual = default_dominating_individual()
        self.assertEqual(individual.domination_count, 0)
        individual.increment_dominated()
        self.assertEqual(individual.domination_count, 1)

    def test_is_dominated(self):
        individual = default_dominating_individual()
        self.assertFalse(individual.is_dominated())
        individual.increment_dominated()
        self.assertTrue(individual.is_dominated())

    def test_decrement_dominated(self):
        individual = default_dominating_individual()
        self.assertEqual(individual.domination_count, 0)
        individual.increment_dominated()
        self.assertEqual(individual.domination_count, 1)
        individual.decrement_dominated()
        self.assertEqual(individual.domination_count, 0)
        individual.decrement_dominated()
        self.assertEqual(individual.domination_count, 0)

    def test_set_get_crowding_distance(self):
        individual = default_individual()
        self.assertEqual(individual.get_crowding_distance(), 0)
        individual.set_crowding_distance(3.14)
        self.assertEqual(individual.get_crowding_distance(), 3.14)

    def test_swap_half_genes(self):
        Random.begin_test()
        Random.set_test_value_for("random_int_between_a_and_b", 2)
        parent = default_dominating_individual()
        child = default_other_dominating_individual()
        child.swap_half_genes(parent)
        values = [child.problem.get_value(k) for k in child.problem.keys()]
        self.assertEqual(values, [1, 3, 1])
        Random.end_test()

    def test_emo_phase(self):
        Random.begin_test()
        Constants.NSGA2_NUM_GENES_MUTATING = 1
        Random.set_test_value_for("random_choice", 3)
        Random.set_test_value_for("random_choice", "2")
        child = default_dominating_individual()
        child.emo_phase()
        self.assertEqual(child.problem.get_value("0"), 1)
        self.assertEqual(child.problem.get_value("1"), 2)
        self.assertEqual(child.problem.get_value("2"), 3)
        Random.end_test()

    def test_eq(self):
        self.assertTrue(default_individual() == default_individual())
        self.assertFalse(default_individual() == default_dominating_individual())
