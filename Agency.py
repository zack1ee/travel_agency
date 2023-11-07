from Administrators import Administrators
from Trip import Trip
from Flights import Flights
from Destinations import Destinations
import tkinter as tk
import A_Exceptions as exceptions
from A_Exceptions import InvalidCredentialsException

class Agency:
    def __init__(self):
        self.loggedInUser = None
        self.admins = Administrators()
        self.flights = Flights(self)
        self.destinations = Destinations(self)
        self.destinations.insert_dummy_data()
        self.admins.insert_dummy_data()
        self.trip = Trip(self)
    
    def login(self, usr_ent, psw_ent):
        usr = usr_ent.get()
        psw = psw_ent.get()
        try:
            if self.admins.has_administrator(usr, psw):
                self.login_window.destroy()
                self.main_window(self.admins.get_administrator(usr,psw))
                details = (usr, psw)
                return details
            else:
                raise InvalidCredentialsException()
        except InvalidCredentialsException:
            exceptions.ExceptionWindow("InvalidCredentialsException", "The credentials do not match our records.")

    def start_window(self):
        button_color = '#3A9AFF'
        #basics
        self.login_window = tk.Tk()
        self.login_window.title("Prog 2 Travel Agency")
        login_icon_path = "assets/login_icon.png"
        try:
            login_icon = tk.PhotoImage(file=login_icon_path)
            self.login_window.iconphoto(True, login_icon)
        except tk.TclError as e:
            print(e)
        
        login_title = tk.Label(self.login_window, text="Login:", font="Helvetica 15 bold", padx=2,pady=2, fg="black")
        login_title.pack()

        self.login_frame = tk.Frame(self.login_window, pady=10)
        self.login_frame.pack()

        #username and password
        user_label = tk.Label(self.login_frame, text="Username:", font="Helvetica 10 bold", fg='black')
        user_label.grid(row=0,column=0, sticky=tk.E)

        user_entry = tk.Entry(self.login_frame)
        user_entry.grid(row=0,column=1, sticky=tk.E)

        password_label = tk.Label(self.login_frame, text="Password", font="Helvetica 10 bold", fg='black')
        password_label.grid(row=1,column=0, sticky=tk.W)

        password_entry = tk.Entry(self.login_frame, show="·")
        password_entry.grid(row=1,column=1, sticky=tk.E)

        #login
        self.button_frame = tk.Frame(self.login_window)
        self.button_frame.pack()

        button_width = 20
        button_height = 2
        login_btn = tk.Button(self.button_frame, 
                            width=button_width,
                            height=button_height,
                            text="Login",
                            command=lambda: self.login(user_entry, password_entry),
                            fg="black",
                            relief=tk.FLAT, borderwidth=0,
                            state=tk.DISABLED)
        login_btn.grid(row=2,column=0, sticky=tk.W)

        def update_login_button_state(event):
            if user_entry.get() and password_entry.get():
                login_btn.config(state=tk.NORMAL, bg=button_color) #enable
                login_btn.bind("<Enter>", self.on_enter)
                login_btn.bind("<Leave>", self.on_leave)
            else:
                try:
                    login_btn.config(state=tk.DISABLED, bg='#7CBCFF') #disable
                    login_btn.unbind("<Enter>", self.on_enter)
                    login_btn.unbind("<Leave>", self.on_leave)
                except TypeError:
                    pass
        
        user_entry.bind("<KeyRelease>", update_login_button_state)
        password_entry.bind("<KeyRelease>", update_login_button_state)

        #exit
        exit_btn = tk.Button(self.button_frame, 
                             width=button_width, 
                             height=button_height, 
                             text="Close", 
                             command=self.close_program, 
                           fg="black",
                             relief=tk.FLAT, borderwidth=0)
        exit_btn.grid(row=2,column=1, sticky=tk.E)

        #hover events
        exit_btn.bind("<Enter>", self.on_enter)
        exit_btn.bind("<Leave>", self.on_leave)

        #main loop
        self.login_window.mainloop()
    
    def close_program(self):
        self.login_window.quit()
    
    def main_window(self, admins):
        button_color = '#3A9AFF'
        #basics
        self.main_window = tk.Tk()
        self.main_window.title("Prog 2 Travel Agency")
        font = "Helvetica 10 bold"
        
        #icon
        agency_icon_path="assets/agency_icon.png"
        self.agency_icon = tk.PhotoImage(file=agency_icon_path)
        self.main_window.iconphoto(False, self.agency_icon)

        #main image
        agency_img_path = "assets/agency.png"
        self.agency_img = tk.PhotoImage(file=agency_img_path)
        self.agency_img = self.agency_img.subsample(2)
        self.agency_img_label = tk.Label(self.main_window, image=self.agency_img)
        self.agency_img_label.pack()

        #main frame
        self.main_frame = tk.Frame(self.main_window,  highlightbackground="black", highlightthickness=1)
        self.main_frame.pack(expand=True,fill="both")

        #should be an image somewhere above the line below
        main_welcome = tk.Label(self.main_frame,text=f"Hi {str(admins.name)}, welcome to the Prog2 Travel Agency",font=font, fg=('black'), padx=5,pady=20)
        main_welcome.pack(expand=True,fill="both", anchor="center")

        #buttons 4 flights, destinations, trip and exit
        button_width = 25
        button_height = 1

        self.agency_btn_frame = tk.Frame(self.main_window)
        self.agency_btn_frame.pack()

        flight_btn = tk.Button(self.agency_btn_frame,
                           text="Flights",
                        
                           width=button_width,
                           height=button_height,
                           command=lambda: self.flights.flights_window(admins, self.main_window))
        flight_btn.grid(row=1, column=0)

        destination_btn = tk.Button(self.agency_btn_frame,
                                    text="Destinations",
              
                
                                    width=button_width,
                                    height=button_height,
                                    command=lambda: self.destinations.destination_window(self.main_window, admins))
        destination_btn.grid(row=1, column=1)

        trip_btn = tk.Button(self.agency_btn_frame,
                            text="Trip",
                
                            width=button_width,
                            height=button_height,
                            command=lambda:self.trip.main_window(self.main_window,admins))
        trip_btn.grid(row=1, column=2)

        exit_btn = tk.Button(self.agency_btn_frame,
                            text="Exit",
                            font=font,
                        
                            command=self.close_program,
                            width=button_width,
                            height=button_height)
        exit_btn.grid(row=1, column=3)

        for btn in [flight_btn, destination_btn, trip_btn, exit_btn]:
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            btn.configure(relief=tk.FLAT, borderwidth=0)
        
    def on_enter(self,event):
        event.widget.config()
    def on_leave(self,event):
        event.widget.config()


if __name__ == '__main__':
    agency = Agency()    
    agency.start_window()