class Variable:
    def __init__(self, domain, objective_info):
        self.domain = domain
        self.objective_info = objective_info
        self.value = None

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

    def reset_value(self):
        self.value = None

    def get_domain(self):
        return self.domain

    def get_random_from_domain(self):
        return self.domain.random()

    def closest_in_domain(self, value):
        return self.domain.closest(value)

    def get_objective_info(self):
        return self.objective_info
