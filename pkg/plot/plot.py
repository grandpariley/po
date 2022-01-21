import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, solutions, timer):
        self.solutions = solutions
        self.timer = timer

    def print(self):
        i = 0
        fig = plt.figure(figsize=(12, 12))
        for key in self.solutions:
            i += 1
            points = [[], [], []]
            for s in self.solutions[key]:
                points[0].append(s.objective_values()[0])
                points[1].append(s.objective_values()[1])
                points[2].append(1)
            subplot = fig.add_subplot(1, 1, 1, projection='3d')
            subplot.scatter(np.array(points[0]), np.array(points[1]), np.array(points[2]))
        plt.show()

    def compare(self):
        print(self.timer.get_times_as_formatted_str())
