def compareSolutions(actual, *solns):
    return [actual] + [str(soln) for soln in solns]

# TODO figure out how to compare stuff
def dominates(obj1, obj2):
    if obj1 is obj2:
        return False
    return all(obj1[o] >= obj2[o] for o in range(obj1)) and any(obj1[o] > obj2[o] for o in range(obj1))
