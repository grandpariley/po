import json
import os.path
import shutil

from memory import limit_memory
from pkg.consts import Constants
from pkg.log import Log
from pkg.moead.moead import Moead
from pkg.problem.builder import default_portfolio_optimization_problem_arch_2, generate_solutions_discrete_domain, \
    default_portfolio_optimization_problem_arch_1
from pkg.problem.problem import problem_encoder_fn
from pkg.timer.timer import Timer

PROBLEMS = {
    'arch1': default_portfolio_optimization_problem_arch_1('Alice'),
    'arch2': default_portfolio_optimization_problem_arch_2(),
}


def create_output_folders():
    for folder in PROBLEMS.keys():
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)


def save_solutions(folder, filename, solutions):
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(folder + '/' + filename + '.json', 'w') as json_file:
        json.dump(solutions, json_file, default=problem_encoder_fn)


def get_solutions(run, timer):
    input_solutions = {}
    for name, problem in PROBLEMS.items():
        Log.log("Generating solutions for " + name, "generate")
        input_solutions[name] = timer.time(lambda: generate_solutions_discrete_domain(problem), name + '/' + run)
    Log.log("Generating complete!")
    for name in PROBLEMS.keys():
        save_solutions(name + '/' + run, 'initial', input_solutions[name])
    output_solutions = {}
    for name in PROBLEMS.keys():
        Log.log("Starting to solve using MOEA/D for " + name, name)
        output_solutions[name] = timer.time(Moead(input_solutions[name], name + '/' + run).solve, name + '/' + run)
    return output_solutions


@limit_memory(percentage=0.9)
def main():
    create_output_folders()
    for run in range(Constants.NUM_RUNS):
        Log.log("Run: " + str(run), "run")
        timer = Timer()
        solutions = get_solutions(str(run), timer)
        timer.save()
        for name in PROBLEMS.keys():
            save_solutions(name + '/' + str(run), 'solutions', solutions[name])


if __name__ == '__main__':
    main()
