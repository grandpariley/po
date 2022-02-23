from os import getenv

from pkg.log_level import LogLevel


class Constants:
    BUDGET = 10000.00
    NSGA2_NUM_INDIVIDUALS = 10
    NSGA2_NUM_GENERATIONS = 5
    NSGA2_NUM_GENES_MUTATING = 30

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
    EXTERNAL_API = getenv('EXTERNAL_API', 'false') == 'true'
