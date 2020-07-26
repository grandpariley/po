from abc import abstractmethod

class Solver:
    def __init__(self, problem):
        self.problem = problem
    
    def __str__(self):
        return str(self.problem)

    @abstractmethod
    def solve(self): 
        raise NotImplementedError