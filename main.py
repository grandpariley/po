import json

from cache import file_cache
from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.moead import Moead, get_non_dominated
from pkg.evaluation.evaluation import Evaluation, INDEX_TO_LABEL
from pkg.parse.parse import parse_from_importer
from pkg.problem.builder import default_portfolio_optimization_problem_arch_2, generate_solutions_discrete_domain, \
    default_portfolio_optimization_problem_arch_1
from pkg.problem.problem import problem_encoder_fn
from pkg.timer.timer import Timer


@limit_memory(percentage=0.9)
def main():
    for i in range(Constants.NUM_RUNS):
        Log.log("Run: " + str(i), "run")
        timer = Timer()
        problems = [
            # default_portfolio_optimization_problem_arch_1('Alice'),
            default_portfolio_optimization_problem_arch_2()
        ]
        solutions = get_solutions(problems, timer)
        evaluate(i, solutions, timer)


def evaluate(i, solutions, timer):
    result = Evaluation(i, solutions, timer)
    result.dump_solutions()
    result.dump_time()
    result.dump_graph({
        # "arch1": ['objectives'],
        "arch2": range(len(INDEX_TO_LABEL))
    }, 2, 5, 'Alice')


# @file_cache(filename='arch1-solutions.pkl')
def get_arch1_solutions(solutions, timer):
    return timer.time(Moead(solutions).solve, "arch1")


# @file_cache(filename='arch2-solutions.pkl')
def get_arch2_solutions(solutions, timer):
    return timer.time(Moead(solutions).solve, "arch2")


# @file_cache(filename='arch1-generated-solutions.pkl')
def get_generated_solutions_arch1(problem, timer):
    return timer.time(lambda: generate_solutions_discrete_domain(Constants.NUM_INDIVIDUALS, problem),
                      "generate")


# @file_cache(filename='arch2-generated-solutions.pkl')
def get_generated_solutions_arch2(problem, timer):
    return timer.time(lambda: generate_solutions_discrete_domain(Constants.NUM_INDIVIDUALS, problem),
                      "generate")


# @file_cache(filename='get-solutions.pkl')
def get_solutions(problems, timer):
    solutions = []
    # Log.log("Generating solutions for arch 1", "generate")
    # solutions.append(get_generated_solutions_arch1(problems[0], timer))
    Log.log("Generating solutions for arch 2", "generate")
    solutions.append(get_generated_solutions_arch2(problems[0], timer))
    with open('generated-solutions.json', 'w') as json_file:
        json.dump(solutions[0], json_file, default=problem_encoder_fn)
    # Log.log("Starting to solve using MOEA/D for arch 1", "arch1")
    # arch_1_solutions = get_arch1_solutions(solutions[0], timer)
    Log.log("Starting to solve using MOEA/D for arch 2", "arch2")
    arch_2_solutions = get_arch2_solutions(solutions[0], timer)
    return {
        # 'arch1': arch_1_solutions,
        'arch2': arch_2_solutions
    }


if __name__ == '__main__':
    main()
