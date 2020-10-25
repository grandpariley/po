import unittest

from pkg.problem.functional_domain import FunctionalDomain
from pkg.random.random import Random


def default_domain():
    return FunctionalDomain(lambda: [1, 2, 3, 4, 5])


class FunctionalDomainTest(unittest.TestCase):
    def test_pop(self):
        self.assertTrue(1 <= default_domain().pop() <= 5)

    def test_top(self):
        self.assertTrue(1 <= default_domain().top() <= 5)

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
        Random.set_test_value_for("random_choice", 3)
        self.assertTrue(default_domain().random(), 3)
        Random.end_test()
