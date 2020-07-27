import unittest
from pkg.problem.compare import dominates


class CompareTest(unittest.TestCase):
    def test_dominates(self):
        objs = [(3, 2, 1), (3, 2, 2), (3, 2, 2), (1, 2, 3)]
        self.assertTrue(dominates(objs[1], objs[0]))
        self.assertFalse(dominates(objs[0], objs[1]))
        self.assertFalse(dominates(objs[1], objs[2]))
        self.assertFalse(dominates(objs[2], objs[3]))
        self.assertFalse(dominates(objs[0], objs[3]))
        self.assertFalse(dominates(objs[3], objs[0]))
