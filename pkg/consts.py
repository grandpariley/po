from os import getenv

from pkg.log_level import LogLevel


class Constants:
    BUDGET_UTILIZATION = 0.75
    BUDGET = 100.00
    NUM_INDIVIDUALS = 200
    NSGA2_NUM_GENERATIONS = 100
    NSGA2_NUM_GENES_MUTATING = 0.20
    MOEAD_NUM_GENERATIONS = 3
    MOEAD_NUM_CLOSEST_WEIGHT_VECTORS = 20

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
