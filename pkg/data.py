import asyncio
import os

from po.memory import get_memory
from po.pkg.parse.parse import parse_from_importer
from po.pkg.random.random import Random
from poimport import db

_data = []

def keys():
    return data().keys()


def count():
    return len(data().keys())


def fetch(ticker):
    return data()[ticker]


def data():
    global _data
    if len(_data) == 0:
        _data = populate_data()
    return _data


def populate_data():
    if Random.is_test():
        return get_test_data()
    if os.path.exists('po/data.json'):
        return parse_from_importer('po/data.json')
    else:
        print("populating data from db ...")
        d = asyncio.run(db.fetch_data())
        print("remaining memory: " + str(get_memory()) + " kB")
        return d


def get_test_data():
    return {
        "0": {},
        "1": {},
        "2": {}
    }
