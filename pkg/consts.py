import json
import os.path
from os import getenv

from po.pkg.log_level import LogLevel

_investors = []


def investors():
    global _investors
    if not os.path.exists('weights.json'):
        _investors = [
            {
                "person": "Alice",
                "description": "the Balanced Corporate Governance Nerd",
                "weights": {
                    "var": 0.15,
                    "cvar": 0.15,
                    "return": 0.1,
                    "environment": 0.0,
                    "governance": 0.0,
                    "social": 0.6
                }
            },
            {
                "person": "Jars",
                "description": "the Long-Time-Horizon ESG? ES-shmee Investor",
                "weights": {
                    "var": 0.45,
                    "cvar": 0.45,
                    "return": 0.1,
                    "environment": 0.0,
                    "governance": 0.0,
                    "social": 0.0
                }
            },
            {
                "person": "Sam",
                "description": "the Conservative Socially Conscious",
                "weights": {
                    "var": 0.05,
                    "cvar": 0.05,
                    "return": 0.1,
                    "environment": 0.3,
                    "governance": 0.3,
                    "social": 0.2
                }
            }
        ]
    if len(_investors) == 0:
        with open('weights.json', 'r') as json_file:
            _investors = json.load(json_file)
    return _investors


class Constants:
    DIVERSITY = 15
    BUDGET_UTILIZATION = 0.7
    NUM_RUNS = 1
    BUDGET = 100000
    NUM_INDIVIDUALS = 500
    NUM_GENERATIONS = 10
    GENES_MUTATING = 0.20
    MOEAD_NUM_WEIGHT_VECTORS_T = 50
    MEM_UTILIZATION = 0.8
    INVESTORS = investors()
    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
