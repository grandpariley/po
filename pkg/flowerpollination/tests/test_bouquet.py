import unittest, copy
from pkg.flowerpollination.bouquet import Bouquet
from pkg.flowerpollination.flower import Flower
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.random.random import Random
from pkg.consts import Constants


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

    def test_pollinate(self):
        Random.begin_test()
        Random.set_test_value_for("random_float_between_0_and_1", 0.7)
        Random.set_test_value_for("random_float_between_0_and_1", 0.2)
        flowers = [None for _ in range(6)]
        for i in range(5):
            flowers[i] = self.default_flower()
            flowers[i].problem.set_value(0, i)
            flowers[i].problem.set_value(1, i + 1)
            flowers[i].problem.set_value(2, i + 1)
        flowers[5] = copy.deepcopy(flowers[4])
        bouquet = Bouquet(flowers)
        bouquet.pollinate(0)
        local_pollination_result = bouquet.flowers[0]
        self.assertEqual(local_pollination_result.get_objective_values(), (4, 5, 5))
        bouquet.pollinate(1)
        global_pollination_result = bouquet.flowers[1]
        self.assertEqual(global_pollination_result.get_objective_values(), (4, 5, 5))

    def test_local_pollination(self):
        Random.begin_test()
        Random.set_test_value_for("random_float_between_0_and_1", 0.5)
        Random.set_test_value_for("random_float_between_0_and_1", 0.5)
        Random.set_test_value_for("random_float_between_0_and_1", 0.5)
        Random.set_test_value_for("random_float_between_0_and_1", 0.5)
        flowers = [None for _ in range(6)]
        for i in range(5):
            flowers[i] = self.default_flower()
            flowers[i].problem.set_value(0, i)
            flowers[i].problem.set_value(1, i + 1)
            flowers[i].problem.set_value(2, i + 1)
        flowers[5] = copy.deepcopy(flowers[4])
        bouquet = Bouquet(flowers)
        bouquet.calculate_best()
        bouquet.local_pollination(0)
        local_pollination_result = bouquet.flowers[0]
        self.assertEqual(local_pollination_result.get_objective_values(), (4, 5, 5))
        Random.end_test()
    
    def test_global_pollination(self):
        Constants.FP_GAMMA_CONSTANT = 1
        Constants._fp_levy_constant = 1
        flowers = [None for _ in range(6)]
        for i in range(5):
            flowers[i] = self.default_flower()
            flowers[i].problem.set_value(0, i)
            flowers[i].problem.set_value(1, i + 1)
            flowers[i].problem.set_value(2, i + 1)
        flowers[5] = copy.deepcopy(flowers[4])
        bouquet = Bouquet(flowers)
        bouquet.calculate_best()
        bouquet.global_pollination(0)
        local_pollination_result = bouquet.flowers[0]
        self.assertEqual(local_pollination_result.get_objective_values(), (4, 5, 5))
