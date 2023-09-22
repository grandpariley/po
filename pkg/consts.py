from os import getenv

from pkg.log_level import LogLevel


class Constants:
    BUDGET_UTILIZATION = 0.80
    BUDGET = 20000.00
    NSGA2_NUM_GENERATIONS = 100
    NSGA2_NUM_GENES_MUTATING = 0.20
    MOEAD_NUM_GENERATIONS = 100
    MOEAD_NUM_CLOSEST_WEIGHT_VECTORS = 20

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'debug'))
