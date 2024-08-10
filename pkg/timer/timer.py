import json
import time


class Timer:
    def __init__(self):
        self.times = {}

    def time(self, func, label):
        start = time.process_time_ns()
        rt = func()
        end = time.process_time_ns()
        if label not in self.times:
            self.times[label] = []
        self.times[label].append((end - start))
        return rt

    def save(self):
        for t in self.times.keys():
            with open(t + '/times.json', 'w') as json_file:
                json.dump(self.times[t], json_file)