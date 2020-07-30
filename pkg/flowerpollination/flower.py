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
    
    def get_value(self, index):
        return self.problem.get_value(index)

    def safe_set_value(self, index, value):
        self.problem.set_value(index, self.problem.closest_in_domain(index, value))

    def num_variables(self):
        return self.problem.num_variables()