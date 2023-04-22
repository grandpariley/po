import time
from pkg.log import Log


class Timer:
    def __init__(self):
        self.times = {}

    def time(self, func, label):
        start = time.process_time_ns()
        rt = func()
        end = time.process_time_ns()
        self.times[label] = (end - start)
        return rt

    def get_times_as_formatted_str(self):
        builder = "Times: "
        for label, thyme in self.times.items():
            builder += "\n\t" + str(label) + " : " + str(thyme / 1000.000) + "ms"
        return builder
