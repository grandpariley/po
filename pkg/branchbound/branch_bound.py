from pkg.problem.solver import Solver
from pkg.branchbound.node import Node
from pkg.problem.compare import non_dominated
from pkg.log import Log
from copy import deepcopy


class BranchBound(Solver):
    def solve_helper(self, collection, solutions):
        Log.log([str(node) for node in collection])
        Log.log([str(s) for s in solutions])
        if not collection:
            Log.log("end of the road")
            return solutions
        node = collection.pop()
        if node.is_leaf():
            if node.is_consistent() and non_dominated(node.get_objective_values(), [s.objective_values() for s in solutions]):
                Log.log("found a solution!")
                solutions.add(node.get_problem())
            return self.solve_helper(collection, solutions)
        for i in range(node.num_variables()):
            if node.get_value(i) is None:
                for d in node.get_domain(i):
                    node.set_value(i, d)
                    collection.append(deepcopy(node))
                    Log.log("new node: " + str(node))
        return self.solve_helper(collection, solutions)

    def solve(self):
        Log.begin_debug("branch-bound")
        solns = self.solve_helper([Node(self.problem)], set())
        Log.end_debug()
        return solns
