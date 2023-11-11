import matplotlib.pyplot as plt

ORDER_OF_COLOURS = ['ko', 'ro', 'bo']


class Plot:
    def __init__(self, solutions, timer):
        self.solutions = solutions
        self.timer = timer

    # FIXME TWO AND ONLY TWO
    def print(self, objective_indexes):
        for objective_index in objective_indexes:
            for objective_index2 in objective_indexes:
                if objective_index == objective_index2:
                    continue
                colour = iter(ORDER_OF_COLOURS)
                for key in self.solutions:
                    plt.plot([s.objective_values()[objective_index] for s in self.solutions[key]],
                             [s.objective_values()[objective_index2] for s in self.solutions[key]], next(colour),
                             label=key)
                plt.xlabel(objective_index)
                plt.ylabel(objective_index2)
                plt.show()

    def compare(self):
        print(self.timer.get_times_as_formatted_str())
