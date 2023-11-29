from cache import file_cache
from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.moead import Moead
from pkg.nsga2.nsga2 import Nsga2
from pkg.plot.plot import Plot
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain
from pkg.timer.timer import Timer


@limit_memory(percentage=0.9)
def main():
    timer = Timer()
    problem, pos = default_portfolio_optimization_problem()
    solutions = get_cached_solutions(problem, pos, timer)
    plot_solutions(solutions, timer)


def plot_solutions(solutions, timer):
    plot = Plot(solutions, timer)
    plot.print(range(len(solutions['nsga2'][0].objective_values())))
    plot.compare()


@file_cache(filename='solutions.pkl')
def get_cached_solutions(problem, pos, timer):
    return get_solutions(problem, pos, timer)


@file_cache(filename='nsga2-solutions.pkl')
def get_cached_nsga2(solutions, pos, timer):
    return timer.time(Nsga2(solutions, pos).solve, "nsga2")


@file_cache(filename='moead-solutions.pkl')
def get_cached_moead(solutions, pos, timer):
    return timer.time(Moead(solutions, pos).solve, "moead")


def get_solutions(problem, pos, timer):
    Log.log("Begin generating solutions", "generate")
    solutions = timer.time(lambda: generate_solutions_discrete_domain(problem, pos, Constants.NUM_INDIVIDUALS),
                           "generate")
    Log.log("Generated! Starting to solve using NSGA-II", "nsga2")
    nsga2_soln = get_cached_nsga2(solutions, pos, timer)
    Log.log("Solved! Starting to solve using MOEA/D", "moead")
    moead_soln = get_cached_moead(solutions, pos, timer)
    Log.log("Solved! Showing results", "")
    return {
        'nsga2': nsga2_soln,
        'moead': moead_soln,
    }


if __name__ == '__main__':
    main()
