import tkinter as tk
from tkinter import ttk

class ExceptionWindow(tk.Toplevel):
    def __init__(self, exception_message, additional_info=None):
        super().__init__()
        self.title("Error")
        self.geometry("425x230")

        image_path = "assets/error.png"
        error_icon_path = "assets/error_icon.png"
        error_icon = tk.PhotoImage(file=error_icon_path)

        self.iconphoto(False,error_icon)
        self.img = tk.PhotoImage(file=image_path)
        self.img = self.img.subsample(4)

        img_label = tk.Label(self,image=self.img)
        img_label.pack()
        
        error_label = tk.Label(self, text="Error", font="Helvetica 10 bold", pady=5, fg="#3A9AFF")
        error_label.pack()

        message_label = tk.Label(self, text=exception_message, font="Helvetica 10 bold", fg="red", pady=5)
        message_label.pack()

        if additional_info:
            additional_info_label = tk.Label(self, text=additional_info, font="Helvetica 10 bold")
            additional_info_label.pack()

        close_window_btn = tk.Button(self,
                                     text="Close",
                                     font="Helvetica",
                                     command=self.close_window, 
                                     bg="#3A9AFF", 
                                     fg="white", 
                                     height=1,width=45,
                                     pady=5,
                                     relief=tk.FLAT, borderwidth=0,)
        close_window_btn.pack()
        close_window_btn.bind("<Enter>", self.on_enter), 
        close_window_btn.bind("<Leave>", self.on_leave)


    def close_window(self):
        self.destroy()   
    def on_enter(self,event):
        event.widget.config(bg='#6CD0FF')
    def on_leave(self,event):
        event.widget.config(bg='#3A9AFF')
    

class InvalidCredentialsException(Exception):
    def __init__(self, message="InvalidCredentialsException", additional_info="The credentials are incorrect"):
        super().__init__(message, additional_info)

class FlightExistsException(Exception):
    def __init__(self, message="FlightExistsException", additional_info="The flight already exists."):
        super().__init__(message, additional_info)

class DestinationExistsException(Exception):
    def __init__(self, message="DestinationExistsException", additional_info="The destination already exists."):
        super().__init__(message, additional_info)

class NumberFormatException(Exception):
    def __init__(self, message="NumberFormatException", additional_info="Flight Number and/or Cost Must be Numbers!"):
        super().__init__(message, additional_info)

class ItemNotFoundException(Exception):
    def __init__(self, message="ItemNotFoundException", additional_info="No such item exists."):
        super().__init__(message, additional_info)