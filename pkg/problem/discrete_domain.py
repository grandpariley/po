from pkg.problem.domain import Domain


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

    def closest(self, target):
        if not target:
            return None
        if target in self.values:
            return target
        current_closest = self.values[0]
        current_closest_distance = float('inf')
        for value in self.values:
            distance = value - target
            if current_closest_distance > abs(distance) or (
                    current_closest_distance == abs(distance) and value > current_closest):
                current_closest = value
                current_closest_distance = abs(distance)
        return current_closest

    def get_base_value(self):
        return self.base_value
