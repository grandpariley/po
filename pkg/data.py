import gc

from po.memory import get_memory, get_limit
from po.pkg.consts import Constants
from po.pkg.log import Log
from po.pkg.random.random import Random
from poimport import db

_data = dict()
_keys = []
_count = -1

async def keys():
    global _keys
    if len(_keys) == 0:
        _keys = await db.symbols()
    else:
        Log.log("hit key cache")
    return _keys


async def count():
    global _count
    if _count <= 0:
        _count = await db.count()
    else:
        Log.log("hit count cache")
    return _count


async def fetch(ticker):
    if Random.is_test():
        return get_test_data()[ticker]
    global _data
    if ticker in _data.keys():
        Log.log("hit data cache")
        return _data[ticker]
    if get_memory() > (Constants.MEM_UTILIZATION * get_limit()):
        Log.log("remove cache - memory too high")
        del _data
        gc.collect()
        _data = dict()
    new_data = await db.fetch_data(ticker)
    _data[ticker] = new_data
    return new_data


def get_test_data():
    return {
        "0": {},
        "1": {},
        "2": {}
    }
