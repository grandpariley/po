import asyncio
import json
import os.path
from os import getenv

from po.pkg.log_level import LogLevel
from po.pkg.parse.parse import parse_from_importer
from poimport import db

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
    if len(_data) == 0:
        _data = populate_data()
    return _data


def populate_data():
    if os.path.exists('po/data.json'):
        return parse_from_importer('po/data.json')
    else:
        return asyncio.run(db.fetch_data())


class Constants:
    NUM_RUNS = 1
    BUDGET = 30000
    NUM_INDIVIDUALS = 500
    NUM_GENERATIONS = 10
    GENES_MUTATING = 0.20
    MOEAD_NUM_WEIGHT_VECTORS_T = 50
    INVESTORS = investors()
    DATA = data()
    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
