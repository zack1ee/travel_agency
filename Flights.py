from Flight import Flight
from Destinations import Destinations
import tkinter as tk
from tkinter import ttk

class Flights:
    def __init__(self, agency):
        self.agency = agency
        self.flights = []
        self.flight_img_path = "assets/flight.png"

    def add_flight(self, flight:Flight):
        if self.has_flight(flight.takeoff, flight.landing):
            from A_Exceptions import NumberFormatException, ExceptionWindow
            Exception("FlightExistException", "This flight is already exists")
        else:  
            self.flights.append(flight)
    
    def remove_flight(self, flight:Flight):
        for f in self.flights:
            if f.takeoff == flight.takeoff and f.landing == flight.landing:
                self.flights.remove(f)
    
    def has_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return True
        return False
    
    def get_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return f
        return None
        
    def get_filtered_flights(self,country):
        filtered = []
        for f in self.flights:
            if country.lower() in str(f.landing).lower() or country.lower() in str(f.takeoff).lower():
                filtered.append(f)
        return filtered
    
    def get_total_cost(self):
        cost = 0.0
        for f in self.flights:
            cost = cost + f.cost
        return cost

    def flights_window(self, admins, agency_window):
        button_color = '#3A9AFF'
        button_width = 23
        button_height = 1
        self.flight_window = tk.Toplevel(agency_window)    
        self.flight_window.title("Prog 2 Travel Agency")
        
        icon_path = "assets/flights_icon.png"
        icon = tk.PhotoImage(file=icon_path)
        self.flight_window.iconphoto(True,icon)
        self.flight_img = tk.PhotoImage(file=self.flight_img_path)
        self.flight_img = self.flight_img.subsample(2)
        self.flight_img_label = tk.Label(self.flight_window, image=self.flight_img)
        self.flight_img_label.pack()
        

        self.flights_label = tk.Label(self.flight_window, 
                                      text=f"Welcome {str(admins.name)} to the Flights Section",
                                      pady=15,
                                      font="20",
                                      fg=button_color)
        self.flights_label.pack()

        #buttons

        self.flight_btn_frame = tk.Frame(self.flight_window)
        self.flight_btn_frame.pack()

        view_all_flight_button = tk.Button(
            self.flight_btn_frame,
            text="View Flights",
            fg='black',
            width=button_width,
            height=button_height,
            command=lambda:self.view_all_flights(self.flight_window)
            )
        view_all_flight_button.grid(row=2,column=0)

        view_flight_by_country = tk.Button(
            self.flight_btn_frame,
            text="View Flights by Country",
            fg='black',
            width=button_width,
            height=button_height,
            command=lambda:self.filter_flights(self.flight_window)
            )
        view_flight_by_country.grid(row=2,column=1)

        add_flight_button = tk.Button(
            self.flight_btn_frame,
            text="Add Flight",
            fg='black',
            width=button_width,
            height=button_height,
            command=lambda:self.add_flight_window(self.flight_window)
            )
        add_flight_button.grid(row=2,column=2)

        remove_flight_button = tk.Button(
            self.flight_btn_frame,
            text="Remove Flight",
            fg='black',
            width=button_width,
            height=button_height,
            command=lambda:self.remove_flight_window(self.flight_window)
            )
        remove_flight_button.grid(row=2,column=3)

        close_button = tk.Button(
            self.flight_btn_frame,
            text="Close",
            fg="black",
            width=button_width,
            height=button_height,
            command=lambda: self.close_window(self.flight_window)
        )
        close_button.grid(row=2,column=4)

        for btn in [view_all_flight_button, view_flight_by_country, add_flight_button, remove_flight_button, close_button]:
            btn.bind("<Enter>", self.enter)
            btn.bind("<Leave>", self.leave)
            btn.configure(relief=tk.FLAT, borderwidth=0)
    
    def view_all_flights(self, f_window):
        button_color = '#3A9AFF'
        button_height = 1

        self.vaf_window = tk.Toplevel(f_window)
        self.vaf_window.title("View All Flights")

        self.img = tk.PhotoImage(file=self.flight_img_path)
        self.img = self.img.subsample(2)
        self.img_label = tk.Label(self.vaf_window, image=self.img)
        self.img_label.pack()

        vaf_label = tk.Label(self.vaf_window, text="Flights", font="Helvetica 25 bold", fg=button_color,pady=15)
        vaf_label.pack()

        s = ttk.Style()
        s.theme_use('default')
        s.configure('Treeview.Heading', font=("Helvetica", 10, "bold"), foreground=button_color)

        col = ('Airline', 'Flight Number', 'Takeoff Country', 'Landing Country', 'Cost')
        treeview_frame = tk.Frame(self.vaf_window)
        treeview_frame.pack()

        treeview = ttk.Treeview(treeview_frame, columns=col, show='headings')
        for c in col:
            treeview.column(c, anchor=tk.W, width=160, stretch=tk.NO)
            treeview.heading(c, text=c)

        treeview.grid(row=0, column=0, sticky="nsew")

        self.vsb = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        treeview.configure(yscrollcommand=self.vsb.set)

        treeview_frame.grid_rowconfigure(0, weight=1)
        treeview_frame.grid_columnconfigure(0, weight=1)

        for f in self.flights:
            airline = f.get_airline()
            flight_no = f.get_flight_no()
            takeoff = f.get_takeoff()
            landing = f.get_landing()
            cost = f.get_cost()
            details = [airline, flight_no, takeoff, landing, cost]
            if self.flights.index(f) % 2 == 0:
                treeview.insert('', tk.END, values=details, tags=("even_row",))
            else:
                treeview.insert('', tk.END, values=details, tags=("odd_row",))
        
        treeview.tag_configure('even_row', background='white')
        treeview.tag_configure('odd_row', background='#EEF0F3')
        

        close_btn = tk.Button(self.vaf_window,
                            text="Exit",
                            height=button_height,
                            width=116,
                            bg=button_color,
                            fg="white",
                            command=lambda: self.close_window(self.vaf_window)
                            )
        close_btn.pack()
        close_btn.bind("<Enter>", self.enter)
        close_btn.bind("<Leave>", self.leave)
        close_btn.configure(relief=tk.FLAT, borderwidth=0)
    
    def filter_flights(self, ff_window):
        button_color = '#3A9AFF'
        button_width = 10
        button_height = 1

        self.filter_window = tk.Toplevel(ff_window)
        self.filter_window.title("View All Flights")
        self.img = tk.PhotoImage(file=self.flight_img_path)
        self.img = self.img.subsample(2)
        self.img_label = tk.Label(self.filter_window, image=self.img)
        self.img_label.pack()

        title_label = tk.Label(self.filter_window, text="Filtered Flights", font="Helvetica 25 bold", fg=button_color,pady=10)
        title_label.pack()

        subtitle = tk.Label(self.filter_window, text="Country", font="Helvetica 15 bold", fg=button_color,pady=10)
        subtitle.pack()

        search_entry = tk.Entry(self.filter_window, font="Helvetica 10", width=116)
        search_entry.pack()

        s = ttk.Style()
        s.theme_use('default')
        s.configure('Treeview.Heading', font=("Helvetica", 10, "bold"), foreground=button_color)

        col = ('Airline', 'Flight Number', 'Takeoff Country', 'Landing Country', 'Cost')
        treeview_frame = tk.Frame(self.filter_window)
        treeview_frame.pack()

        treeview = ttk.Treeview(treeview_frame, columns=col, show='headings')
        for c in col:
            treeview.column(c, anchor=tk.W, width=160, stretch=tk.NO)
            treeview.heading(c, text=c)
        treeview.grid(row=0, column=0, sticky="nsew")

        self.vsb = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        treeview.configure(yscrollcommand=self.vsb.set)

        treeview_frame.grid_rowconfigure(0, weight=1)
        treeview_frame.grid_columnconfigure(0, weight=1)

        if not search_entry.get():
            for f in self.flights:
                    airline = f.get_airline()
                    flight_no = f.get_flight_no()
                    takeoff = f.get_takeoff()
                    landing = f.get_landing()
                    cost = f.get_cost()
                    details = [airline, flight_no, takeoff, landing, cost]
                    if self.flights.index(f) % 2 == 0:
                        treeview.insert('', tk.END, values=details, tags=("even_row",))
                    else:
                        treeview.insert('', tk.END, values=details, tags=("odd_row",))
                
            treeview.tag_configure('even_row', background='white')
            treeview.tag_configure('odd_row', background='#EEF0F3')
        
        def update_flight_list(event):
            search_for = search_entry.get()
            treeview.delete(*treeview.get_children())

            if search_for:
                for f in self.get_filtered_flights(search_for):
                    airline = f.get_airline()
                    flight_no = f.get_flight_no()
                    takeoff = f.get_takeoff()
                    landing = f.get_landing()
                    cost = f.get_cost()
                    details = [airline, flight_no, takeoff, landing, cost]
                    
                    if self.flights.index(f) % 2 == 0:
                        treeview.insert('', tk.END, values=details, tags=("even_row",))
                    else:
                        treeview.insert('', tk.END, values=details, tags=("odd_row",))
                
                treeview.tag_configure('even_row', background='white')
                treeview.tag_configure('odd_row', background='#EEF0F3')
                    
            elif search_for == "":
                for f in self.flights:
                    airline = f.get_airline()
                    flight_no = f.get_flight_no()
                    takeoff = f.get_takeoff()
                    landing = f.get_landing()
                    cost = f.get_cost()
                    details = [airline, flight_no, takeoff, landing, cost]

                    if self.flights.index(f) % 2 == 0:
                        treeview.insert('', tk.END, values=details, tags=("even_row",))
                    else:
                        treeview.insert('', tk.END, values=details, tags=("odd_row",))
                
                treeview.tag_configure('even_row', background='white')
                treeview.tag_configure('odd_row', background='#EEF0F3')

        search_entry.bind('<KeyRelease>', update_flight_list)

        close_btn = tk.Button(self.filter_window,
                            text="Exit",
                            height=button_height,
                            width=116,
                            bg=button_color,
                            fg="white",
                            command=lambda: self.close_window(self.filter_window)
                            )
        close_btn.pack()
        close_btn.bind("<Enter>", self.enter)
        close_btn.bind("<Leave>", self.leave)
        close_btn.configure(relief=tk.FLAT, borderwidth=0)
    
    def add_flight_window(self,window):
        button_color = '#3A9AFF'
        add_flight_window = tk.Toplevel(window)
        add_flight_window.title("Prog 2 Travel Agency")
        
        self.add_img = tk.PhotoImage(file=self.flight_img_path).subsample(2)
        self.img_label = tk.Label(add_flight_window, image=self.add_img)
        self.img_label.pack()

        title = tk.Label(add_flight_window, text="Add a Flight", font="Helvetica 20 bold", fg=button_color,pady=10)
        title.pack()

        entry_frame = tk.Frame(add_flight_window)
        entry_frame.pack()

        #airline, flight_no, takeoff, landing, cost

        label_font = "Helvetica 11 bold"

        airline_label = tk.Label(entry_frame, text="Airline:",font=label_font,fg=button_color, pady=3)
        airline_label.grid(row=0,column=0)

        airline_no_label = tk.Label(entry_frame, text="Flight Number:",font=label_font,fg=button_color, pady=3)
        airline_no_label.grid(row=1,column=0)

        takeoff_label = tk.Label(entry_frame, text="Takeoff",font=label_font,fg=button_color, pady=3)
        takeoff_label.grid(row=2,column=0)

        landing_label = tk.Label(entry_frame, text="Landing",font=label_font,fg=button_color, pady=3)
        landing_label.grid(row=3,column=0)

        cost_label = tk.Label(entry_frame, text="Cost",font=label_font,fg=button_color, pady=3)
        cost_label.grid(row=4,column=0)

        airline_entry = tk.Entry(entry_frame, font="Helvetica 10")
        airline_entry.grid(row=0,column=1)

        flight_no_entry = tk.Entry(entry_frame, font="Helvetica 10")
        flight_no_entry.grid(row=1,column=1)

        takeoff_entry = tk.Entry(entry_frame, font="Helvetica 10")
        takeoff_entry.grid(row=2,column=1)

        landing_entry = tk.Entry(entry_frame, font="Helvetica 10")
        landing_entry.grid(row=3,column=1)

        cost_entry = tk.Entry(entry_frame, font="Helvetica 10")
        cost_entry.grid(row=4,column=1)

        btn_frame = tk.Frame(add_flight_window)
        btn_frame.pack()

        def create_flight():
            airline = airline_entry.get()
            flight_no = flight_no_entry.get()
            takeoff = takeoff_entry.get()
            landing = landing_entry.get()
            cost = cost_entry.get()  # Correct the variable name
            
            try:
                flight_no = int(flight_no)  # Convert to int here
                cost = float(cost)  # Convert to float here
                
                if self.has_flight(takeoff, landing):
                    from A_Exceptions import FlightExistsException, ExceptionWindow
                    Exception("FlightExistsException")
                else:
                    self.add_flight(Flight(airline, flight_no, takeoff, landing, cost))
                    self.close_window(add_flight_window)
            
            except ValueError:
                from A_Exceptions import NumberFormatException, ExceptionWindow
                ExceptionWindow("NumberFormatException", "Enter a number!")


        add_flight_btn = tk.Button(btn_frame,
                            text="Add Flight",
                            width=58,
                            bg='#7CBCFF',
                            fg="white",
                            command=None
                            )
        add_flight_btn.grid(row=0,column=0)
        add_flight_btn.configure(relief=tk.FLAT, borderwidth=0)
        
        def update_btn_state(event):
            if flight_no_entry.get() and airline_entry.get() and takeoff_entry.get() and landing_entry.get() and cost_entry.get():
                add_flight_btn.config(command=create_flight, bg=button_color,fg='white') #enable
                add_flight_btn.bind("<Enter>", self.enter)
                add_flight_btn.bind("<Leave>", self.leave)
            else:
                try:
                    add_flight_btn.config(command=None, bg='#7CBCFF',fg='white') #disable
                    add_flight_btn.unbind("<Enter>", self.enter)
                    add_flight_btn.unbind("<Leave>", self.leave)
                except TypeError:
                    pass
        
        flight_no_entry.bind("<KeyRelease>", update_btn_state)
        airline_entry.bind("<KeyRelease>", update_btn_state)
        takeoff_entry.bind("<KeyRelease>", update_btn_state)
        landing_entry.bind("<KeyRelease>", update_btn_state)
        cost_entry.bind("<KeyRelease>", update_btn_state)

        close_btn = tk.Button(btn_frame,
                            text="Exit",
                            width=58,
                            bg=button_color,
                            fg="white",
                            command=lambda: self.close_window(add_flight_window)
                            )
        close_btn.grid(row=0,column=1)
        close_btn.bind("<Enter>", self.enter)
        close_btn.bind("<Leave>", self.leave)
        close_btn.configure(relief=tk.FLAT, borderwidth=0)
    
    def remove_flight_window(self,window):
        button_color = '#3A9AFF'
        remove_flight_window = tk.Toplevel(window)
        remove_flight_window.title("Prog 2 Travel Agency")

        self.img = tk.PhotoImage(file=self.flight_img_path)
        self.img = self.img.subsample(2)
        self.img_label = tk.Label(remove_flight_window, image=self.img)
        self.img_label.pack()

        title = tk.Label(remove_flight_window,text='Remove a Flight', fg=button_color, font="Helvetica 20 bold",pady=10)
        title.pack()

        frame = tk.Frame(remove_flight_window, pady=5)
        frame.pack()

        takeoff_label = tk.Label(frame, text="Takeoff:",font="Helvetica 12 bold", fg=button_color)
        takeoff_label.grid(row=0,column=0)

        landing_label = tk.Label(frame, text="Landing:", font="Helvetica 12 bold", fg=button_color)
        landing_label.grid(row=1,column=0)

        takeoff_entry = tk.Entry(frame, font="Helvetica 12")
        takeoff_entry.grid(row=0,column=1)

        landing_entry = tk.Entry(frame, font="Helvetica 12")
        landing_entry.grid(row=1,column=1)

        btn_frame = tk.Frame(remove_flight_window)
        btn_frame.pack()

        def destroy_flight():
            t = takeoff_entry.get()
            l = landing_entry.get()
            if self.has_flight(t,l):
                flight = self.get_flight(t,l)
                self.remove_flight(flight)
                self.close_window(remove_flight_window)
            else:
                from A_Exceptions import ItemNotFoundException, ExceptionWindowException
                Exception("ItemNotFoundException", "No such item exists.")

        remove_flight_btn = tk.Button(btn_frame,
                            text="Remove Flight",
                            width=58,
                            bg='#7CBCFF',
                            fg="white",
                            command=None
                            )
        remove_flight_btn.grid(row=0,column=0)
        remove_flight_btn.configure(relief=tk.FLAT, borderwidth=0)

        def update_btn_state(event):
            if takeoff_entry.get() and landing_entry.get():
                remove_flight_btn.config(command=destroy_flight, bg=button_color,fg='white') #enable
                remove_flight_btn.bind("<Enter>", self.enter)
                remove_flight_btn.bind("<Leave>", self.leave)
            else:
                try:
                    remove_flight_btn.config(command=None, bg='#7CBCFF',fg='white') #disable
                    remove_flight_btn.unbind("<Enter>", self.enter)
                    remove_flight_btn.unbind("<Leave>", self.leave)
                except TypeError:
                    pass

        takeoff_entry.bind("<KeyRelease>", update_btn_state)
        landing_entry.bind("<KeyRelease>", update_btn_state)
        

        close_btn = tk.Button(btn_frame,
                            text="Exit",
                            width=58,
                            bg=button_color,
                            fg="white",
                            command=lambda: self.close_window(remove_flight_window)
                            )
        close_btn.grid(row=0,column=1)
        close_btn.bind("<Enter>", self.enter)
        close_btn.bind("<Leave>", self.leave)
        close_btn.configure(relief=tk.FLAT, borderwidth=0)

        

    def close_window(self, window):
        window.destroy()
    
    def enter(self,event):
        event.widget.config(bg='#6CD0FF')
    def leave(self,event):
        event.widget.config(bg='#3A9AFF')