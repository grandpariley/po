from pkg.problem.domain import Domain, closest_in_list


class DiscreteDomain(Domain):
    def __init__(self, values):
        super().__init__()
        self.values = values

    def __str__(self):
        return str(self.values)

    def contains(self, el):
        if not self.values:
            return False
        return el in self.values

    def pop(self):
        if not self.values:
            return None
        return self.values.pop()

    def top(self):
        if not self.values:
            return None
        return self.values[-1]

    def closest(self, el):
        return closest_in_list(el, self.values)
