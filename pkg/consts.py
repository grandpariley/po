import json
from os import getenv

from pkg.log_level import LogLevel

_investors = []


def investors():
    if len(_investors) == 0:
        with open('weights.json', 'r') as json_file:
            global _investors
            _investors = json.load(json_file)
    return _investors


class Constants:
    NUM_RUNS = 10
    BUDGET_UTILIZATION = 0.80
    BUDGET = 1000.00
    NUM_INDIVIDUALS = 100
    NUM_GENERATIONS = 10
    NUM_GENES_MUTATING = 0.20
    MOEAD_NUM_WEIGHT_VECTORS_T = 10
    INVESTORS = investors()
    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
