from copy import deepcopy
from pkg.problem.solver import Solver
from pkg.branchbound.node import Node
from pkg.problem.compare import non_dominated


class BranchBound(Solver):
    def solve_helper(self, collection, solutions):
        if not collection:
            return solutions
        node = collection.pop()
        if node.is_leaf() and node.is_consistent() and non_dominated(node.get_objective_values(), [s.objective_values() for s in solutions]):
            solutions.append(node.get_problem())
            return solutions
        if not node.is_leaf():
            for i in range(node.num_variables()):
                if node.get_value(i) is None:
                    for d in node.get_domain(i):
                        node.set_value(i, d)
                        collection.append(deepcopy(node))
        return self.solve_helper(collection, solutions)

    def solve(self):
        return self.solve_helper([Node(self.problem)], [])
