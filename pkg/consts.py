from os import getenv

from pkg.log_level import LogLevel

class Constants:
    CONTINUOUS_DOMAIN_ITERATION_LIMIT = 500
    BUDGET = 50000.00
    GIVE_UP_MAX = 100
    NSGA2_NUM_INDIVIDUALS = 20
    NSGA2_NUM_GENERATIONS = 2
    NSGA2_NUM_GENES_MUTATING = 3
    NSGA2_MUTATION_STRENGTH = 2

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'none'))
    EXTERNAL_API = getenv('EXTERNAL_API', 'false') == 'true'
