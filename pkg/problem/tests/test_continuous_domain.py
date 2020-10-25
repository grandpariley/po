import unittest

from pkg.problem.continuous_domain import ContinuousDomain
from pkg.random.random import Random


def default_domain():
    return ContinuousDomain(1, 5)


class ContinuousDomainTest(unittest.TestCase):
    def test_pop(self):
        Random.begin_test()
        Random.set_test_value_for("random_float_between_a_and_b", 3)
        self.assertTrue(default_domain().pop(), 3)
        Random.end_test()

    def test_top(self):
        Random.begin_test()
        Random.set_test_value_for("random_float_between_a_and_b", 3)
        self.assertTrue(default_domain().top(), 3)
        Random.end_test()

    def test_closest_in_domain(self):
        self.assertEqual(default_domain().closest(3), 3)

    def test_closest_not_in_domain(self):
        self.assertEqual(default_domain().closest(5.5), 5)
        self.assertEqual(default_domain().closest(0.5), 1)

    def test_contains_contains(self):
        self.assertTrue(3 in default_domain())

    def test_contains_does_not_contain(self):
        self.assertFalse(0.5 in default_domain())
        self.assertFalse(5.5 in default_domain())

    def test_random(self):
        Random.begin_test()
        Random.set_test_value_for("random_float_between_a_and_b", 3)
        self.assertTrue(default_domain().random(), 3)
        Random.end_test()
