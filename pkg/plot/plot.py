import math

import matplotlib.pyplot as plt

ORDER_OF_COLOURS = ['ko', 'ro', 'bo']
INDEX_TO_LABEL = ['VaR', 'CVaR', 'Return', 'Environment', 'Governance', 'Social']


class Plot:
    def __init__(self, solutions, timer):
        self.solutions = solutions
        self.timer = timer

    # FIXME TWO AND ONLY TWO
    def print(self, objective_indexes, nrows=None, ncols=None):
        done = []
        if nrows is None or ncols is None:
            nrows = 2
            ncols = int(math.comb(len(objective_indexes), 2) / 2)
        figure, axis = plt.subplots(nrows, ncols, figsize=(24, 10))
        axis_count_rows = 0
        axis_count_cols = 0
        for objective_index in objective_indexes:
            for objective_index2 in objective_indexes:
                if (objective_index == objective_index2 or
                        (objective_index, objective_index2) in done or
                        (objective_index2, objective_index) in done):
                    continue
                done.append((objective_index, objective_index2))
                colour = iter(ORDER_OF_COLOURS)

                for key in self.solutions:
                    axis[axis_count_rows, axis_count_cols].plot(
                        [s.objective_values()[objective_index] for s in self.solutions[key]],
                        [s.objective_values()[objective_index2] for s in self.solutions[key]],
                        next(colour),
                        label=key)
                axis[axis_count_rows, axis_count_cols].set_title(
                    INDEX_TO_LABEL[objective_index] + " compared to " + INDEX_TO_LABEL[objective_index2])
                axis_count_rows = (axis_count_rows + 1) % nrows
                axis_count_cols = (axis_count_cols + 1) % ncols
        plt.show()

    def compare(self):
        print(self.timer.get_times_as_formatted_str())
