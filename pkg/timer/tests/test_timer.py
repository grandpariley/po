import unittest
from pkg.timer.timer import Timer


class TimerTest(unittest.TestCase):
    def test_timer(self):
        timer = Timer()
        rt = timer.time(lambda: sum([i for i in range(10000000)]), "test")
        self.assertEqual(list(timer.times.keys())[0], "test")
        self.assertGreater(list(timer.times.values())[0][0], 0)
        self.assertEqual(49999995000000, rt)
