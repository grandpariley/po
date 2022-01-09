import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, solutions, timer):
        self.solutions = solutions
        self.timer = timer

    def print(self):
        i = 0
        for key in self.solutions:
            print(key)
            i += 1
            xpoints = []
            ypoints = []
            for s in self.solutions[key]:
                xpoints.append(s.objective_values()[0])
                ypoints.append(s.objective_values()[1])
            plt.subplot(1, 1, i)
            plt.scatter(np.array(xpoints), np.array(ypoints))
        plt.show()

    def compare(self):
        # solution_compare = compare_solutions(self.solutions)
        # non_dominated_str = ""
        # for name in solution_compare:
        #     if solution_compare[name]:
        #         non_dominated_str += name + ", "
        # non_dominated_str = non_dominated_str[0:-2]
        # print(non_dominated_str + " have solutions that are not dominated by other solutions")
        print(self.timer.get_times_as_formatted_str())
