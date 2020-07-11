import copy

class Problem:
    """
    define a problem as 
        a set of variables, 
        a set of constraints on those variables, and 
        an optional objective lambda function of the form ([x, y, z] => return a) where a is to be maximized
    """

    def __init__(self, variables, constraints, objectiveFuncs):
        self.variables = variables
        self.constraints = constraints
        self.objectiveFuncs = objectiveFuncs

    def __str__(self):
        return "Problem: \n\tvariables: " + str([str(var) for var in self.variables]) + "\n\tconstraints: " + str([str(con) for con in self.constraints])

    def consistent(self):
        for constraint in self.constraints:
            if not constraint.holds(self.variables):
                return False
        return True

    def will_be_consistent(self, variable_index, variable_value):
        if variable_index < 0 or variable_index >= len(self.variables):
            return False
        problem = copy.deepcopy(self)
        problem.set_value(variable_index, variable_value)
        return problem.consistent()

    def all_assigned(self):
        for variable in self.variables:
            if variable.get_value() is None:
                return False
        return True

    def set_value(self, variable_index, value):
        if 0 <= variable_index < len(self.variables):
            self.variables[variable_index].set_value(value)
    
    def reset_value(self, variable_index):
        if 0 <= variable_index < len(self.variables):
            self.variables[variable_index].reset_value()

    def objective_values(self):
        if self.objectiveFuncs is None:
            return None
        return tuple([objFunc(self.variables) for objFunc in self.objectiveFuncs])
    
    def get_domain(self, variable_index):
        if 0 <= variable_index < len(self.variables):
            return self.variables[variable_index].get_domain()
        return []

    def num_variables(self):
        return len(self.variables)

    def variable_assignments(self):
        return tuple([v.get_value() for v in self.variables])
