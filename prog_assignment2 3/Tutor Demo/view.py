import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from turtle import width


class View(tk.Frame):
    

    def __init__(self, parent):
        super().__init__(parent)
        self.counterWin = 0
        self.controller = None
        self.StadLbl = tk.Label(self, text='Stadium')
        self.StadLbl.grid(row=0, column=0, sticky=tk.NSEW)
        col =  ('Name', 'Capacity', 'Price', 'Sold', 'Income', 'Left')
        self.treeview = ttk.Treeview(self, columns=col, show='headings')
        for c in col:
            self.treeview.column(c, anchor=tk.CENTER, width=80, stretch=tk.NO)
        # self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.treeview.heading('Name', text='Name')
        self.treeview.heading('Capacity', text='Capacity')
        self.treeview.heading('Price', text='Price')
        self.treeview.heading('Sold', text='Sold')
        self.treeview.heading('Income', text='Income')
        self.treeview.heading('Left', text='Left')
        # self.treeview.bind('<<TreeviewSelect>>', self.item_selected)
        self.treeview.grid(row=1, column=0, sticky=tk.NSEW)
        self.sell_button = tk.Button(self, text='Open', command=lambda:self.openWindow())
        self.sell_button.grid(row=2, column=0, sticky=tk.NSEW)
        



    def insertItem(self, item):
        # add data to the treeview
        name  = item.getName()
        capacity = item.getCapacity()
        price = '{:.2f}'.format(item.getPrice())
        sold = item.getSold()
        income = item.getIncome()
        left = item.getLeft()
        group_details = [name, capacity, price, sold, income, left]
        # st = f'{name} seats (${price})' 
        self.treeview.insert('', tk.END, values=group_details)
        # self.listbox.insert(tk.END, st)

    def item_selected(self):
        for selected_item in self.treeview.selection():
            item = self.treeview.item(selected_item)
            record = item['values']
            # show a message
            print(record)
            return record[0]
            # showinfo(title='Information', message=','.join(record))

    def openWindow(self):
        if self.counterWin < 20:
            self.newWindow = tk.Toplevel(self)
            item = self.item_selected()
            
            # create widgets
            # label
            self.groupLabel = tk.Label(self.newWindow, text='Seat Group:')
            self.groupLabel.grid(row=0, column=0, sticky=tk.W)
            self.capacityLabel = tk.Label(self.newWindow, text='Capacity:')
            self.capacityLabel.grid(row=1, column=0, sticky=tk.W)
            self.priceLabel = tk.Label(self.newWindow, text='Price: ($)')
            self.priceLabel.grid(row=2, column=0, sticky=tk.W)
            self.soldLabel = tk.Label(self.newWindow, text='Sold:')
            self.soldLabel.grid(row=3, column=0, sticky=tk.W)
            self.leftLabel = tk.Label(self.newWindow, text='Left:')
            self.leftLabel.grid(row=4, column=0, sticky=tk.W)
            self.incomeLabel = tk.Label(self.newWindow, text='Income: ($)')
            self.incomeLabel.grid(row=5, column=0, sticky=tk.W)
            self.sellLabel = tk.Label(self.newWindow, text='Sell')
            self.sellLabel.grid(row=6, column=0, sticky=tk.W)

            # sell entry
            self.sellTf = tk.Entry(self.newWindow)
            self.sellTf.grid(row=6, column=1, sticky=tk.W)
            self.set_text(self.sellTf, "0")

            # sell button
            self.sell_button = tk.Button(self.newWindow, text='Sell', command=self.sell_button_clicked)
            self.sell_button.grid(row=7, column=1, sticky=tk.E)
            

            # message - texts
            self.groupName = tk.Message(self.newWindow, justify=tk.LEFT, text="", width=300) 
            self.groupName.grid(row=0, column=1, sticky=tk.W)
            self.groupCapacity = tk.Message(self.newWindow, justify=tk.LEFT, text="", width=300) 
            self.groupCapacity.grid(row=1, column=1, sticky=tk.W)
            self.groupPrice = tk.Message(self.newWindow, justify=tk.LEFT, text="", width=300) 
            self.groupPrice.grid(row=2, column=1, sticky=tk.W)
            self.groupSold = tk.Message(self.newWindow, justify=tk.LEFT, text="", width=300) 
            self.groupSold.grid(row=3, column=1, sticky=tk.W)
            self.groupLeft = tk.Message(self.newWindow, justify=tk.LEFT, text="", width=300) 
            self.groupLeft.grid(row=4, column=1, sticky=tk.W)
            self.groupIncome = tk.Message(self.newWindow, justify=tk.LEFT, text="", width=300) 
            self.groupIncome.grid(row=5, column=1, sticky=tk.W)

            self.controller.setstuff(str(item))

            self.counterWin +=1
        else:
            print("reached max limit")


    
    def selected_item(self):
        # Traverse the tuple returned by
        # curselection method and print
        # corresponding value(s) in the listbox
        for i in self.listbox.curselection():
            return self.listbox.get(i).split(" ")[0]

    


    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def sell_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            try:
                self.controller.sell(self.sellTf.get())
            except:
                pass

    def set_message_text(self, mf, text):
        mf.configure(text=text)

    def set_text(self, tf, text):
        tf.delete(0,tk.END)
        tf.insert(0,text)

