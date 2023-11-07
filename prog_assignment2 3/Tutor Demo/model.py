from Stadium import Stadium
class Model:
    def __init__(self):
        self.stadium = Stadium()
        self.groups = self.stadium.getGroups()
        self.group = None
    
    def getGroup(self, Selgroup):
        for group in self.groups:
            print("SelGroup:", Selgroup)
            if Selgroup == self.getGroupName(group):
                return group
        return None

    def getGroups(self):
        return self.groups

    def setGroup(self, Selgroup):
        self.group = self.getGroup(Selgroup)
       
    def sell(self, quantity):
        """
        Save the email into a file
        :return:
        """
        if self.group.canSell(quantity):
            self.group.sell(quantity)
    
    def getGroupName(self, group):
        return str(group.getName())

    def getGroupN(self):
        return str(self.group.getName())    
    
    def getGroupCapacity(self):
        return int(self.group.getCapacity())
    
    def getGroupPrice(self):
        return float(self.group.getPrice())

    def getGroupSold(self):
        return int(self.group.getSold())

    def getGroupIncome(self):
        return float(self.group.getIncome())

    def getGroupLeft(self):
        return int(self.group.getLeft())