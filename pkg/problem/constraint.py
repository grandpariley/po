class Constraint:
    def __init__(self, variable_indexes, func):
        self.func = func
        self.variable_indexes = variable_indexes

    def __str__(self):
        return str(self.variable_indexes)

    def holds(self, curr_variables):
        vrs = tuple(curr_variables[i] for i in self.variable_indexes)
        for vr in vrs:
            if vr.get_value() is None:
                return False
        return bool(self.func(vrs))
