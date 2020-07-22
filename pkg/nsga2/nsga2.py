from pkg.problem.solver import Solver
from pkg.nsga2.individual import Individual
from pkg.problem.builder import generateManyRandomSolutions
from pkg.consts import Constants

class Nsga2(Solver):
    def solve_helper(self, population):
        front = [set()]
        for p in population:
            for q in population:
                if p.does_dominate(q):
                    p.add_dominated(q)
                elif q.does_dominate(p):
                    p.increment_dominated()
            if not p.is_dominated():
                p.set_rank(0)
                front[0].add(p)
        front_count = 0
        while front[front_count]:
            next_front = set()
            for p in front[front_count]:
                for q in p.get_dominates():
                    q.decrement_dominated()
                    if not q.is_dominated():
                        q.set_rank(front_count + 1)
                        next_front.add(q)
            front_count += 1
            front.append(next_front)
        return front

    def solve(self):
        return self.solve_helper([Individual(p) for p in generateManyRandomSolutions(self.problem, Constants.NSGA2_NUM_INDIVIDUALS)])[0]