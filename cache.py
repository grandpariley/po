import os, dill
from pkg.log import Log


def file_cache(filename='cache.pkl'):
    def decorator(function):
        def wrapper(*args, **kwargs):
            inputs = []
            if os.path.exists('inputs-' + filename):
                with open('inputs-' + filename, 'rb') as file:
                    inputs = dill.load(file)
            if os.path.exists(filename) and inputs == args:
                with open(filename, 'rb') as file:
                    Log.log("Hit cache for " + filename)
                    return dill.load(file)
            r = function(*args, **kwargs)
            with open(filename, 'wb') as file:
                dill.dump(r, file)
            with open('inputs-' + filename, 'wb') as file:
                dill.dump(args, file)
            return r

        return wrapper

    return decorator
