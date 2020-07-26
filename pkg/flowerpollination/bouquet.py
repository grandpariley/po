import random
from pkg.consts import Constants

class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers
        self.best = None

    def find_best(self):
        self.best = self.flowers[0]

    def get_best(self):
        return self.best

    def pollinate(self):
        for flower in self.flowers:
            if random.uniform(0.0, 1.0) < Constants.FP_SWITCH_PROBABILITY:
                self.global_pollination(flower)
            else:
                self.local_pollination(flower)
            self.update_population()

    def global_pollination(self, flower):
        pass

    def local_pollination(self, flower):
        pass

    def update_population(self):
        pass
        