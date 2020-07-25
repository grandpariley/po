from pkg.beecolony.food_source_memory import FoodSourceMemory

class Colony:
    def __init__(self, bees):
        self.bees = bees
        self.food_source_memory = FoodSourceMemory()

    def assign_employed_bees(self):
        pass

    def send_onlooker_bees(self):
        collection_probability = self.get_collection_probability()

    def get_collection_probability(self):
        return 0;

    def send_scout(self):
        pass

    def get_solutions(self):
        return [b.get_problem() for b in self.bees]