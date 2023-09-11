from os import getenv

from pkg.log_level import LogLevel


class Constants:
    BUDGET_UTILIZATION = 0.80
    BUDGET = 20000.00
    NSGA2_NUM_INDIVIDUALS = 300
    NSGA2_NUM_GENERATIONS = 100
    NSGA2_NUM_GENES_MUTATING = 0.20

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
