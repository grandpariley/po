def dominates(obj1, obj2):
    if obj1 is obj2:
        return False
    return all(obj1[o] >= obj2[o] for o in range(len(obj1))) and any(obj1[o] > obj2[o] for o in range(len(obj1)))


def non_dominated(obj, objs):
    for o in objs:
        if dominates(o, obj):
            return False
    return True

def compareSolutions(solution_dict):
    non_dominated_solutions = {}
    for name, solns in solution_dict:
        for other_name, other_solns in solution_dict:
            if name is other_name:
                continue
            is_non_dominated = True
            for soln in solns:
                is_non_dominated = is_non_dominated and non_dominated(soln.objective_values(), other_solns.objective_values())
            if name in non_dominated_solutions:
                non_dominated_solutions.update({name: non_dominated_solutions[name] if name in non_dominated_solutions else True and is_non_dominated})
    return non_dominated_solutions
