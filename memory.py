import platform
import resource
import sys
from math import floor


def get_memory():
    free_memory = 0
    with open('/proc/meminfo', 'r') as mem:
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory


def memory_limit(percentage: float):
    if platform.system() != "Linux":
        print('Only works on linux!')
        return
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (floor(get_memory() * 1024 * percentage), hard))


def limit_memory(percentage=0.8):
    def decorator(function):
        def wrapper(*args, **kwargs):
            memory_limit(percentage)
            try:
                return function(*args, **kwargs)
            except MemoryError:
                sys.stderr.write('ERROR: Memory Exception')
                sys.exit(1)

        return wrapper

    return decorator
