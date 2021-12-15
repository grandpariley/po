from abc import abstractmethod


def closest_in_list(el, lst):
    if not lst or not el:
        return None
    if el in lst:
        return el
    current_closest = lst[0]
    current_closest_distance = float('inf')
    for l in lst:
        distance = l - el
        if current_closest_distance > abs(distance) or (current_closest_distance == abs(distance) and l > current_closest):
            current_closest = l
            current_closest_distance = abs(distance)
    return current_closest

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
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def __next__(self):
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

    def get_base_value(self):
        raise NotImplementedError
