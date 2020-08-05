class Constraint:
    def __init__(self, variable_indicies, func):
        self.func = func
        self.variable_indicies = variable_indicies

    def __str__(self):
        return str(self.variable_indicies)

    def holds(self, curr_variables):
        vrs = tuple(curr_variables[i] for i in self.variable_indicies)
        return bool(self.func(vrs))
