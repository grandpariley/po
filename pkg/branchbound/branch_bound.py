from pkg.problem.solver import Solver

class BranchBound(Solver):
    def solve_helper(self, i):
        return self.problem
    
    def solve(self):
        return self.solve_helper(0)

