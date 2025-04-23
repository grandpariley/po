from abc import abstractmethod


class Solver:
    def __init__(self, problems, tag=None):
        self.problems = problems
        self.tag = tag

    def __str__(self):
        return str(self.problems)

    @abstractmethod
    def solve(self):
        raise NotImplementedError
