import unittest
from pkg.problem.constraint import Constraint
from pkg.problem.variable import Variable

class ConstraintTest(unittest.TestCase):

    def defaultVariables(self):
        return [
            Variable([0, 1]), 
            Variable([0, 1])
        ]

    def defaultHeldConstraint(self):
        variables = self.defaultVariables()
        variables[0].set_value(0)
        variables[1].set_value(0)
        return Constraint((0, 1), lambda variables: variables[0] == variables[1]), variables

    def defaultBrokenConstraint(self):
        variables = self.defaultVariables()
        variables[0].set_value(0)
        variables[1].set_value(1)
        return Constraint((0, 1), lambda variables: variables[0] == variables[1]), variables

    def test_constrained_valid(self):
        """
        test constrained true
        """
        cons, variables = self.defaultHeldConstraint()
        self.assertTrue(cons.holds(variables))

    def test_constrained_broken(self):
        """
        test constrained false
        """
        cons, variables = self.defaultBrokenConstraint()

        self.assertFalse(cons.holds(variables))
