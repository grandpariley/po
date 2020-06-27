class Variable:
    """
    define a variable as a domain of possible values
    """
    
    def __init__(self, domain):
        self.domain = domain
        self.value = None

    def __str__(self):
        return str(self.domain)
    
    def pop(self):
        if not self.domain:
            return None
        return self.domain.pop()

    def top(self):
        if not self.domain:
            return None
        return self.domain[-1]

    def set_value(self, value):
        if value in self.domain:
            self.value = value

    def get_value(self):
        return self.value

    def reset_value(self):
        self.value = None

    def get_domain(self):
        return self.domain