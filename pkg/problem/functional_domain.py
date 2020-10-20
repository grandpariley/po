from pkg.problem.domain import Domain, closest_in_list


class FunctionalDomain(Domain):
    def __init__(self, get_values):
        super().__init__()
        self.get_values = get_values

    def __str__(self):
        raise str(self.get_values())

    def contains(self, el):
        if not self.get_values:
            return False
        return el in self.get_values()

    def pop(self):
        if not self.get_values:
            return None
        return self.get_values().pop()

    def top(self):
        if not self.get_values:
            return None
        return self.get_values()[-1]

    def closest(self, el):
        return closest_in_list(el, self.get_values())
