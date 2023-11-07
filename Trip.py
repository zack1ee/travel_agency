from Destinations import Destinations
from Flights import Flights
import tkinter as tk
from tkinter import ttk

class Trip:
    def __init__(self, agency):
        self.agency = agency
        self.flights = Flights(self.agency)
        self.destinations = Destinations(self.agency)
        self.trips_img_path = 'assets/trip.png'
    
    def add_connecting_flights(self):
        if len(self.destinations.destinations) <= 1:
            from A_Exceptions import Error, InvalidCredentialsException
            Error("NotSufficientFlightException",("There are no flights to connect to "))
        self.flights.flights.clear()
        current_destination = None
        next_destination = None
        for i in range(len(self.destinations.destinations)):
            current_destination = self.destinations.destinations[i]
            if i == (len(self.destinations.destinations) - 1):
                return
            next_destination = self.destinations.destinations[i + 1]
            if current_destination == next_destination or current_destination.country == next_destination.country:
                #throw error
                pass
            
            for f in self.agency.flights.flights:
                if f.takeoff == current_destination.country and f.landing == next_destination.country:
                    try:
                        self.flights.add_flight(f)
                    except:
                        #throw error
                        pass
                    break
    
    def get_itinery(self):
        objects = []
        for i in range(len(self.destinations.destinations)):
            objects.append(self.destinations.destinations[i])
            if i < len(self.flights.flights):
                objects.append(self.flights.flights[i])
        return objects
    
    def main_window(self, window, admins):
        button_color = '#3A9AFF'
        self.main_trips_img = tk.PhotoImage(file=self.trips_img_path).subsample(2)
        
        trip_main_window = tk.Toplevel(window)

        main_img_label = tk.Label(trip_main_window, image=self.main_trips_img)
        main_img_label.pack()
        
        main_title = tk.Label(trip_main_window,
                            text=f"Welcome {str(admins.name)} to the Trips Section",
                            font="Helvetica 10 bold",
                            fg=button_color,
                            pady=10)
        main_title.pack()

        btn_width = int((self.main_trips_img.width())/33)

        btn_frame = tk.Frame(trip_main_window)
        btn_frame.pack()

        add_destination_button = tk.Button(btn_frame, 
                              text="Add Destination", 
                              width=btn_width, 
                              fg='black',

                              command=lambda:self.destinations.add_destination(trip_main_window)) 
        add_destination_button.grid(row=0,column=0)

        remove_destination_button = tk.Button(btn_frame, 
                              text="Remove Destination", 
                              width=btn_width, 
                              fg='black',

                              command=lambda:self.destinations.remove_destination(trip_main_window)) 
        remove_destination_button.grid(row=0,column=1)

        add_connecting_button= tk.Button(btn_frame, 
                              text="Add Connecting Flights", 
                              width=btn_width, 
                              fg='black',
                              command=self.add_connecting_flights) 
        add_connecting_button.grid(row=0,column=2)

        view_trip_button = tk.Button(btn_frame, 
                              text="View Trip", 
                              width=btn_width, 
                              fg='black',
                              command=lambda:self.view_trip_window(trip_main_window)) 
        view_trip_button.grid(row=0,column=3)

        close_button = tk.Button(btn_frame, 
                              text="Close", 
                              width=btn_width, 
                              fg='black',

                              command=lambda:self.close_window(trip_main_window)) 
        close_button.grid(row=0,column=4)

        for btn in [add_destination_button, remove_destination_button, add_connecting_button, view_trip_button, close_button]:
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            btn.configure(relief=tk.FLAT, borderwidth=0)
    
        
    def view_trip_window(self, window):
        button_color = '#3A9AFF'
        self.view_trip_img = tk.PhotoImage(file=self.trips_img_path).subsample(2)
        btn_width = 60
        
        view_t_window = tk.Toplevel(window)

        main_img_label = tk.Label(view_t_window, image=self.view_trip_img)
        main_img_label.pack()

        main_title = tk.Label(view_t_window,
                            text="Your Trip",
                            font="Helvetica 10 bold",
                            fg=button_color,
                            pady=10)
        main_title.pack()

        #if nothing, text should be 'nothing yet'.
        if len(self.destinations.destinations) == 0:
            nothing_yet_label = tk.Label(view_t_window, text="Nothing yet.", font="Helvetica 10 bold",pady=30)
            nothing_yet_label.pack(anchor="center")
        else:
            raw_items = [ ]
            list_frame = tk.Frame(view_t_window, pady=10, width=120)
            list_frame.pack()

            trip_list = tk.Listbox(list_frame, width=120, 
                                   font='Helvetica 10', 
                                   relief=tk.FLAT, 
                                   selectmode=tk.EXTENDED,
                                   selectborderwidth=0,
                                   activestyle=tk.NONE)
            
            for item in self.get_itinery():
                raw_items.append(item)
                trip_list.insert(tk.END, item.to_string())
            
            def cherry_pick(event):
                selected_items = trip_list.curselection()
                clicked_item = trip_list.nearest(event.y)
                
                if clicked_item in selected_items:
                    trip_list.selection_clear(clicked_item)
                else:
                    trip_list.selection_set(clicked_item)
            
            def retrieve_selection():
                selected_items = trip_list.curselection()
                selected_objects = [raw_items[i] for i in selected_items]
                selected_strings = [trip_list.get(index) for index in selected_items]
                
                def verify_elements(objects):
                    first_type = type(objects[0])
                    for item in objects[1:]:
                        if type(item) != first_type:
                            return False
                    return True
                
                if verify_elements(selected_objects):
                    object_type = type(selected_objects[0])
                    if 'Flight' in str(object_type):
                        self.flights.flights.clear()
                        for obj in selected_objects:
                            self.flights.flights.append(obj)
                        self.flights.view_all_flights(view_t_window)
                    elif 'Destination' in str(object_type):
                        self.destinations.destinations.clear()
                        for obj in selected_objects:
                            self.destinations.destinations.append(obj)
                        self.destinations.viewalldestination(view_t_window)
                else:
                    from A_Exceptions import ExceptionWindow, InvalidCredentialsException
                    ExceptionWindow("InputMismatchException",("Can't view this selected flights/destinations"))
            
            trip_list.pack(fill=tk.BOTH, expand=True)
            trip_list.bind("<Button-1>", cherry_pick)

        
        btn_frame = tk.Frame(view_t_window)
        btn_frame.pack()

        view_individual_btn = tk.Button(btn_frame, 
                                        text="View Individual", 
                                        width=btn_width, 
                                        fg='black',
                                        )
        view_individual_btn.grid(row=0,column=0)
        
        close_btn = tk.Button(btn_frame,text="Close", 
                              width=btn_width, 
                              fg='black',

                              command=lambda:self.close_window(view_t_window))
        close_btn.grid(row=0,column=1)

        close_btn.bind("<Enter>", self.on_enter)
        close_btn.bind("<Leave>", self.on_leave)

        for btn in [view_individual_btn, close_btn]:
            btn.configure(relief=tk.FLAT, borderwidth=0)
 
        if len(self.destinations.destinations) > 0:
            view_individual_btn.configure(command=retrieve_selection, bg=button_color)
            view_individual_btn.bind("<Enter>", self.on_enter)
            view_individual_btn.bind("<Leave>", self.on_leave)


    def generic_window(self, window):
        button_color = '#3A9AFF'
        self.main_trips_img = tk.PhotoImage(file=self.trips_img_path).subsample(2)
        
        trip_main_window = tk.Toplevel(window)

        main_img_label = tk.Label(trip_main_window, image=self.main_trips_img)
        main_img_label.pack()
        
        main_title = tk.Label(trip_main_window,
                            text="Generic Window",
                            font="Helvetica 10 bold",
                            fg=button_color,
                            pady=10)
        main_title.pack()

        btn_width = int(self.main_trips_img.width())
        
    def on_enter(self,event):
        event.widget.config(bg='#6CD0FF')
    def on_leave(self,event):
        event.widget.config(bg='#3A9AFF')

    def close_window(self, window):
        window.destroy()