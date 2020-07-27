from pkg.random.random import Random
from pkg.consts import Constants


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers
        self.best = None

    # TODO
    def find_best(self):
        self.best = self.flowers[0]

    def get_best(self):
        return self.best

    def pollinate(self):
        for flower in self.flowers:
            if Random.random_float_between_0_and_1() < Constants.FP_SWITCH_PROBABILITY:
                self.global_pollination(flower)
            else:
                self.local_pollination(flower)
            self.update_population()

    # TODO
    def global_pollination(self, flower):
        pass

    # TODO
    def local_pollination(self, flower):
        pass

    # TODO
    def update_population(self):
        pass
