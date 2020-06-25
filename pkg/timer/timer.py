import time

class Timer:
    def __init__(self):
        self.clearTimes()

    def time(self, func, label):
        start = time.process_time_ns()
        rt = func()
        end = time.process_time_ns()
        self.times[label] = (end - start)
        return rt
        
    def getTimesAsFormattedString(self):
        builder = "Times: "
        for label, time in self.times.items():
            builder += "\n\t" + str(label) + " : " + str(time) + "ns"
        return builder
        
    def clearTimes(self):
        self.times = {}
