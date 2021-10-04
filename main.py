from pkg.problem.builder import default_portfolio_optimization_problem, generate_many_random_solutions
from pkg.problem.compare import compare_solutions
from pkg.nsga2.nsga2 import Nsga2
from pkg.timer.timer import Timer
from pkg.problem.builder import stock_names
from copy import deepcopy


def main():
    timer = Timer()
    problem = default_portfolio_optimization_problem()
    timer.time(lambda: generate_many_random_solutions(problem, 10), "generate")
    nsga2 = Nsga2(deepcopy(problem))
    nsga2_soln = timer.time(nsga2.solve, "nsga2")
    solutions = {
        'nsga2': nsga2_soln,
    }
    print("Solutions: ")
    for name in solutions:
        print(name + ": ")
        for soln in solutions[name]:
            print("\trisk: " + str(-soln.objective_values()[0]))
            print("\treward: " + str(soln.objective_values()[1]))
            print("\tbudget: " + str(sum([s.get_value() * s.get_objective_info()['price'] for s in soln.variables])))
            for i in range(len(stock_names)):
                print("\t\t" + stock_names[i] + ": " + str(soln.variable_assignments()[i]))
            print()
        print()
    solution_compare = compare_solutions(solutions)
    non_dominated_str = ""
    for name in solution_compare:
        if solution_compare[name]:
            non_dominated_str += name + ", "
    non_dominated_str = non_dominated_str[0:-2]
    print(non_dominated_str + " have solutions that are not dominated by other solutions")
    print(timer.get_times_as_formatted_str())


if __name__ == '__main__':
    main()
