from po.pkg.random.random import Random
from poimport import db

_data = dict()
_keys = []
_count = -1

async def keys():
    global _keys
    if len(_keys) == 0:
        _keys = await db.symbols()
    return _keys


async def count():
    global _count
    if _count <= 0:
        _count = await db.count()
    return _count


async def fetch(ticker):
    if Random.is_test():
        return get_test_data()[ticker]
    global _data
    if ticker in _data.keys():
        return _data[ticker]
    new_data = await db.fetch_data(ticker)
    _data[ticker] = new_data
    return new_data


def get_test_data():
    return {
        "0": {},
        "1": {},
        "2": {}
    }
