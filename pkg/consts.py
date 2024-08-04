import json
import os.path
from os import getenv

from pkg.log_level import LogLevel
from pkg.parse.parse import parse_from_importer

_investors = []
_data = {}


def investors():
    global _investors
    if not os.path.exists('weights.json'):
        _investors = [
            {
                "person": "Alice",
                "description": "Risk tolerant; long time horizon; strong ESG preferences",
                "weights": {
                    "var": 0.05,
                    "cvar": 0.05,
                    "return": 0.05,
                    "environment": 0.3,
                    "governance": 0.25,
                    "social": 0.3
                }
            }
        ]
    if len(_investors) == 0:
        with open('weights.json', 'r') as json_file:
            _investors = json.load(json_file)
    return _investors


def data():
    global _data
    if not os.path.exists('data.json'):
        return {}
    if len(_data) == 0:
        _data = parse_from_importer('data.json')
    return _data


class Constants:
    RUN_FOLDER = 'most-recent-run'
    NUM_RUNS = 1
    BUDGET = 100000
    NUM_INDIVIDUALS = 1000
    NUM_GENERATIONS = 20
    GENES_MUTATING = 0.10
    MOEAD_NUM_WEIGHT_VECTORS_T = 50
    INVESTORS = investors()
    DATA = data()
    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
