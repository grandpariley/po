def compareSolutions(actual, *solns):
    return [actual] + [str(soln) for soln in solns]

# TODO figure out how to compare stuff
def compareObjectives(obj1, obj2):
    if obj1 is obj2:
        return False
    return True
