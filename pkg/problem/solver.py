from abc import abstractmethod


class Solver:
    def __init__(self, problems, data):
        self.problems = problems
        self.data = data

    def __str__(self):
        return str(self.problems)

    @abstractmethod
    def solve(self):
        raise NotImplementedError
