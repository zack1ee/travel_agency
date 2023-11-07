class Group:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.sold = 0
        self.income = self.sold*self.price
        self.left = self.capacity-self.sold

    def getName(self):
        return self.name

    def getCapacity(self):
        return self.capacity

    def getPrice(self):
        return self.price
    
    def getSold(self):
        return self.sold
    
    def getIncome(self):
        return self.income

    def getLeft(self):
        return self.left
    
    def canSell(self, num):
        return num <= self.left

    def sell(self, num):
        self.sold = self.sold+num
        self.income = self.sold*self.price
        self.left = self.capacity-self.sold

    



    
