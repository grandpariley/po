import unittest
from pkg.problem.constraint import Constraint
from pkg.problem.discrete_domain import DiscreteDomain
from pkg.problem.variable import Variable


def default_variables():
    return {
        "0": Variable(DiscreteDomain(1, 0), {}),
        "1": Variable(DiscreteDomain(1, 0), {})
    }


def default_held_constraint():
    variables = default_variables()
    variables["0"].set_value(1)
    variables["1"].set_value(1)
    return Constraint(lambda v: v["0"].get_value() == v["1"].get_value(), ("0", "1")), variables


def default_broken_constraint():
    variables = default_variables()
    variables["0"].set_value(1)
    variables["1"].set_value(2)
    return Constraint(lambda v: v["0"].get_value() == v["1"].get_value(), ("0", "1")), variables


class ConstraintTest(unittest.TestCase):

    def test_constrained_valid(self):
        cons, variables = default_held_constraint()
        self.assertTrue(cons.holds(variables))

    def test_constrained_broken(self):
        cons, variables = default_broken_constraint()
        self.assertFalse(cons.holds(variables))
