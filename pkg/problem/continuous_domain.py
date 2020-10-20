from pkg.problem.domain import Domain


class ContinuousDomain(Domain):
    def __init__(self, low, high):
        super().__init__()
        self.low = low
        self.high = high

    def __str__(self):
        return str(self.low) + "," + str(self.high)

    def contains(self, el):
        if not self.low or not self.high:
            return False
        return self.low <= el <= self.high

    def pop(self):
        # TODO figure out what this means for a continuous domain
        raise NotImplementedError

    def top(self):
        # TODO figure out what this means for a continuous domain
        raise NotImplementedError

    def closest(self, el):
        if not self.low or not self.high:
            return False
        if el <= self.low:
            return self.low
        if el >= self.high:
            return self.high
        return el
