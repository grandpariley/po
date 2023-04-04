from os import getenv

from pkg.log_level import LogLevel


class Constants:
    BUDGET = 10000.00
    NSGA2_NUM_INDIVIDUALS = 130
    NSGA2_NUM_GENERATIONS = 10
    NSGA2_NUM_GENES_MUTATING = 30

    GENERATE_ONLY = getenv('GENERATE_ONLY', 'false') == 'true'
    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
