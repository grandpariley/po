import os, dill
from po.pkg.log import Log


def file_cache(filename='cache.pkl'):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if os.path.exists(filename):
                with open(filename, 'rb') as file:
                    Log.log("Hit cache for " + filename)
                    return dill.load(file)
            r = function(*args, **kwargs)
            with open(filename, 'wb') as file:
                dill.dump(r, file)
            return r

        return wrapper

    return decorator
