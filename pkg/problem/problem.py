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

    def objective_values(self):
        if self.objectiveFuncs is None:
            return None
        return tuple([objFunc(self.variables) for objFunc in self.objectiveFuncs])
