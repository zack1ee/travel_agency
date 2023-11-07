class Destination:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def to_string(self):
        return self.name + " in " + self.country