import unittest
from pkg.timer.timer import Timer


class TimerTest(unittest.TestCase):
    def test_timer(self):
        timer = Timer()
        rt = timer.time(lambda: sum([i for i in range(10000000)]), "test")
        self.assertEqual(next(iter(timer.times.keys())), "test")
        self.assertEqual(type(next(iter(timer.times.values()))), type(1))
        self.assertGreater(next(iter(timer.times.values())), 0)
        self.assertEqual(rt, 49999995000000)

    def test_get_times_as_string(self):
        timer = Timer()
        timer.time(lambda: sum([i for i in range(10000000)]), "test")
        self.assertEqual(timer.get_times_as_formatted_str(),
                         "Times: \n\ttest : " + str(timer.times["test"]) + "ns")

    def test_clear_times(self):
        timer = Timer()
        timer.time(lambda: sum([i for i in range(10000000)]), "test1")
        timer.time(lambda: sum([i for i in range(10000000)]), "test2")
        timer.time(lambda: sum([i for i in range(10000000)]), "test3")
        self.assertEqual(len(timer.times), 3)
        timer.clear_times()
        self.assertEqual(len(timer.times), 0)
