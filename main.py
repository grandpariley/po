from po.memory import limit_memory
from po.pkg.log import Log
from po.pkg.moead.moead import Moead
from po.pkg.problem.builder import generate_solutions_discrete_domain


async def get_solutions(problems):
    input_solutions = {}
    for name, problem in problems.items():
        Log.log("Generating solutions for " + name, "generate")
        input_solutions[name] = await generate_solutions_discrete_domain(problem)
        Log.log("Generating complete! Generated " + str(len(input_solutions[name])) + " solutions")
    output_solutions = {}
    for name in problems.keys():
        Log.log("Starting to solve using MOEA/D for " + name, name)
        output_solutions[name] = await Moead(input_solutions[name], tag=name).solve()
    return output_solutions


@limit_memory(percentage=0.9)
async def main(problems):
    return await get_solutions(problems)
