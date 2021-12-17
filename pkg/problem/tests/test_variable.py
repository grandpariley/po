import unittest

from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.variable import Variable


def default_variable():
    return Variable(DiscreteDomain([1, 2, 3, 4, 5], 1), {})


class VariableTest(unittest.TestCase):

    def test_pop(self):
        var = default_variable()
        self.assertEqual(var.pop(), 5)
        self.assertEqual(len(var.domain), 4)

    def test_pop_empty(self):
        var = Variable(DiscreteDomain([], 0), {})
        self.assertIsNone(var.pop())

    def test_top(self):
        var = default_variable()
        self.assertEqual(var.top(), 5)
        self.assertEqual(len(var.domain), 5)

    def test_top_empty(self):
        var = Variable(DiscreteDomain([], 0), {})
        self.assertIsNone(var.top())

    def test_set_value(self):
        var = default_variable()
        var.set_value(3)
        self.assertEqual(var.get_value(), 3)

    def test_set_value_not_in_domain(self):
        var = default_variable()
        var.set_value(7)
        self.assertEqual(var.get_value(), var.domain.get_base_value())
