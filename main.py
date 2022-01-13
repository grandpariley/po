from pkg.moboa.moboa import Moboa
from copy import deepcopy
from pkg.consts import Constants
from pkg.nsga2.nsga2 import Nsga2
from pkg.plot.plot import Plot
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain
from pkg.timer.timer import Timer


def main():
    timer = Timer()
    problem = default_portfolio_optimization_problem()
    nsga2_problems = timer.time(lambda: generate_solutions_discrete_domain(problem, Constants.NSGA2_NUM_INDIVIDUALS),
                                "generate nsga2")
    nsga2_soln = timer.time(Nsga2(nsga2_problems).solve, "nsga2")
    moboa_problems = timer.time(lambda: generate_solutions_discrete_domain(problem, Constants.MOBOA_NUM_INDIVIDUALS),
                                "generate moboa")
    moboa_soln = timer.time(Moboa(moboa_problems).solve, "moboa")
    nsga2_problems = generate_solutions_discrete_domain(deepcopy(problem), Constants.NSGA2_NUM_INDIVIDUALS)
    nsga2 = Nsga2(nsga2_problems)
    nsga2_soln = timer.time(nsga2.solve, "nsga2")
    solutions = {
        'nsga2': nsga2_soln,
        'moboa': moboa_soln,
    }
    plot = Plot(solutions, timer)
    plot.print()
    plot.compare()


if __name__ == '__main__':
    main()
