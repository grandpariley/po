import json
import os.path
import shutil

from memory import limit_memory
from pkg.consts import Constants
from pkg.evaluation.evaluation import Evaluation, INDEX_TO_LABEL
from pkg.log import Log
from pkg.moead.moead import Moead
from pkg.problem.builder import default_portfolio_optimization_problem_arch_2, generate_solutions_discrete_domain, \
    default_portfolio_optimization_problem_arch_1
from pkg.problem.problem import problem_encoder_fn
from pkg.timer.timer import Timer
from progress import ProgressBar


@limit_memory(percentage=0.9)
def main():
    if os.path.exists('arch1'):
        shutil.rmtree('arch1')
    if os.path.exists('arch2'):
        shutil.rmtree('arch2')
    os.mkdir('arch1')
    os.mkdir('arch2')
    for i in range(Constants.NUM_RUNS):
        Log.log("Run: " + str(i), "run")
        timer = Timer()
        problems = [
            default_portfolio_optimization_problem_arch_1('Alice'),
            default_portfolio_optimization_problem_arch_2()
        ]
        solutions = get_solutions(i, problems, timer)
        evaluate(i, solutions, timer)


def get_solutions(run, problems, timer):
    solutions = []
    Log.log("Generating solutions for arch 1", "generate")
    solutions.append(timer.time(lambda: generate_solutions_discrete_domain(problems[0]), "generate"))
    Log.log("Generating solutions for arch 2", "generate")
    solutions.append(timer.time(lambda: generate_solutions_discrete_domain(problems[1]), "generate"))
    Log.log("Generating complete!")
    arch1_folder = 'arch1/' + str(run)
    arch2_folder = 'arch2/' + str(run)
    save_generated_solutions(arch1_folder, solutions[0])
    save_generated_solutions(arch2_folder, solutions[1])
    Log.log("Starting to solve using MOEA/D for arch 1", "arch1")
    arch1_solutions = timer.time(Moead(solutions[0], arch1_folder).solve, "arch1")
    Log.log("Starting to solve using MOEA/D for arch 2", "arch2")
    arch2_solutions = timer.time(Moead(solutions[1], arch2_folder).solve, "arch2")
    return {
        'arch1': arch1_solutions,
        'arch2': arch2_solutions
    }


def save_generated_solutions(folder, solutions):
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(folder + '/generated-solutions.json', 'w') as json_file:
        json.dump(solutions, json_file, default=problem_encoder_fn)


def evaluate(i, solutions, timer):
    ProgressBar.begin(3)
    result = Evaluation(i, solutions, timer)
    ProgressBar.update(1)
    result.dump_time()
    ProgressBar.update(2)
    result.dump_graph({
        "arch1": ['objectives'],
        "arch2": range(len(INDEX_TO_LABEL))
    }, 2, 5, 'Alice')
    ProgressBar.update(3)
    ProgressBar.end()

if __name__ == '__main__':
    main()
