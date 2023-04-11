from abc import abstractmethod


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
    def get_random(self):
        raise NotImplementedError

    @abstractmethod
    def closest(self, target):
        raise NotImplementedError

    @abstractmethod
    def get_base_value(self):
        raise NotImplementedError
