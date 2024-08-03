import random
import numpy as np


class Random:
    @classmethod
    def begin_test(cls):
        cls.non_random_values = {
            "random_int_between_a_and_b": [],
            "random_choice": [],
            "random_normal": []
        }

    @classmethod
    def end_test(cls):
        cls.non_random_values = {}

    @classmethod
    def set_test_value_for(cls, key, value):
        cls.non_random_values.update({key: cls.non_random_values[key] + [value]})

    @classmethod
    def random_int_between_a_and_b(cls, a, b):
        if hasattr(cls, "non_random_values") and cls.non_random_values["random_int_between_a_and_b"]:
            return cls.non_random_values["random_int_between_a_and_b"].pop()
        return random.randint(a, b)

    @classmethod
    def random_choice(cls, lst):
        if hasattr(cls, "non_random_values") and cls.non_random_values["random_choice"]:
            return cls.non_random_values["random_choice"].pop()
        if len(lst) > 0:
            return random.choice(lst)
        raise ValueError("no choice in list: " + str(lst))

    @classmethod
    def random_normal(cls, lst):
        if hasattr(cls, "non_random_values") and cls.non_random_values["random_normal"]:
            return cls.non_random_values["random_normal"].pop()
        if len(lst) > 0:
            return lst[np.floor(np.random.normal(np.mean(lst), np.std(lst))).astype(int) % len(lst)]
        raise ValueError("no choice in list: " + str(lst))
