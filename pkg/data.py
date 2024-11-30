import asyncio

import ioloop

from po.pkg.log import Log
from po.pkg.random.random import Random
from poimport import db

_data = dict()
_keys = []
_count = -1

def keys():
    global _keys
    if len(_keys) == 0:
        _keys = db.symbols()
        Log.log("HEY IT'S KEYS" + str(_keys))
    return _keys


def count():
    global _count
    if _count <= 0:
        _count = db.count()
        Log.log("HEY IT'S COUNT" + str(_count))
    return _count


def fetch(ticker):
    if Random.is_test():
        return get_test_data()[ticker]
    global _data
    if ticker in _data.keys():
        return _data[ticker]
    new_data = db.fetch_data(ticker)
    _data[ticker] = new_data
    Log.log("HEY IT'S DATA" + str(new_data))
    return new_data


def get_test_data():
    return {
        "0": {},
        "1": {},
        "2": {}
    }
