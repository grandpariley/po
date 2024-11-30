import unittest

from po.pkg.consts import Constants
from po.pkg.moead.tests.test_util import default_dominated_individual
from po.pkg.parse.parse import get_portfolio_option_from_data
from po.pkg.problem.builder import generate_solutions_discrete_domain, default_portfolio_optimization_problem_arch_2, \
    portfolio_optimization_combination_strategy
from po.pkg.problem.tests.default_problems import default_consistent_problem_set_values, \
    default_other_consistent_problem_set_values
from po.pkg.random.random import Random


def get_default_data():
    return {
        "BKI.TO": {
            "ticker": "BKI.TO",
            "price": 0.05,
            "return": 0.20559082643598406,
            "cvar": 0.00039570213032859004,
            "var": 0.0005623721522929325,
            "environment": None,
            "governance": None,
            "social": None
        },
        "BLCO": {
            "ticker": "BLCO",
            "price": 15.94,
            "return": 0.08940554954151672,
            "cvar": 0.0001249700268012922,
            "var": 0.00015278353801098635,
            "environment": None,
            "governance": None,
            "social": None
        },
        "BLDP": {
            "ticker": "BLDP",
            "price": 2.67,
            "return": 0.2221303825492562,
            "cvar": 0.00022870169342460763,
            "var": 0.00032945291957550455,
            "environment": None,
            "governance": None,
            "social": None
        },
        "BLN.TO": {
            "ticker": "BLN.TO",
            "price": 4.5,
            "return": 0.19640218415083288,
            "cvar": 0.00018072656381530776,
            "var": 0.00027609977110681856,
            "environment": None,
            "governance": None,
            "social": None
        },
        "BLX": {
            "ticker": "BLX",
            "price": 31.79,
            "return": 0.16117905539108662,
            "cvar": 0.00011893488649589012,
            "var": 0.00019778672976864323,
            "environment": None,
            "governance": None,
            "social": None
        },
        "BMO": {
            "ticker": "BMO",
            "price": 86.64,
            "return": 0.16138324744186777,
            "cvar": 8.010603913128042e-05,
            "var": 0.00012292360423323898,
            "environment": 0.08270676691729324,
            "governance": 0.393206381883685,
            "social": 0.31144872490504616
        },
        "BN": {
            "ticker": "BN",
            "price": 46.01,
            "return": 0.21549414089886923,
            "cvar": 8.95466105707872e-05,
            "var": 0.0001372280445255943,
            "environment": 0.03494029190623618,
            "governance": 0.5193000514668039,
            "social": 0.4829083016820402
        },
        "BNGO": {
            "ticker": "BNGO",
            "price": 0.6592,
            "return": 0.2875739348246108,
            "cvar": 0.000670729761743193,
            "var": 0.0009986505230311232,
            "environment": None,
            "governance": None,
            "social": None
        },
        "BNRE": {
            "ticker": "BNRE",
            "price": 45.97,
            "return": 0.21865911768597687,
            "cvar": 0.00010887626146529753,
            "var": 0.00015716082655362632,
            "environment": None,
            "governance": None,
            "social": None
        },
        "BNS": {
            "ticker": "BNS",
            "price": 47.06,
            "return": 0.14035146621141056,
            "cvar": 7.852496133387945e-05,
            "var": 0.00012433101525973316,
            "environment": 0.06899601946041575,
            "governance": 0.45702521873391666,
            "social": 0.5263157894736842
        },
        "CARS": {
            "ticker": "CARS",
            "price": 19.1,
            "return": 0.26776730589884046,
            "cvar": 0.00018718728959348177,
            "var": 0.0002932426265249015,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CASH": {
            "ticker": "CASH",
            "price": 59.45,
            "return": 0.11145829102587958,
            "cvar": 0.00013149904619135568,
            "var": 0.0002185909084341916,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CIF": {
            "ticker": "CIF",
            "price": 1.7358,
            "return": 0.12034064523485907,
            "cvar": 7.860120618527781e-05,
            "var": 0.00012690008272189728,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CIGI": {
            "ticker": "CIGI",
            "price": 123.82,
            "return": 0.20630549861371805,
            "cvar": 0.00011303083104853121,
            "var": 0.00017364691960617751,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CINF": {
            "ticker": "CINF",
            "price": 122.34,
            "return": 0.10839541026416252,
            "cvar": 8.361168532273058e-05,
            "var": 0.00013696481576725607,
            "environment": 0.07784166298098187,
            "governance": 0.662892434379825,
            "social": 0.5952251763429192
        },
        "CINT": {
            "ticker": "CINT",
            "price": 5.52,
            "return": 0.15668683027390157,
            "cvar": 0.00023877422921217311,
            "var": 0.0003642660073004488,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CIX": {
            "ticker": "CIX",
            "price": 23.26,
            "return": 0.11983016510790624,
            "cvar": 0.00015025721669733157,
            "var": 0.00022522753281290503,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CJT.TO": {
            "ticker": "CJT.TO",
            "price": 132.9,
            "return": 0.13820744967820864,
            "cvar": 0.00010647915091184443,
            "var": 0.00016443939141270688,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CKISF": {
            "ticker": "CKISF",
            "price": 6.06,
            "return": 0.12983557559618197,
            "cvar": 7.41359290681162e-05,
            "var": 0.00016623841840721418,
            "environment": 0.778858911985847,
            "governance": 0.37364899639732374,
            "social": 0.7064568638090071
        },
        "CLF": {
            "ticker": "CLF",
            "price": 16.17,
            "return": 0.24755229287150782,
            "cvar": 0.00015476218931683735,
            "var": 0.00024525136999049076,
            "environment": None,
            "governance": None,
            "social": None
        },
        "CLG.F": {
            "ticker": "CLG.F",
            "price": 79.5,
            "return": 0.20712226681684257,
            "cvar": 0.00022700114948600843,
            "var": 0.00039049198716982795,
            "environment": None,
            "governance": None,
            "social": None
        }
    }


def set_random_test_values():
    Random.set_test_value_for("random_choice", 'CINF')
    Random.set_test_value_for("random_choice", 1)
    Random.set_test_value_for("random_choice", 'CIX')
    Random.set_test_value_for("random_choice", 'CASH')
    Random.set_test_value_for("random_choice", 'BNS')
    Random.set_test_value_for("random_choice", 'BNRE')
    Random.set_test_value_for("random_choice", 'BN')
    Random.set_test_value_for("random_choice", 'CIGI')
    Random.set_test_value_for("random_choice", 2)
    Random.set_test_value_for("random_choice", 'CINT')
    Random.set_test_value_for("random_choice", 8)
    Random.set_test_value_for("random_choice", 'CLG.F')
    Random.set_test_value_for("random_choice", 45)
    Random.set_test_value_for("random_choice", 'CJT.TO')
    Random.set_test_value_for("random_choice", 89)
    Random.set_test_value_for("random_choice", 'CKISF')
    Random.set_test_value_for("random_choice", 2)
    Random.set_test_value_for("random_choice", 'CLF')
    Random.set_test_value_for("random_choice", 50)
    Random.set_test_value_for("random_choice", 'CIF')
    Random.set_test_value_for("random_choice", 1)
    Random.set_test_value_for("random_choice", 'BLX')
    Random.set_test_value_for("random_choice", 19)
    Random.set_test_value_for("random_choice", 'BLN.TO')
    Random.set_test_value_for("random_choice", 40)
    Random.set_test_value_for("random_choice", 'BLDP')
    Random.set_test_value_for("random_choice", 180)
    Random.set_test_value_for("random_choice", 'BLCO')
    Random.set_test_value_for("random_choice", 300)
    Random.set_test_value_for("random_choice", 'BKI.TO')
    Random.set_test_value_for("random_choice", 500)
    Random.set_test_value_for("random_choice", 'BNGO')
    Random.set_test_value_for("random_choice", 100)
    Random.set_test_value_for("random_choice", 'CARS')
    Random.set_test_value_for("random_choice", 200)
    Random.set_test_value_for("random_choice", 'BMO')


class BuilderTest(unittest.TestCase):
    def test_generate_solutions_discrete_domain(self):
        Constants.BUDGET = 30000
        Constants.NUM_INDIVIDUALS = 1
        Random.begin_test()
        set_random_test_values()
        solutions = generate_solutions_discrete_domain(
            default_portfolio_optimization_problem_arch_2()
        )
        Random.end_test()
        self.assertEqual(
            "[{'variables': {'BMO': 200, 'CARS': 100, 'BNGO': 500, 'BKI.TO': 300, 'BLCO': 180, 'BLDP': 40, 'BLN.TO': 19, 'BLX': 1, 'CIF': 50, 'CLF': 2, 'CKISF': 89, 'CJT.TO': 45, 'CLG.F': 8, 'CINT': 2, 'CIX': 1}, 'constraints': ['budget'], 'objectives': [-0.5420839279529841, -0.8011769208810373, 319.7656504663144, 85.85979655019904, 111.8960370560988, 125.16440586001087]}]",
            str(solutions)
        )

    def test_portfolio_optimization_combination_strategy(self):
        child = default_consistent_problem_set_values()
        portfolio_optimization_combination_strategy(
            child,
            default_other_consistent_problem_set_values()
        )
        self.assertEqual([3, 2, 2], [v.get_value() for v in child.variables.values()])
