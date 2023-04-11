from pkg.problem.domain import Domain
from pkg.random.random import Random


class DiscreteDomain(Domain):
    def __init__(self, max_value, base_value):
        super().__init__()
        self.max = max_value
        self.base_value = base_value

    def __str__(self):
        return str(self.max)

    def __len__(self):
        return self.max

    def __contains__(self, item):
        if not self.max:
            return False
        return 0 <= item <= self.max

    def __iter__(self):
        self.iterator = iter(range(self.max))
        return self

    def __next__(self):
        return next(self.iterator)

    def get_random(self):
        return Random.random_int_between_a_and_b(0, self.max)

    def closest(self, target):
        if not target:
            return None
        if 0 <= target <= self.max:
            return round(target, 0)
        return self.max

    def get_base_value(self):
        return self.base_value
