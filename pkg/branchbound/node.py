class Node:
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

    def is_leaf(self):
        return self.problem.all_assigned()

    def is_consistent(self):
        return self.problem.consistent()

    def get_problem(self):
        return self.problem

    def num_variables(self):
        return self.problem.num_variables()

    def get_value(self, variable_index):
        return self.problem.get_value(variable_index)

    def get_domain(self, variable_index):
        return self.problem.get_domain(variable_index)

    def set_value(self, variable_index, variable_value):
        return self.problem.set_value(variable_index, variable_value)

    def get_objective_values(self):
        return self.problem.objective_values()
