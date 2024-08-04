import unittest
from pkg.random.random import Random


class RandomTest(unittest.TestCase):

    def test_set_test_value_for(self):
        Random.begin_test()
        self.assertEqual(Random.non_random_values["random_int_between_a_and_b"], [])
        self.assertEqual(Random.non_random_values["random_choice"], [])
        Random.set_test_value_for("random_int_between_a_and_b", 0)
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        Random.set_test_value_for("random_int_between_a_and_b", 2)
        Random.set_test_value_for("random_choice", 3)
        Random.set_test_value_for("random_choice", 5)
        Random.set_test_value_for("random_choice", 2)
        self.assertEqual(Random.non_random_values["random_int_between_a_and_b"], [0, 1, 2])
        self.assertEqual(Random.non_random_values["random_choice"], [3, 5, 2])
        Random.end_test()

    def test_random_choice(self):
        Random.begin_test()
        true_rando = Random.random_choice([0, 1, 2, 3, 4, 5])
        self.assertIn(true_rando, [0, 1, 2, 3, 4, 5])
        Random.set_test_value_for("random_choice", 1)
        Random.set_test_value_for("random_choice", 2)
        Random.set_test_value_for("random_choice", 3)
        self.assertEqual(Random.random_choice([0, 1, 2, 3, 4, 5]), 3)
        self.assertEqual(Random.random_choice([0, 1, 2, 3, 4, 5]), 2)
        self.assertEqual(Random.random_choice([0, 1, 2, 3, 4, 5]), 1)
        true_rando = Random.random_choice([0, 4, 5])
        self.assertNotIn(true_rando, [1, 2, 3])
        Random.end_test()

    def test_random_int_between_a_and_b(self):
        Random.begin_test()
        true_rando = Random.random_int_between_a_and_b(1, 5)
        self.assertLessEqual(true_rando, 5)
        self.assertLessEqual(1, true_rando)
        Random.set_test_value_for("random_int_between_a_and_b", 1)
        Random.set_test_value_for("random_int_between_a_and_b", 2)
        Random.set_test_value_for("random_int_between_a_and_b", 3)
        self.assertEqual(Random.random_int_between_a_and_b(1, 5), 3)
        self.assertEqual(Random.random_int_between_a_and_b(1, 5), 2)
        self.assertEqual(Random.random_int_between_a_and_b(1, 5), 1)
        Random.end_test()

