from pkg.problem.builder import default_portfolio_optimization_problem
from pkg.problem.compare import compareSolutions
from pkg.beecolony.bee_colony import BeeColony
from pkg.branchbound.branch_bound import BranchBound
from pkg.flowerpollination.flower_pollination import FlowerPollination 
from pkg.nsga2.nsga2 import Nsga2
from pkg.pso.pso import Pso 
from pkg.spea2.spea2 import Spea2 
from pkg.timer.timer import Timer

def main():
    timer = Timer()

    branch_bound = BranchBound(default_portfolio_optimization_problem())
    branch_bound_soln = timer.time(branch_bound.solve, "branch_bound")
    bee_colony = BeeColony(default_portfolio_optimization_problem())
    bee_colony_soln = timer.time(bee_colony.solve, "bee_colony")
    flower_pollination = FlowerPollination(default_portfolio_optimization_problem())
    flower_pollination_soln = timer.time(flower_pollination.solve, "flower_pollination")
    nsga2 = Nsga2(default_portfolio_optimization_problem())
    nsga2_soln = timer.time(nsga2.solve, "nsga2")
    pso = Pso(default_portfolio_optimization_problem())
    pso_soln = timer.time(pso.solve, "pso")
    spea2 = Spea2(default_portfolio_optimization_problem())
    spea2_soln = timer.time(spea2.solve, "spea2")

    print(compareSolutions(branch_bound_soln, bee_colony_soln, flower_pollination_soln, nsga2_soln, pso_soln, spea2_soln))
    print(timer.get_times_as_formatted_str())

main()