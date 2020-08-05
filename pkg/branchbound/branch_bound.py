from pkg.problem.solver import Solver
from pkg.branchbound.node import Node
from pkg.problem.compare import non_dominated
from pkg.log import Log
from copy import deepcopy


class BranchBound(Solver):
    lower_bound = -float('inf')

    def bound_ok(self, node):
        return self.lower_bound < sum(node.get_objective_values())

    def set_lower_bound(self, node):
        if self.lower_bound < sum(node.get_objective_values()):
            self.lower_bound = sum(node.get_objective_values())
    
    def solve_helper(self, collection, solutions):
        if not collection:
            return solutions
        node = collection.pop()
        if node.is_leaf():
            if node.is_consistent() and non_dominated(node.get_objective_values(), [s.objective_values() for s in solutions]):
                self.set_lower_bound(node)
                solutions.add(node.get_problem())
            return self.solve_helper(collection, solutions)
        for i in range(node.num_variables()):
            if node.get_value(i) is None:
                for d in node.get_domain(i):
                    node.set_value(i, d)
                    if node.is_consistent() and self.bound_ok(node):
                        collection.append(deepcopy(node))
        return self.solve_helper(collection, solutions)

    def solve(self):
        Log.begin_debug("branch-bound")
        solns = self.solve_helper([Node(self.problem)], set())
        Log.end_debug()
        return solns
