import math


def dominates(obj1, obj2):
    if obj1 is obj2 or len(obj1) != len(obj2):
        return False
    return all(obj1[o] >= obj2[o] for o in range(len(obj1))) and any(obj1[o] > obj2[o] for o in range(len(obj1)))


def euclidean_distance(obj1, obj2):
    if obj1 is obj2:
        return 0
    if len(obj1) != len(obj2):
        return math.inf
    return math.sqrt(sum([pow(obj1[o] - obj2[o], 2) for o in range(len(obj1))]))
