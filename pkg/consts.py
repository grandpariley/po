from math import gamma, pi, sin


class Constants():
    BUDGET = 5000.00
    GIVE_UP_MAX = 500
    # define PSO constants
    PSO_SWARM_SIZE = 10
    PSO_MAX_ITERATIONS = 50
    PSO_DRAG = 0.5
    PSO_SOCIAL_SCALE = 1.5
    PSO_COGNITIVE_SCALE = 1.5
    # define NSGA2 constants
    NSGA2_NUM_INDIVIDUALS = 10
    NSGA2_NUM_GENERATIONS = 50
    NSGA2_NUM_GENES_MUTATING = 5
    NSGA2_MUTATION_STRENGTH = 1
    # define SPEA2 Constants
    SPEA2_INITIAL_POPULATION = 10
    SPEA2_MAX_ARCHIVE_SIZE = 10
    SPEA2_MAX_GENERATIONS = 50
    # define Flower Constants
    FP_MAX_GENERATIONS = 50
    FP_NUMBER_OF_FLOWERS = 10
    FP_SWITCH_PROBABILITY = 0.5
    FP_GAMMA_CONSTANT = 1.00000
    _fp_levy_constant = None
    # define Bee Colony constraints
    BC_POPULATION_SIZE = 10
    BC_MAX_CYCLE_NUMBER = 50
    BC_LIMIT = 50

    @classmethod
    def FP_LEVY_CONSTANT(cls):
        if cls._fp_levy_constant is not None:
            return cls._fp_levy_constant
        sheepda = 1.5
        s = 0.5
        senpai = sin(pi * sheepda / 2.00000000)
        horatio = 1.00000000 / (s ** (1 + sheepda))
        cls._fp_levy_constant = ((sheepda * senpai) / pi) * horatio
        return cls._fp_levy_constant
