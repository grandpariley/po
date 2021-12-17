class Variable:
    def __init__(self, domain, objective_info):
        self.domain = domain
        self.objective_info = objective_info
        self.value = domain.get_base_value()

    def __str__(self):
        return str(self.domain) + " {" + str(self.value) + "}"

    def pop(self):
        return self.domain.pop()

    def top(self):
        return self.domain.top()

    def set_value(self, value):
        if value in self.domain:
            self.value = value

    def get_value(self):
        return self.value
