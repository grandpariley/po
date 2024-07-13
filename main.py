from cache import file_cache
from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.moead import Moead
from pkg.evaluation.evaluation import Evaluation, INDEX_TO_LABEL
from pkg.parse.parse import parse_from_importer
from pkg.problem.builder import default_portfolio_optimization_problem_arch_2, generate_solutions_discrete_domain
from pkg.timer.timer import Timer


@limit_memory(percentage=0.9)
def main():
    for i in range(Constants.NUM_RUNS):
        Log.log("Run: " + str(i), "run")
        timer = Timer()
        options = parse_from_importer()
        problem = default_portfolio_optimization_problem_arch_2()
        solutions = get_solutions(problem, options, timer)
        evaluate(i, solutions, timer)


def evaluate(i, solutions, timer):
    result = Evaluation(i, solutions, timer)
    result.dump_solutions()
    result.dump_time()
    result.dump_graph(range(len(INDEX_TO_LABEL)), 3, 5)  # hack circular dependency lmao


@file_cache(filename='moead-solutions.pkl')
def get_moead_solutions(solutions, options, timer):
    return timer.time(Moead(solutions, options).solve, "moead")


@file_cache(filename='generated-solutions.pkl')
def get_generated_solutions(problem, options, timer):
    return timer.time(lambda: generate_solutions_discrete_domain(Constants.NUM_INDIVIDUALS, options, problem),
                      "generate")


def get_solutions(problem, options, timer):
    Log.log("Generating solutions", "generate")
    solutions = get_generated_solutions(problem, options, timer)
    Log.log("Starting to solve using MOEA/D", "moead")
    moead_solutions = get_moead_solutions(solutions, options, timer)
    Log.log("Showing results", "results")
    return {
        'moead': moead_solutions,
    }


if __name__ == '__main__':
    main()
