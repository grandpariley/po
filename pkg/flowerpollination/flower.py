class Flower:
    def __init__(self, problem):
        self.problem = problem

    def __str__(self):
        return str(self.problem)

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def get_objective_values(self):
        return self.problem.objective_values()