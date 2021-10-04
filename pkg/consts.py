from math import pi, sin
from os import getenv

from pkg.log_level import LogLevel

class Constants:
    CONTINUOUS_DOMAIN_ITERATION_LIMIT = 500
    BUDGET = 5000.00
    GIVE_UP_MAX = 500
    NSGA2_NUM_INDIVIDUALS = 100
    NSGA2_NUM_GENERATIONS = 10
    NSGA2_NUM_GENES_MUTATING = 5
    NSGA2_MUTATION_STRENGTH = 1

    LOG_LEVEL = LogLevel(getenv('LOG_LEVEL', 'none'))
    EXTERNAL_API = getenv('EXTERNAL_API', 'false') == 'true'
