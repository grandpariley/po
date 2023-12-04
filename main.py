from cache import file_cache
from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.moead import Moead
from pkg.nsga2.nsga2 import Nsga2
from pkg.evaluation.evaluation import Evaluation, INDEX_TO_LABEL
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain
from pkg.timer.timer import Timer


@limit_memory(percentage=0.9)
def main():
    for i in Constants.NUM_RUNS:
        timer = Timer()
        problem, pos = default_portfolio_optimization_problem()
        solutions = get_solutions(problem, pos, timer)
        evaluate(i, solutions, timer)


def evaluate(i, solutions, timer):
    eval = Evaluation(i, solutions, timer)
    eval.dump_solutions()
    eval.dump_time()
    eval.dump_metrics()
    eval.dump_graph(range(len(INDEX_TO_LABEL)), 3, 5)  # hack circular dependency lmao


# @file_cache(filename='nsga2-solutions.pkl')
def get_cached_nsga2(solutions, pos, timer):
    return timer.time(Nsga2(solutions, pos).solve, "nsga2")


# @file_cache(filename='moead-solutions.pkl')
def get_cached_moead(solutions, pos, timer):
    return timer.time(Moead(solutions, pos).solve, "moead")


# @file_cache(filename='generated-solutions.pkl')
def get_cached_generated_solutions(problem, pos, timer):
    return timer.time(lambda: generate_solutions_discrete_domain(Constants.NUM_INDIVIDUALS, pos, problem),
                      "generate")


def get_solutions(problem, pos, timer):
    Log.log("Generating solutions", "generate")
    solutions = get_cached_generated_solutions(problem, pos, timer)
    Log.log("Starting to solve using NSGA-II", "nsga2")
    nsga2_soln = get_cached_nsga2(solutions, pos, timer)
    Log.log("Starting to solve using MOEA/D", "moead")
    moead_soln = get_cached_moead(solutions, pos, timer)
    Log.log("Showing results", "results")
    return {
        'nsga2': nsga2_soln,
        'moead': moead_soln,
    }


if __name__ == '__main__':
    main()
