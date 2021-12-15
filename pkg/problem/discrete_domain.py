from pkg.problem.domain import Domain, closest_in_list
from pkg.random.random import Random


class DiscreteDomain(Domain):
    def __init__(self, values, base_value):
        super().__init__()
        self.values = values
        self.base_value = base_value

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __contains__(self, item):
        if not self.values:
            return False
        return item in self.values

    def __iter__(self):
        self.iterator = iter(self.values)
        return self

    def __next__(self):
        return next(self.iterator)

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

    def random(self):
        return Random.random_choice(self.values)

    def get_base_value(self):
        return self.base_value