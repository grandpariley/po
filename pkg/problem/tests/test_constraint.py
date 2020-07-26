import unittest
from pkg.problem.constraint import Constraint
from pkg.problem.variable import Variable

class ConstraintTest(unittest.TestCase):

    def default_variables(self):
        return [
            Variable([0, 1]), 
            Variable([0, 1])
        ]

    def default_held_constraint(self):
        variables = self.default_variables()
        variables[0].set_value(0)
        variables[1].set_value(0)
        return Constraint((0, 1), lambda variables: variables[0] == variables[1]), variables

    def default_broken_constraint(self):
        variables = self.default_variables()
        variables[0].set_value(0)
        variables[1].set_value(1)
        return Constraint((0, 1), lambda variables: variables[0] == variables[1]), variables

    def test_constrained_valid(self):
        cons, variables = self.default_held_constraint()
        self.assertTrue(cons.holds(variables))

    def test_constrained_broken(self):
        cons, variables = self.default_broken_constraint()

        self.assertFalse(cons.holds(variables))
