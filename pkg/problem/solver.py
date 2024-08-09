from abc import abstractmethod


class Solver:
    def __init__(self, problems, output_folder):
        self.problems = problems
        self.output_folder = output_folder

    def __str__(self):
        return str(self.problems)

    @abstractmethod
    def solve(self):
        raise NotImplementedError
