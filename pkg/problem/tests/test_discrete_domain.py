import unittest

from pkg.problem.discrete_domain import DiscreteDomain
from pkg.random.random import Random


def default_domain():
    return DiscreteDomain([1, 2, 3, 4, 5], 1)


class DiscreteDomainTest(unittest.TestCase):
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

    def test_iterator(self):
        domain = default_domain()
        i = 1
        for d in domain:
            self.assertEqual(d, i)
            i += 1
