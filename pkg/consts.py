from os import getenv

from pkg.log_level import LogLevel


class Constants:
    NUM_RUNS = 10
    BUDGET_UTILIZATION = 0.80
    BUDGET = 100.00
    NUM_INDIVIDUALS = 100
    NUM_GENERATIONS = 10
    NUM_GENES_MUTATING = 0.20
    MOEAD_NUM_WEIGHT_VECTORS_T = 10

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
