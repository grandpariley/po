import unittest
from pkg.random.random import Random


class RandomTest(unittest.TestCase):

    def test_begin_test(self):
        self.assertFalse(Random.test)
        Random.begin_test()
        self.assertTrue(Random.test)
        Random.end_test()

    def test_end_test(self):
        Random.begin_test()
        self.assertTrue(Random.test)
        Random.end_test()
        self.assertFalse(Random.test)

    def test_set_test_value_for(self):
        Random.begin_test()
        self.assertEqual(
            Random.non_random_values["random_float_between_0_and_1"], [])
        self.assertEqual(
            Random.non_random_values["random_int_between_a_and_b"], [])
        self.assertEqual(
            Random.non_random_values["random_float_between_a_and_b"], [])
        self.assertEqual(Random.non_random_values["random_choice"], [])
        Random.set_test_value_for("random_float_between_0_and_1", 0.123)
        Random.set_test_value_for("random_float_between_0_and_1", 0.456)
        Random.set_test_value_for("random_int_between_a_and_b", 0)
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        Random.set_test_value_for("random_int_between_a_and_b", 2)
        Random.set_test_value_for("random_float_between_a_and_b", 0.000)
        Random.set_test_value_for("random_float_between_a_and_b", 4.123)
        Random.set_test_value_for("random_float_between_a_and_b", 5.432)
        Random.set_test_value_for("random_choice", 3)
        Random.set_test_value_for("random_choice", 5)
        Random.set_test_value_for("random_choice", 2)
        self.assertEqual(
            Random.non_random_values["random_float_between_0_and_1"], [0.123, 0.456])
        self.assertEqual(
            Random.non_random_values["random_int_between_a_and_b"], [0, 1, 2])
        self.assertEqual(Random.non_random_values["random_float_between_a_and_b"], [
            0.000, 4.123, 5.432])
        self.assertEqual(Random.non_random_values["random_choice"], [3, 5, 2])
        Random.end_test()

    def test_random_choice(self):
        true_rando = Random.random_choice([0, 1, 2, 3, 4, 5])
        self.assertIn(true_rando, [0, 1, 2, 3, 4, 5])
        Random.begin_test()
        Random.set_test_value_for("random_choice", 1)
        Random.set_test_value_for("random_choice", 2)
        Random.set_test_value_for("random_choice", 3)
        self.assertEqual(Random.random_choice([0, 1, 2, 3, 4, 5]), 3)
        self.assertEqual(Random.random_choice([0, 1, 2, 3, 4, 5]), 2)
        self.assertEqual(Random.random_choice([0, 1, 2, 3, 4, 5]), 1)
        Random.end_test()
        true_rando = Random.random_choice([0, 4, 5])
        self.assertNotIn(true_rando, [1, 2, 3])

    def test_random_float_between_0_and_1(self):
        true_rando = Random.random_float_between_0_and_1()
        self.assertLessEqual(true_rando, 1.0)
        self.assertLessEqual(0.0, true_rando)
        Random.begin_test()
        Random.set_test_value_for("random_float_between_0_and_1", 0.1)
        Random.set_test_value_for("random_float_between_0_and_1", 0.2)
        Random.set_test_value_for("random_float_between_0_and_1", 0.3)
        self.assertEqual(Random.random_float_between_0_and_1(), 0.3)
        self.assertEqual(Random.random_float_between_0_and_1(), 0.2)
        self.assertEqual(Random.random_float_between_0_and_1(), 0.1)
        Random.end_test()

    def test_random_float_between_a_and_b(self):
        true_rando = Random.random_float_between_a_and_b(2.4142, 3.1416)
        self.assertLessEqual(true_rando, 3.1416)
        self.assertLessEqual(2.4142, true_rando)
        Random.begin_test()
        Random.set_test_value_for("random_float_between_0_and_1", 2.5)
        Random.set_test_value_for("random_float_between_0_and_1", 2.9)
        Random.set_test_value_for("random_float_between_0_and_1", 3.1)
        self.assertEqual(Random.random_float_between_0_and_1(), 3.1)
        self.assertEqual(Random.random_float_between_0_and_1(), 2.9)
        self.assertEqual(Random.random_float_between_0_and_1(), 2.5)
        Random.end_test()

    def test_random_int_between_a_and_b(self):
        true_rando = Random.random_int_between_a_and_b(1, 5)
        self.assertLessEqual(true_rando, 5)
        self.assertLessEqual(1, true_rando)
        Random.begin_test()
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        Random.set_test_value_for("random_int_between_a_and_b", 2)
        Random.set_test_value_for("random_int_between_a_and_b", 3)
        self.assertEqual(Random.random_int_between_a_and_b(1, 5), 3)
        self.assertEqual(Random.random_int_between_a_and_b(1, 5), 2)
        self.assertEqual(Random.random_int_between_a_and_b(1, 5), 1)
        Random.end_test()
