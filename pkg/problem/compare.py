def dominates(obj1, obj2):
    if obj1 is obj2:
        return False
    return all(obj1[o] >= obj2[o] for o in range(len(obj1))) and any(obj1[o] > obj2[o] for o in range(len(obj1)))

def non_dominated(obj, objs):
    for o in objs:
        if dominates(o, obj):
            return False
    return True
