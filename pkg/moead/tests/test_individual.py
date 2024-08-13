import unittest

from pkg.consts import Constants
from pkg.moead.tests.test_util import default_dominating_individual, default_individual, \
    default_other_dominating_individual, default_individual_with_values, default_dominated_individual
from pkg.problem.tests.default_problems import get_test_data
from pkg.random.random import Random


def default_combination_strategy(child, parent):
    return child


class IndividualTest(unittest.TestCase):

    def test_does_dominate(self):
        self.assertTrue(default_dominating_individual().does_dominate(default_individual_with_values()))

    def test_swap_half_genes_reset(self):
        Constants.DATA = get_test_data()
        Random.begin_test()
        Random.set_test_value_for("random_choice", '1')
        Random.set_test_value_for("random_choice", '2')
        parent = default_individual_with_values()
        child = default_other_dominating_individual()
        child.swap_half_genes(parent)
        values = [child.problem.get_value(k) for k in child.problem.keys()]
        Random.end_test()
        self.assertEqual([1, 3, 1], values)

    def test_swap_half_genes(self):
        Constants.DATA = get_test_data()
        Random.begin_test()
        Random.set_test_value_for("random_choice", '1')
        Random.set_test_value_for("random_choice", '0')
        parent = default_dominating_individual()
        child = default_dominated_individual()
        child.swap_half_genes(parent)
        values = [child.problem.get_value(k) for k in child.problem.keys()]
        Random.end_test()
        self.assertEqual([1, 2, 1], values)

    def test_swap_half_genes_combination_strategy(self):
        Constants.DATA = get_test_data()
        parent = default_dominating_individual()
        parent.problem.combination_strategy = default_combination_strategy
        child = default_other_dominating_individual()
        child.problem.combination_strategy = default_combination_strategy
        child.swap_half_genes(parent)
        values = [child.problem.get_value(k) for k in child.problem.keys()]
        self.assertEqual(values, [1, 3, 1])

    def test_eq(self):
        self.assertTrue(default_individual() == default_individual())
        self.assertFalse(default_individual() == default_dominating_individual())

    def test_str(self):
        self.assertEqual(
            "{'variables': {'0': 2, '1': 1, '2': 2}, 'constraints': [{'variables': ['0', '1']}, {'variables': ['2']}], 'objectives': [2, 1, 2]}",
            str(default_individual())
        )
