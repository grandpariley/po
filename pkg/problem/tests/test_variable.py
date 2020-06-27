import unittest
from pkg.problem.variable import Variable

class VariableTest(unittest.TestCase):
    def default_variable(self):
        return Variable([1, 2, 3, 4, 5])

    def test_pop(self):
        """
        test pop
        """
        var = self.default_variable()
        self.assertEqual(var.pop(), 5)
        self.assertEqual(len(var.domain), 4)

    def test_pop_empty(self):
        """
        test pop for empty domain
        """
        var = Variable([])
        self.assertIsNone(var.pop())
    
    def test_top(self):
        """
        test top
        """
        var = self.default_variable()
        self.assertEqual(var.top(), 5)
        self.assertEqual(len(var.domain), 5)
    
    def test_top_empty(self):
        """
        test top for empty domain
        """
        var = Variable([])
        self.assertIsNone(var.top())

    def test_set_value(self):
        """
        test set value in domain
        """
        var = self.default_variable()
        var.set_value(3)
        self.assertEqual(var.get_value(), 3)

    def test_set_value_not_in_domain(self):
        """
        test set value not in domain
        """
        var = self.default_variable()
        var.set_value(7)
        self.assertIsNone(var.get_value())

    def test_reset_value(self):
        var = self.default_variable()
        var.set_value(3)
        self.assertEqual(var.get_value(), 3)
        var.reset_value()
        self.assertIsNone(var.get_value())
