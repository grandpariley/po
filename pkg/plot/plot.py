import matplotlib.pyplot as plt

ORDER_OF_COLOURS = ['ko', 'ro', 'bo']
INDEX_TO_LABEL = ['VaR', 'CVaR', 'Return', 'Environment', 'Governance', 'Social']


class Plot:
    def __init__(self, solutions, timer):
        self.solutions = solutions
        self.timer = timer

    # FIXME TWO AND ONLY TWO
    def print(self, objective_indexes):
        done = []
        for objective_index in objective_indexes:
            for objective_index2 in objective_indexes:
                if (objective_index == objective_index2 or
                        (objective_index, objective_index2) in done or
                        (objective_index2, objective_index) in done):
                    continue
                done.append((objective_index, objective_index2))
                colour = iter(ORDER_OF_COLOURS)
                for key in self.solutions:
                    plt.plot([s.objective_values()[objective_index] for s in self.solutions[key]],
                             [s.objective_values()[objective_index2] for s in self.solutions[key]], next(colour),
                             label=key)
                plt.xlabel(INDEX_TO_LABEL[objective_index])
                plt.ylabel(INDEX_TO_LABEL[objective_index2])
                plt.show()

    def compare(self):
        print(self.timer.get_times_as_formatted_str())
