import unittest
from copy import deepcopy
from pkg.flowerpollination.bouquet import Bouquet
from pkg.flowerpollination.flower import Flower
from pkg.problem.tests.default_problems import default_consistent_problem
from pkg.random.random import Random
from pkg.consts import Constants


def default_flower():
    return Flower(default_consistent_problem())


def default_flowers():
    flowers = [None for _ in range(6)]
    for i in range(5):
        flowers[i] = default_flower()
        flowers[i].problem.set_value(0, i)
        flowers[i].problem.set_value(1, i + 1)
        flowers[i].problem.set_value(2, i + 1)
    return flowers


class BouquetTest(unittest.TestCase):

    def test_calculate_best(self):
        flowers = default_flowers()
        flowers[5] = deepcopy(flowers[4])
        bouquet = Bouquet(flowers)
        bouquet.calculate_best()
        self.assertEqual(flowers[4:5], bouquet.get_best())

    def test_pollinate(self):
        Random.begin_test()
        flowers = default_flowers()
        flowers[5] = deepcopy(flowers[4])
        for _ in range(9):
            Random.set_test_value_for("random_float_between_0_and_1", 0.5)
        Random.set_test_value_for("random_float_between_0_and_1", 0.7)
        Random.set_test_value_for("random_float_between_0_and_1", 0.2)
        bouquet = Bouquet(flowers)
        bouquet.pollinate(0)
        local_pollination_result = bouquet.flowers[0]
        self.assertEqual(local_pollination_result.get_objective_values(), (4, 5, 5))
        bouquet.pollinate(1)
        global_pollination_result = bouquet.flowers[1]
        self.assertEqual(global_pollination_result.get_objective_values(), (3, 4, 4))

    def test_local_pollination(self):
        Random.begin_test()
        flowers = default_flowers()
        flowers[5] = deepcopy(flowers[4])
        for _ in range(len(flowers[0].get_objective_values()) * flowers[0].num_variables()):
            Random.set_test_value_for("random_float_between_0_and_1", 0.5)
        bouquet = Bouquet(flowers)
        bouquet.calculate_best()
        bouquet.local_pollination(0)
        local_pollination_result = bouquet.flowers[0]
        self.assertEqual(local_pollination_result.get_objective_values(), (3, 4, 4))
        Random.end_test()

    def test_global_pollination(self):
        Constants.FP_GAMMA_CONSTANT = 1
        Constants._fp_levy_constant = 1
        flowers = default_flowers()
        flowers[5] = deepcopy(flowers[4])
        bouquet = Bouquet(flowers)
        bouquet.calculate_best()
        bouquet.global_pollination(0)
        local_pollination_result = bouquet.flowers[0]
        self.assertEqual(local_pollination_result.get_objective_values(), (4, 5, 5))
