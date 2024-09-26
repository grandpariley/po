from po.pkg.consts import Constants
from po.pkg.log import Log
from po.pkg.moead.moead import Moead
from po.pkg.problem.builder import generate_solutions_discrete_domain, default_portfolio_optimization_problem_arch_1, \
    default_portfolio_optimization_problem_arch_2
from po.memory import limit_memory


def get_solutions(problems):
    input_solutions = {}
    for name, problem in problems.items():
        Log.log("Generating solutions for " + name, "generate")
        input_solutions[name] = generate_solutions_discrete_domain(problem)
    Log.log("Generating complete!")
    output_solutions = {}
    for name in problems.keys():
        Log.log("Starting to solve using MOEA/D for " + name, name)
        output_solutions[name] = Moead(input_solutions[name]).solve()
    return output_solutions


@limit_memory(percentage=0.9)
def main(problems):
    for run in range(Constants.NUM_RUNS):
        Log.log("Run: " + str(run), "run")
        return get_solutions(problems)


if __name__ == '__main__':
    main({
        'arch1-alice': default_portfolio_optimization_problem_arch_1('Alice'),
        'arch1-jars': default_portfolio_optimization_problem_arch_1('Jars'),
        'arch1-sam': default_portfolio_optimization_problem_arch_1('Sam'),
        'arch2': default_portfolio_optimization_problem_arch_2(),
    })
