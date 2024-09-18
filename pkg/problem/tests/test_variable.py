import unittest

from po.pkg.problem.discrete_domain import DiscreteDomain
from po.pkg.problem.variable import Variable


def default_variable():
    return Variable(DiscreteDomain(5, 1), {})


class VariableTest(unittest.TestCase):

    def test_set_value(self):
        var = default_variable()
        var.set_value(3)
        self.assertEqual(var.get_value(), 3)

    def test_set_value_not_in_domain(self):
        var = default_variable()
        var.set_value(7)
        self.assertEqual(var.get_value(), var.domain.get_base_value())
