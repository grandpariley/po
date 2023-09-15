import unittest

from pkg.moead.family import generate_child, get_parents
from pkg.moead.tests.test_util import default_b, default_individuals
from pkg.problem.tests.default_problems import get_test_data
from pkg.random.random import Random


class FamilyTest(unittest.TestCase):
    def test_generate_child(self):
        individuals = default_individuals()
        child = generate_child(individuals, default_b(), get_test_data())
        self.assertEqual(child, None)

    def test_get_parents(self):
        Random.begin_test()
        individuals = default_individuals()
        Random.set_test_value_for("random_int_between_a_and_b", 0)
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        mum, dad = get_parents(individuals, False)
        self.assertEqual(mum, individuals[0])
        self.assertEqual(dad, individuals[1])
        Random.end_test()

