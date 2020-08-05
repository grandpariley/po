class Individual:
    def __init__(self, problem):
        self.problem = problem
        self.inverse_tournament_rank = 0

    def __str__(self):
        return str(self.problem) + "\nrank: " + str(self.inverse_tournament_rank)

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def set_inverse_tournament_rank(self, inverse_tournament_rank):
        self.inverse_tournament_rank = inverse_tournament_rank

    def get_inverse_tournament_rank(self):
        return self.inverse_tournament_rank

    def get_objective_values(self):
        return self.problem.objective_values()
    
    def get_problem(self):
        return self.problem