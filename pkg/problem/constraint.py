def constraint_encoder_fn(obj):
    if not isinstance(obj, Constraint):
        return obj
    if obj.variables is None:
        return {
            "variables": []
        }
    return {
        "variables": obj.variables
    }


class Constraint:
    def __init__(self, func, variables=None):
        self.variables = variables
        self.func = func

    def __str__(self):
        return str(self.variables)

    def holds(self, curr_variables):
        param = {}
        if self.variables is not None:
            for v in self.variables:
                if v in curr_variables.keys():
                    param[v] = curr_variables[v]
            return bool(self.func(param))
        return bool(self.func(curr_variables))
