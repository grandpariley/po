from pkg.problem.compare import dominates

class Individual:
    def __init__(self, problem):
        self.problem = problem
        self.dominates = set()
        self.domination_count = 0
        self.crowding_distance = 0
        self.rank = None

    def __str__(self):
        return str(self.problem) + "\n" + str(self.dominates) + "\n" + str(self.domination_count)

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def does_dominate(self, q):
        return dominates(self.problem.objective_values(), q.problem.objective_values())

    def add_dominated(self, q):
        self.dominates.add(q)

    def increment_dominated(self):
        self.domination_count += 1

    def set_rank(self, rank):
        self.rank = rank

    def is_dominated(self):
        return self.domination_count != 0

    def get_dominated(self):
        return self.dominates

    def decrement_dominated(self):
        if self.domination_count > 0:
            self.domination_count -= 1

    def set_crowding_distance(self, crowding_distance):
        self.crowding_distance = crowding_distance

    def get_crowding_distance(self):
        return self.crowding_distance

    def get_objective_values(self):
        return self.problem.objective_values()