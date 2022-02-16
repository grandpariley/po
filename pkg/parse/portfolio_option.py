class PortfolioOption:
    def __init__(self, dictionary):
        self.price = dictionary['price']
        self.ret = dictionary['return']
        self.var = dictionary['var']
        self.cvar = dictionary['cvar']
        self.environment = dictionary['environment'] if dictionary['environment'] is not None else 0
        self.social = dictionary['social'] if dictionary['social'] is not None else 0
        self.governance = dictionary['governance'] if dictionary['governance'] is not None else 0

    def __str__(self):
        return "[" + str(self.price) + " " + str(self.ret) + " " + str(self.var) + " " + str(self.cvar) + " " + str(
            self.environment) + " " + str(self.social) + " " + str(self.governance) + "]"

    def __repr__(self):
        return str(self)
