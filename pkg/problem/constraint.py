def constraint_encoder_fn(obj):
    if not isinstance(obj, Constraint):
        return obj
    return obj.name


class Constraint:
    def __init__(self, func, name='constraint'):
        self.func = func
        self.name = name

    def __str__(self):
        return self.name

    def holds(self, curr_variables):
        return bool(self.func(curr_variables))
