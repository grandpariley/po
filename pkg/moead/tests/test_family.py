import unittest

from pkg.consts import Constants
from pkg.moead.family import generate_child, get_parents
from pkg.moead.tests.test_util import default_b, default_individuals, default_individual
from pkg.problem.tests.default_problems import get_test_data
from pkg.random.random import Random


class FamilyTest(unittest.TestCase):
    def test_generate_child(self):
        Random.begin_test()
        Constants.MOEAD_NUM_WEIGHT_VECTORS_T = 2
        Constants.DATA = get_test_data()
        individuals = default_individuals()
        Random.set_test_value_for("random_choice", 1)
        Random.set_test_value_for("random_choice", 1)
        Random.set_test_value_for("random_int_between_a_and_b", 0)
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        Random.set_test_value_for("random_int_between_a_and_b", 2)
        Random.set_test_value_for("random_int_between_a_and_b", 0)
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        child = generate_child(individuals)
        expected = default_individual()
        expected.problem.set_value('0', 1)
        expected.problem.set_value('1', 2)
        expected.problem.set_value('2', 2)
        Random.end_test()
        self.assertEqual(child, expected)

    def test_get_parents(self):
        Random.begin_test()
        Constants.MOEAD_NUM_CLOSEST_WEIGHT_VECTORS = 2
        individuals = default_individuals()
        Random.set_test_value_for("random_int_between_a_and_b", 0)
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        mum, dad = get_parents(individuals)
        expected_mum = default_individual()
        expected_mum.problem.set_value('0', 2)
        expected_mum.problem.set_value('1', 3)
        expected_mum.problem.set_value('2', 3)
        expected_dad = default_individual()
        expected_dad.problem.set_value('0', 1)
        expected_dad.problem.set_value('1', 2)
        expected_dad.problem.set_value('2', 2)
        self.assertEqual(mum, expected_mum)
        self.assertEqual(dad, expected_dad)
        Random.end_test()
