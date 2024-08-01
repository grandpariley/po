import unittest

from pkg.consts import Constants
from pkg.moead.moead import Moead
from pkg.problem.tests.default_problems import default_consistent_problem, get_test_data
from pkg.random.random import Random


def set_random_test_values_a_b():
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 1)
    Random.set_test_value_for("random_int_between_a_and_b", 2)
    Random.set_test_value_for("random_int_between_a_and_b", 0)
    Random.set_test_value_for("random_int_between_a_and_b", 1)


def set_random_test_values_choice():
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)
    Random.set_test_value_for("random_choice", 0)


class MoeadTest(unittest.TestCase):

    def test_solve_helper(self):
        Constants.NUM_GENERATIONS = 3
        Constants.MOEAD_NUM_WEIGHT_VECTORS_T = 2
        Random.begin_test()
        # number of random_int_between_a_and_b: Constants.NUM_GENERATIONS * len(parent_population) * (2 + 1 + x) = 45x
        # number of random_choice: Constants.NUM_GENERATIONS * len(parent_population) * (x) = 15x
        set_random_test_values_a_b()
        set_random_test_values_choice()

        p1 = default_consistent_problem()
        p1.set_value("0", 0)
        p1.set_value("1", 2)
        p1.set_value("2", 5)
        p2 = default_consistent_problem()
        p2.set_value("0", 5)
        p2.set_value("1", 3)
        p2.set_value("2", 5)
        p3 = default_consistent_problem()
        p3.set_value("0", 3)
        p3.set_value("1", 0)
        p3.set_value("2", 4)
        p4 = default_consistent_problem()
        p4.set_value("0", 4)
        p4.set_value("1", 1)
        p4.set_value("2", 2)
        p5 = default_consistent_problem()
        p5.set_value("0", 1)
        p5.set_value("1", 3)
        p5.set_value("2", 1)
        moead = Moead([p1, p2, p3, p4, p5], get_test_data())
        actual_solution = moead.solve()
        print(actual_solution)
        Random.end_test()
