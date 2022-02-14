class Problem:
    def __init__(self, variables, constraints, objective_funcs):
        self.variables = variables
        self.constraints = constraints
        self.objective_funcs = objective_funcs

    def __str__(self):
        return "Problem: \n\tvariables: " + str([str(var) for var in self.variables]) + "\n\tconstraints: " + \
               str([str(con) for con in self.constraints]) + "\n\tobjective values: " + \
               str([str(obj) for obj in self.objective_values()]) + "\n"

    def __repr__(self):
        representation = ""
        for v in range(len(self.variables)):
            if self.variables[v].get_value():
                representation += str(v) + " " + repr(self.variables[v]) + ";"
        return representation

    def consistent(self):
        for constraint in self.constraints:
            if not constraint.holds(self.variables):
                return False
        return True

    def set_value(self, variable_index, value):
        if 0 <= variable_index < len(self.variables):
            self.variables[variable_index].set_value(value)

    def get_value(self, variable_index):
        if 0 <= variable_index < len(self.variables):
            return self.variables[variable_index].get_value()
        return None

    def num_variables(self):
        return len(self.variables)

    def objective_values(self):
        if self.objective_funcs is None:
            return None
        return tuple([obj_func(self.variables) for obj_func in self.objective_funcs])
