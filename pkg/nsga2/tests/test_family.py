import unittest

from pkg.nsga2.family import generate_children, get_parents, get_children
from pkg.nsga2.tests.test_util import default_individuals
from pkg.nsga2.tournament import get_tournament_pool
from pkg.random.random import Random


class FamilyTest(unittest.TestCase):
    def test_generate_children(self):
        individuals = default_individuals()
        children = generate_children(individuals, get_tournament_pool)
        self.assertEqual(len(children), 4)

    def test_get_parents(self):
        Random.begin_test()
        individuals = default_individuals()
        tournament_pool = get_tournament_pool(individuals)
        Random.set_test_value_for("random_choice", tournament_pool[0])
        Random.set_test_value_for("random_choice", tournament_pool[-1])
        mum, dad = get_parents(individuals, False)
        self.assertEqual(mum, tournament_pool[-1])
        self.assertEqual(dad, tournament_pool[0])
        Random.end_test()

    def test_get_children(self):
        Random.begin_test()
        for _ in range(4):
            Random.set_test_value_for("random_int_between_a_and_b", 1)
            Random.set_test_value_for("random_int_between_a_and_b", 2)
        individuals = default_individuals()
        son, daughter = get_children(individuals[0], individuals[1])
        son_values = [son.problem.get_value(k) for k in son.problem.keys()]
        daughter_values = [daughter.problem.get_value(k) for k in daughter.problem.keys()]
        self.assertEqual(son_values, [1, 2, 2])
        self.assertEqual(daughter_values, [0, 1, 1])
        Random.end_test()
