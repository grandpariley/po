from pkg.problem.compare import dominates


class Individual:
    def __init__(self, problem=None, individual=None):
        if problem is None and individual is None:
            raise ValueError("must have a problem or an individual")
        elif problem is not None and individual is not None:
            raise ValueError("must have one of a problem or an individual")
        if problem is not None:
            self.problem = problem
        elif individual is not None:
            self.problem = individual.problem

    def __str__(self):
        return str(self.problem)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if self.problem.num_variables() != other.problem.num_variables():
            return False
        for i in range(self.problem.num_variables()):
            if self.problem.get_value(i) != other.problem.get_value(i):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str([self.problem.get_value(v) for v in range(self.problem.num_variables())]))

    def does_dominate(self, q):
        return dominates(self.problem.objective_values(), q.problem.objective_values())