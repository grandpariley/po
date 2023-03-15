from pkg.consts import Constants
from pkg.log import Log
from pkg.nsga2.nsga2 import Nsga2
from pkg.plot.plot import Plot
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain
from pkg.timer.timer import Timer


def main():
    timer = Timer()
    problem = default_portfolio_optimization_problem()
    Log.log("Begin generating solutions for NSGA-II")
    nsga2_problems = timer.time(lambda: generate_solutions_discrete_domain(problem, Constants.NSGA2_NUM_INDIVIDUALS),
                                "generate")
    Log.log("Generated! Starting to solve using NSGA-II")
    nsga2_soln = timer.time(Nsga2(nsga2_problems).solve, "nsga2")
    Log.log("Begin generating solutions for ASDNSGA-II")
    # asdnsga2_problems = timer.time(lambda: generate_solutions_discrete_domain(problem, Constants.NSGA2_NUM_INDIVIDUALS),
    #                                "generate")
    # Log.log("Generated! Starting to solve using ASDNSGA-II")
    # asdnsga2_soln = timer.time(Asdnsga2(asdnsga2_problems).solve, "asdnsga2")
    # Log.log("Done!")
    solutions = {
        'nsga2': nsga2_soln,
        # 'asdnsga2': asdnsga2_soln,
    }
    plot = Plot(solutions, timer)
    plot.print()
    # plot.compare()


if __name__ == '__main__':
    main()
