import unittest
from pkg.branchbound.branch_bound import BranchBound
from pkg.problem.tests.default_problems import default_consistent_problem


class BranchBoundTest(unittest.TestCase):
    def test_solve(self):
        branch_bound = BranchBound(default_consistent_problem())
        # solution = branch_bound.solve()
        # self.assertEqual(solution.variable_assignments(), (2, 1, 2))
