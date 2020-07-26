class Constraint:
    def __init__(self, variable_indicies, func):
        self.func = func
        self.variable_indicies = variable_indicies
    
    def __str__(self):
        return str(self.variable_indicies)
    
    def holds(self, curr_variables):
        var_vals = tuple(curr_variables[i].get_value() for i in self.variable_indicies)
        for var_val in var_vals:
            if var_val == None:
                return False
        return bool(self.func(var_vals))
