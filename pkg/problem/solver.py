from abc import abstractmethod

class Solver:
    """
    Solver interface to ensure all solvers 
        have a string representation, 
        take a problem as a constructor parameter
        have a defined solve method
    """
    def __init__(self, problem):
        self.problem = problem
    
    def __str__(self):
        return str(self.problem)

    @abstractmethod
    def solve(self): 
        raise NotImplementedError