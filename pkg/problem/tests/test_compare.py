import unittest
from pkg.problem.compare import compareSolutions

class CompareTest(unittest.TestCase):
    def test_compare(self):
        compareSolutions(None, None)
