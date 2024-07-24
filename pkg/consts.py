import json
import os.path
from os import getenv

from pkg.log_level import LogLevel

_investors = []


def investors():
    global _investors
    if not os.path.exists('weights.json'):
        _investors = [
            {
                "person": "Sam",
                "description": "Balanced; wants to buy a house in 10 years; strong Environmental concerns",
                "weights": {
                    "VaR": 0.2,
                    "CVaR": 0.2,
                    "Return": 0.2,
                    "Environment": 0.4,
                    "Governance": 0.0,
                    "Social": 0.0
                }
            }
        ]
    if len(_investors) == 0:
        with open('weights.json', 'r') as json_file:
            _investors = json.load(json_file)
    return _investors


class Constants:
    NUM_RUNS = 10
    BUDGET_UTILIZATION = 0.80
    BUDGET = 2000.00
    NUM_INDIVIDUALS = 200
    NUM_GENERATIONS = 10
    NUM_GENES_MUTATING = 0.20
    MOEAD_NUM_WEIGHT_VECTORS_T = 20
    INVESTORS = investors()
    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
