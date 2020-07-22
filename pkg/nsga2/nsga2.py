from pkg.problem.solver import Solver
from pkg.nsga2.individual import Individual
from pkg.problem.builder import generateManyRandomSolutions
from pkg.consts import Constants

class Nsga2(Solver):
    def fast_non_dominated_sort(self, population):
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

    def crowding_distance_assignment(self, solutions):
        pass

    def generate_children(self, parent_population):
        return []

    def solve_helper(self):
        parent_population = [Individual(p) for p in generateManyRandomSolutions(self.problem, Constants.NSGA2_NUM_INDIVIDUALS)]
        child_population = [Individual(p) for p in generateManyRandomSolutions(self.problem, Constants.NSGA2_NUM_INDIVIDUALS)]
        for _ in range(Constants.NSGA2_NUM_GENERATIONS):
            front = self.fast_non_dominated_sort(parent_population + child_population)
            parent_population = []
            i = 0
            while len(parent_population) + len(front[i]) < Constants.NSGA2_NUM_INDIVIDUALS:
                self.crowding_distance_assignment(front[i])
                parent_population += front[i]
                i += 1
            parent_population += front[i][0:Constants.NSGA2_NUM_INDIVIDUALS - len(parent_population)]
            child_population = self.generate_children(parent_population)

    def solve(self):
        return self.solve_helper()