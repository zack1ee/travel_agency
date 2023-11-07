from Group import Group

class Stadium:

    def __init__(self):
        self.groups = []
        self.groups.append(Group("front", 300, 400.0))
        self.groups.append(Group("middle", 200, 100.0))
        self.groups.append(Group("back", 100, 60.0))
    
    def getGroups(self):
        return self.groups