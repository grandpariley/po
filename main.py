from cache import file_cache
from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.moead import Moead
from pkg.evaluation.evaluation import Evaluation, INDEX_TO_LABEL
from pkg.parse.parse import parse_from_importer
from pkg.problem.builder import default_portfolio_optimization_problem_arch_2, generate_solutions_discrete_domain, \
    default_portfolio_optimization_problem_arch_1
from pkg.timer.timer import Timer


@limit_memory(percentage=0.9)
def main():
    for i in range(Constants.NUM_RUNS):
        Log.log("Run: " + str(i), "run")
        timer = Timer()
        options = parse_from_importer()
        problems = [default_portfolio_optimization_problem_arch_1(), default_portfolio_optimization_problem_arch_2()]
        solutions = get_solutions(problems, options, timer)
        evaluate(i, solutions, timer)


def evaluate(i, solutions, timer):
    result = Evaluation(i, solutions, timer)
    result.dump_solutions()
    result.dump_time()
    result.dump_graph(range(len(INDEX_TO_LABEL)), 3, 5)  # hack circular dependency lmao


@file_cache(filename='arch1-solutions.pkl')
def get_arch1_solutions(solutions, options, timer):
    return timer.time(Moead(solutions, options).solve, "arch1")


@file_cache(filename='arch2-solutions.pkl')
def get_arch2_solutions(solutions, options, timer):
    return timer.time(Moead(solutions, options).solve, "arch2")


@file_cache(filename='generated-solutions.pkl')
def get_generated_solutions(problem, options, timer):
    return timer.time(lambda: generate_solutions_discrete_domain(Constants.NUM_INDIVIDUALS, options, problem),
                      "generate")


def get_solutions(problems, options, timer):
    solutions = []
    Log.log("Generating solutions for arch 1", "generate")
    solutions[0] = get_generated_solutions(problems[0], options, timer)
    Log.log("Generating solutions for arch 2", "generate")
    solutions[1] = get_generated_solutions(problems[1], options, timer)
    Log.log("Starting to solve using MOEA/D for arch 1", "arch1")
    arch_1_solutions = get_arch1_solutions(solutions[0], options, timer)
    Log.log("Starting to solve using MOEA/D for arch 2", "arch2")
    arch_2_solutions = get_arch2_solutions(solutions[1], options, timer)
    Log.log("Showing results", "results")
    return {
        'arch1': arch_1_solutions,
        'arch2': arch_2_solutions
    }


if __name__ == '__main__':
    main()
