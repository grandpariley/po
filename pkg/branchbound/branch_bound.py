from pkg.problem.solver import Solver

class BranchBound(Solver):
    """
    implementation of the branch and bound algorithm for the generic Problem
    """
    def solve_helper(self, i):
        # if self.problem.all_assigned() and self.problem.consistent():
        #     self.solutions.append(self.problem)
        # for d in self.problem.get_domain(i):
        #     if self.problem.will_be_consistent(i, d):
        #         self.problem.set_value(i, d)
        #         return self.solve_helper((i + 1) % self.problem.num_variables())
        return self.problem
    
    def solve(self):
        self.solutions = []
        return self.solve_helper(0)

