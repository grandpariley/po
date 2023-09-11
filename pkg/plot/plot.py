import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, solutions, timer):
        self.solutions = solutions
        self.timer = timer

    def print(self):
        for key in self.solutions:
            fig = plt.figure(figsize=(12, 12))
            points = [[], []]
            for s in self.solutions[key]:
                points[0].append(s.objective_values()[0])
                points[1].append(s.objective_values()[1])
            subplot = fig.add_subplot(1, 1, projection='2d')
            subplot.scatter(np.array(points[0]), np.array(points[1]))
        plt.show()
        for key in self.solutions:
            fig = plt.figure(figsize=(12, 12))
            points = [[], []]
            for s in self.solutions[key]:
                points[0].append(s.objective_values()[2])
                points[1].append(s.objective_values()[3])
                points[2].append(s.objective_values()[4])
            subplot = fig.add_subplot(1, 1, 1, projection='3d')
            subplot.scatter(np.array(points[0]), np.array(points[1]), np.array(points[1]))
        plt.show()

    def compare(self):
        print(self.timer.get_times_as_formatted_str())
