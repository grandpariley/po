import unittest, copy
from pkg.flowerpollination.bouquet import Bouquet
from pkg.flowerpollination.flower import Flower
from pkg.problem.tests.default_problems import default_consistent_problem


class BouquetTest(unittest.TestCase):
    def default_flower(self):
        return Flower(default_consistent_problem())

    def test_calculate_best(self):
        flowers = [None for _ in range(6)]
        for i in range(5):
            flowers[i] = self.default_flower()
            flowers[i].problem.set_value(0, i)
            flowers[i].problem.set_value(1, i + 1)
            flowers[i].problem.set_value(2, i + 1)
        flowers[5] = copy.deepcopy(flowers[4])
        bouquet = Bouquet(flowers)
        bouquet.calculate_best()
        self.assertEqual(flowers[4:5], bouquet.get_best())