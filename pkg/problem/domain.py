from abc import abstractmethod


def closest_in_list(el, lst):
    if not lst or not el:
        return None
    if el in lst:
        return el
    lst.append(el)
    lst.sort()
    if el == lst[0]:
        return lst[1]
    elif el == lst[-1]:
        return lst[-2]
    closest_under = lst[lst.index(el) - 1]
    closest_over = lst[lst.index(el) + 1]
    if abs(closest_under - el) < abs(closest_over - el):
        return closest_under
    return closest_over


class Domain:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        raise NotImplementedError

    @abstractmethod
    def __contains__(self, item):
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        raise NotImplementedError

    @abstractmethod
    def top(self):
        raise NotImplementedError

    @abstractmethod
    def closest(self, el):
        raise NotImplementedError

    @abstractmethod
    def random(self):
        raise NotImplementedError
