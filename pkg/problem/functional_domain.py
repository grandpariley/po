from pkg.problem.domain import Domain, closest_in_list
from pkg.random.random import Random


class FunctionalDomain(Domain):
    def __init__(self, get_values):
        super().__init__()
        self.get_values = get_values

    def __str__(self):
        raise str(self.get_values())

    def __len__(self):
        return len(self.get_values())

    def __contains__(self, item):
        if not self.get_values:
            return False
        return item in self.get_values()

    def __iter__(self):
        self.iterator = iter(self.get_values())
        return self

    def __next__(self):
        return next(self.iterator)

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

    def random(self):
        return Random.random_choice(self.get_values())