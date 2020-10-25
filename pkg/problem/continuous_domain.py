from pkg.consts import Constants
from pkg.problem.domain import Domain
from pkg.random.random import Random
from math import inf


class ContinuousDomain(Domain):
    def __init__(self, low, high):
        super().__init__()
        if low > high:
            raise ArithmeticError
        self.low = low
        self.high = high

    def __str__(self):
        return str(self.low) + "," + str(self.high)

    def __len__(self):
        return inf

    def __contains__(self, item):
        if not self.low or not self.high:
            return False
        return self.low <= item <= self.high

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > Constants.CONTINUOUS_DOMAIN_ITERATION_LIMIT:
            raise StopIteration
        return self.random()

    def top(self):
        return self.random()

    def pop(self):
        return self.random()

    def closest(self, el):
        if el <= self.low:
            return self.low
        if el >= self.high:
            return self.high
        return el

    def random(self):
        return Random.random_float_between_a_and_b(self.low, self.high)