class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.groups = self.getGroups()
        for item in self.groups:
            self.view.insertItem(item)
    
    def setstuff(self, groupN):
        self.group = self.model.getGroup(groupN)
        self.model.setGroup(groupN)
        self.view.set_message_text(self.view.groupName, str(self.model.group.getName()))
        self.view.set_message_text(self.view.groupPrice, str(self.model.getGroupPrice()))
        self.view.set_message_text(self.view.groupCapacity, str(self.model.getGroupCapacity()))
        self.view.set_message_text(self.view.groupLeft, str(self.model.getGroupLeft()))
        self.view.set_message_text(self.view.groupIncome, "{:.2f}".format(float(self.model.getGroupIncome())))
        self.view.set_message_text(self.view.groupSold, self.model.getGroupSold())

    def sell(self, quantity):
        try:
            self.model.sell(int(quantity))
            self.view.set_message_text(self.view.groupSold, str(self.model.getGroupSold()))
            self.view.set_message_text(self.view.groupLeft, str(self.model.getGroupLeft()))
            self.view.set_message_text(self.view.groupIncome, "{:.2f}".format(float(self.model.getGroupIncome())))
            self.view.set_text(self.view.sellTf, "0")
            selected = self.view.treeview.focus()
            self.view.treeview.item(selected, text='', values=(self.group.getName(), self.group.getCapacity(), self.group.getPrice(),self.group.getSold(), self.group.getIncome(),self.group.getLeft()))
        except:
            pass

    def getGroups(self):
        return self.model.getGroups()    