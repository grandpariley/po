from os import getenv

from pkg.log_level import LogLevel


class Constants:
    BUDGET = 3500.00
    NSGA2_GIVE_UP_MAX = 5
    NSGA2_NUM_INDIVIDUALS = 20
    NSGA2_NUM_GENERATIONS = 2
    NSGA2_NUM_GENES_MUTATING = 3
    NSGA2_MUTATION_STRENGTH = 2
    MOBOA_NUM_INDIVIDUALS = 20

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'none'))
    EXTERNAL_API = getenv('EXTERNAL_API', 'false') == 'true'
