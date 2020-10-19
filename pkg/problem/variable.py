from copy import deepcopy


class Variable:
    def __init__(self, domain, objective_info):
        self.domain = domain
        self.objective_info = objective_info
        self.value = None

    def __str__(self):
        return str(self.domain) + " {" + str(self.value) + "}"

    def pop(self):
        if not self.domain:
            return None
        return self.domain.pop()

    def top(self):
        if not self.domain:
            return None
        return self.domain[-1]

    def set_value(self, value):
        if value in self.domain:
            self.value = value

    def get_value(self):
        return self.value

    def reset_value(self):
        self.value = None

    def get_domain(self):
        return self.domain

    def closest_in_domain(self, value):
        if not self.domain:
            return None
        if value in self.domain:
            return value
        domain = deepcopy(self.domain)
        domain.append(value)
        domain.sort()
        if value == domain[0]:
            return domain[1]
        elif value == domain[-1]:
            return domain[-2]
        closest_under = domain[domain.index(value) - 1]
        closest_over = domain[domain.index(value) + 1]
        if abs(closest_under - value) < abs(closest_over - value):
            return closest_under
        return closest_over

    def get_objective_info(self):
        return self.objective_info
