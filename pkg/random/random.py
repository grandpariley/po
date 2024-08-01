import random
import numpy as np


class Random:
    @classmethod
    def begin_test(cls):
        cls.test = True
        cls.non_random_values = {
            "random_float_between_0_and_1": [],
            "random_int_between_a_and_b": [],
            "random_float_between_a_and_b": [],
            "random_choice": []
        }

    @classmethod
    def end_test(cls):
        cls.test = False
        cls.non_random_values = {}

    @classmethod
    def set_test_value_for(cls, key, value):
        cls.non_random_values.update({key: cls.non_random_values[key] + [value]})

    @classmethod
    def random_int_between_a_and_b(cls, a, b):
        print(str(cls.test) + " | " + str(cls.non_random_values["random_int_between_a_and_b"]))
        if cls.test and cls.non_random_values["random_int_between_a_and_b"]:
            return cls.non_random_values["random_int_between_a_and_b"].pop()
        print("random_int_between_a_and_b " + str(a) + " | " + str(b))
        return random.randint(a, b)

    @classmethod
    def random_choice(cls, lst):
        if cls.test and cls.non_random_values["random_choice"]:
            return cls.non_random_values["random_choice"].pop()
        print("random_choice")
        if len(lst) > 0:
            return random.choice(lst)
        raise ValueError("no choice in list: " + str(lst))

    @classmethod
    def random_normal(cls, lst):
        if cls.test and cls.non_random_values["random_choice"]:
            return cls.non_random_values["random_choice"].pop()
        if len(lst) > 0:
            return lst[np.floor(np.random.normal(np.mean(lst), np.std(lst))).astype(int) % len(lst)]
        raise ValueError("no choice in list: " + str(lst))
