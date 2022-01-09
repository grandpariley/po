from pkg.consts import Constants
from pkg.moboa.moboa import Moboa
from pkg.nsga2.nsga2 import Nsga2
from pkg.problem.builder import default_portfolio_optimization_problem, generate_solutions_discrete_domain, stock_names
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
    solutions = {
        'nsga2': nsga2_soln,
        'moboa': moboa_soln,
    }
    print("Solutions: ")
    for name in solutions:
        print(name + ": ")
        for soln in solutions[name]:
            print("\trisk: " + str(soln.objective_values()[0]))
            print("\treward: " + str(soln.objective_values()[1]))
            print("\tbudget: " + str(sum([s.get_value() * s.get_objective_info()['price'] for s in soln.variables])))
            for i in range(len(stock_names)):
                print("\t\t" + stock_names[i] + ": " + str(soln.variable_assignments()[i]))
            print()
        print()
    # solution_compare = compare_solutions(solutions)
    # non_dominated_str = ""
    # for name in solution_compare:
    #     if solution_compare[name]:
    #         non_dominated_str += name + ", "
    # non_dominated_str = non_dominated_str[0:-2]
    # print(non_dominated_str + " have solutions that are not dominated by other solutions")
    # print(timer.get_times_as_formatted_str())


if __name__ == '__main__':
    main()
