from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.nsga2.nsga2 import Nsga2
from pkg.plot.plot import Plot
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain
from pkg.timer.timer import Timer


@limit_memory(percentage=0.9)
def main():
    timer = Timer()
    problem, pos = default_portfolio_optimization_problem()
    Log.log("Begin generating solutions", "generate")
    solutions = timer.time(lambda: generate_solutions_discrete_domain(problem, pos, Constants.NSGA2_NUM_INDIVIDUALS),
                           "generate")
    Log.log("Generated! Starting to solve using NSGA-II", "nsga2")
    nsga2_soln = timer.time(Nsga2(solutions, pos).solve, "nsga2")
    solutions = {
        'nsga2': nsga2_soln,
    }
    plot = Plot(solutions, timer)
    plot.print()


if __name__ == '__main__':
    main()
