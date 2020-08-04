import time
from pkg.log import Log


class Timer:
    def __init__(self):
        self.clear_times()

    def time(self, func, label):
        Log.begin_debug("timer")
        Log.log("starting " + label)
        start = time.process_time_ns()
        rt = func()
        end = time.process_time_ns()
        Log.log("stopping " + label)
        self.times[label] = (end - start)
        Log.end_debug()
        return rt

    def get_times_as_formatted_str(self):
        builder = "Times: "
        for label, time in self.times.items():
            builder += "\n\t" + str(label) + " : " + str(time / 1000.000) + "ms"
        return builder

    def clear_times(self):
        self.times = {}
