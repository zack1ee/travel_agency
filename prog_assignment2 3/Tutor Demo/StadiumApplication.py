import tkinter as tk
from model import Model
from view import View
from controller import Controller
class StadiumApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Stadium')
        
        # create a model
        model = Model()

        view = View(self)

        # create a controller
        controller = Controller(model, view)
        

        # set the controller to view
        view.set_controller(controller)

        # create a view and place it on the root window
        
        view.grid(row=0, column=0)

        


if __name__ == '__main__':
    app = StadiumApplication()
    app.mainloop()