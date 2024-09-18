import unittest

from po.pkg.consts import Constants
from po.pkg.moead.moead import Moead, get_non_dominated, is_non_dominated
from po.pkg.moead.tests.test_util import default_individual_with_values, default_dominated_individual, \
    default_dominating_individual, default_other_dominating_individual
from po.pkg.problem.tests.default_problems import default_consistent_problem, get_test_data
from po.pkg.random.random import Random


def get_population():
    return [
        default_individual_with_values(),
        default_dominated_individual(),
        default_dominating_individual(),
        default_other_dominating_individual()
    ]


class MoeadTest(unittest.TestCase):

    def test_is_non_dominated(self):
        self.assertTrue(is_non_dominated(default_other_dominating_individual(), get_population()))
        self.assertFalse(is_non_dominated(default_dominated_individual(), get_population()))

    def test_get_non_dominated(self):
        non_dominated = get_non_dominated(get_population())
        self.assertEqual(
            [default_other_dominating_individual()],
            non_dominated
        )
