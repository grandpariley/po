import unittest

from pkg.consts import Constants
from pkg.moead.moead import Moead, get_non_dominated, is_non_dominated
from pkg.moead.tests.test_util import default_individual_with_values, default_dominated_individual, \
    default_dominating_individual, default_other_dominating_individual
from pkg.problem.tests.default_problems import default_consistent_problem, get_test_data
from pkg.random.random import Random


def set_random_test_values_a_b():
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)


def set_random_test_values_choice():
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")
    Random.set_test_value_for("random_choice", "0")


def get_population():
    return [
        default_individual_with_values(),
        default_dominated_individual(),
        default_dominating_individual(),
        default_other_dominating_individual()
    ]


class MoeadTest(unittest.TestCase):

    def test_solve_helper(self):
        Constants.NUM_GENERATIONS = 3
        Constants.MOEAD_NUM_WEIGHT_VECTORS_T = 2
        Constants.GENES_MUTATING = 0.4
        Constants.DATA = get_test_data()
        Random.begin_test()
        set_random_test_values_a_b()
        set_random_test_values_choice()

        p1 = default_consistent_problem()
        p1.set_value("0", 1)
        p1.set_value("1", 2)
        p1.set_value("2", 5)
        p2 = default_consistent_problem()
        p2.set_value("0", 5)
        p2.set_value("1", 3)
        p2.set_value("2", 5)
        p3 = default_consistent_problem()
        p3.set_value("0", 3)
        p3.set_value("1", 1)
        p3.set_value("2", 4)
        p4 = default_consistent_problem()
        p4.set_value("0", 4)
        p4.set_value("1", 1)
        p4.set_value("2", 2)
        p5 = default_consistent_problem()
        p5.set_value("0", 1)
        p5.set_value("1", 3)
        p5.set_value("2", 1)
        moead = Moead([p1, p2, p3, p4, p5])
        actual_solution = moead.solve()
        self.assertEqual((5, 3, 5), actual_solution[0].objective_values())
        Random.end_test()

    def test_is_non_dominated(self):
        self.assertTrue(is_non_dominated(default_other_dominating_individual(), get_population()))
        self.assertFalse(is_non_dominated(default_dominated_individual(), get_population()))

    def test_get_non_dominated(self):
        non_dominated = get_non_dominated(get_population())
        self.assertEqual(
            [default_other_dominating_individual()],
            non_dominated
        )
