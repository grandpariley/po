import dill
import os

from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.moead import Moead
from pkg.nsga2.nsga2 import Nsga2
from pkg.plot.plot import Plot
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain
from pkg.timer.timer import Timer

SOLUTIONS_FILE = 'solutions.pkl'


@limit_memory(percentage=0.9)
def main():
    timer = Timer()
    problem, pos = default_portfolio_optimization_problem()
    solutions = get_cached_solutions(problem, pos, timer)
    plot = Plot(solutions, timer)
    plot.print(range(len(solutions['nsga2'].objective_values())))
    plot.compare()


def get_cached_solutions(problem, pos, timer):
    if os.path.exists(SOLUTIONS_FILE):
        with open(SOLUTIONS_FILE, 'rb') as file:
            Log.log("Hit solutions cache!")
            return dill.load(file)
    s = get_solutions(problem, pos, timer)
    with open(SOLUTIONS_FILE, 'wb') as file:
        dill.dump(s, file)
    return s


def get_solutions(problem, pos, timer):
    Log.log("Begin generating solutions", "generate")
    solutions = timer.time(lambda: generate_solutions_discrete_domain(problem, pos, Constants.NUM_INDIVIDUALS),
                           "generate")
    Log.log("Generated! Starting to solve using NSGA-II", "nsga2")
    nsga2_soln = timer.time(Nsga2(solutions, pos).solve, "nsga2")
    Log.log("Solved! Starting to solve using MOEA/D", "moead")
    moead_soln = timer.time(Moead(solutions, pos).solve, "moead")
    Log.log("Solved! Showing results", "")
    return {
        'nsga2': nsga2_soln,
        'moead': moead_soln,
    }


if __name__ == '__main__':
    main()
