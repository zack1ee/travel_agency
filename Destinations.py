from Destination import Destination
from Utils import Utils
import tkinter as tk
from tkinter import ttk

class Destinations:
    def __init__(self, agency):
        self.agency = agency
        self.destinations = []
        self.destinations_img = None
        self.destinations_img_path = "assets/destination.png"
    
    def add_destinations(self, destination: Destination):
        if self.has_destination(destination.name, destination.country):
            pass
        else:
            self.destinations.append(destination)
            Utils.add_flights_for_destination(destination, self.agency)
    
    def remove_destination(self, destination: Destination):
        if self.has_destination(destination.name, destination.country) == False:
            from A_Exceptions import ExceptionWindow, ItemNotFoundException
            ExceptionWindow("ItemNotFoundException", "The item does not exist.")
            pass
        else:
            for d in self.destinations:
                if d.name == destination.name and d.country == destination.country:
                    self.destinations.remove(d)
                    return True
    
    def has_destination(self, name, country):
        for d in self.destinations:
            if d.name == name and d.country == country:
                return True
        return False
    
    def get_destination(self, name, country):
        if self.has_destination(name, country) == False:
            #throw error
            pass
        for d in self.destinations:
            if d.name == name and d.country == country:
                return d
        return None
    
    def insert_dummy_data(self):
        self.destinations.append(Destination("Eiffel Tower", "France"))
        self.destinations.append(Destination("Opera House", "Australia"))
        self.destinations.append(Destination("Uluru", "Australia"))
        self.destinations.append(Destination("Machu Picchu", "Peru"))
        self.destinations.append(Destination("Great Pyramids", "Egypt"))
        self.destinations.append(Destination("Niagara Falls", "Canada"))
        self.destinations.append(Destination("Great Barrier Reef", "Australia"))
        self.destinations.append(Destination("Grand Canyon", "USA"))
        self.destinations.append(Destination("Mount Everest", "Nepal/China"))
        self.destinations.append(Destination("Sahara Desert", "North Africa"))
        self.destinations.append(Destination("Great Wall of China", "China"))
        self.destinations.append(Destination("Galápagos Islands", "Ecuador"))
        self.destinations.append(Destination("Victoria Falls", "Zambia/Zimbabwe"))
        self.destinations.append(Destination("Aurora Borealis", "Arctic"))
        self.destinations.append(Destination("Machu Picchu", "Peru"))
        self.destinations.append(Destination("Antarctica", "Antarctica"))
        
        for d in self.destinations:
            Utils.add_flights_for_destination(d, self.agency)
        
    #buttons should be view destinations, view destinations by country, add dest, remove dest, and close
    def destination_window(self, window, admins):
        self.destinations_window = tk.Toplevel(window)
        self.destinations_window.title("Prog 2 Travel Agency")
        blue='#3A9AFF'
        color = 'black'
        button_width = 23
        button_height = 1

        try:
            self.destinations_img = tk.PhotoImage(file=self.destinations_img_path)
            self.destinations_img = self.destinations_img.subsample(2)
            img_label = tk.Label(self.destinations_window, image=self.destinations_img)
            img_label.pack()
        except tk.TclError:
            print("Failure.")

        welcome_label = tk.Label(self.destinations_window,
                                 text=f"Welcome {admins.name} to The Destinations Section",
                                 font="25", 
                                 fg=blue,
                                 pady=15)
        welcome_label.pack()

        self.destination_btn_frame = tk.Frame(self.destinations_window)
        self.destination_btn_frame.pack()

        view_all_d_btn = tk.Button(
            self.destination_btn_frame,
            text="View Destinations",
            bg=color,
            fg=color,
            width=button_width,
            height=button_height,
            command=lambda:self.viewalldestination(self.destinations_window)
            )
        view_all_d_btn.grid(row=2,column=0)

        filter_destination_btn = tk.Button(
            self.destination_btn_frame,
            text="View Destinations by Country",
            bg=color,
            fg='black',
            width=button_width,
            height=button_height,
            command=lambda:self.destination_filtered(self.destinations_window)
            )
        filter_destination_btn.grid(row=2,column=1)

        add_destination_btn = tk.Button(
            self.destination_btn_frame,
            text="Add Destination",
            bg=color,
            fg='black',
            width=button_width,
            height=button_height,
            command=lambda:self.add_destination(self.destinations_window)
            )
        add_destination_btn.grid(row=2,column=2)

        remove_destination_btn = tk.Button(
            self.destination_btn_frame,
            text="Remove Destination",
            bg=color,
            fg='black',
            width=button_width,
            height=button_height,
            command=lambda:self.remove_destination(self.destinations_window)
            )
        remove_destination_btn.grid(row=2,column=3)

        close_destination_btn = tk.Button(
            self.destination_btn_frame,
            text="Close",
            bg=color,
            fg="black",
            width=button_width,
            height=button_height,
            command=lambda: self.close_window(self.destinations_window)
        )
        close_destination_btn.grid(row=2,column=4)

        for btn in [view_all_d_btn,
                    filter_destination_btn,
                    add_destination_btn,
                    remove_destination_btn,
                    close_destination_btn]:
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            btn.configure(relief=tk.FLAT, borderwidth=0)
    
    def close_window(self, window):
        window.destroy()
    
    def viewalldestination(self, window):
        color = '#3A9AFF'
        view_all_window = tk.Toplevel(window)

        self.img = tk.PhotoImage(file=self.destinations_img_path)
        self.img = self.img.subsample(2)
        self.img_label = tk.Label(view_all_window, image=self.img)
        self.img_label.pack()

        title_label = tk.Label(view_all_window, text="Destinations", font="25", fg='Black', pady=10)
        title_label.pack()

        #treeview

        s = ttk.Style()
        s.theme_use('default')
        s.configure('Treeview.Heading', font='15', fg='white')

        col = ('Name','Country')

        treeview_frame = tk.Frame(view_all_window, pady=10)
        treeview_frame.pack()

        treeview = ttk.Treeview(treeview_frame, columns=col, show='headings')
        for c in col:
            treeview.column(c, anchor=tk.W, width=int((self.img.width() / 2)), stretch=tk.NO)
            treeview.heading(c, text=c)

        treeview.grid(row=0, column=0, sticky="nsew")

        vsb = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        treeview.configure(yscrollcommand=vsb.set)

        treeview_frame.grid_rowconfigure(0, weight=1)
        treeview_frame.grid_columnconfigure(0, weight=1)

        for d in self.destinations:
            name = d.name
            country = d.country
            details = [name,country]
            if self.destinations.index(d) % 2 == 0:
                        treeview.insert('', tk.END, values=details, tags=("even_row",))
            else:
                treeview.insert('', tk.END, values=details, tags=("odd_row",))
        
        treeview.tag_configure('even_row', background='#e8e6e6')
        treeview.tag_configure('odd_row', background='white')


        close_button = tk.Button(view_all_window, 
                              text="Close",
                                font='15',
                              fg=color,
                              width=105,
                              height=1,
                              command=lambda:self.close_window(view_all_window))
        close_button.pack()

        close_button.bind("<Enter>", self.on_enter)
        close_button.bind("<Leave>", self.on_leave)
        close_button.configure(relief=tk.FLAT, borderwidth=0)
    
    def destination_filtered(self, window):
        color = '#3A9AFF'
        filter_d_window = tk.Toplevel(window)

        self.filter_destinations_img = tk.PhotoImage(file=self.destinations_img_path)
        self.filter_destinations_img_s = self.filter_destinations_img.subsample(2)
        self.img_label = tk.Label(filter_d_window, image=self.filter_destinations_img_s)
        self.img_label.pack()

        title_label = tk.Label(filter_d_window, text="Destinations",  fg='black', pady=10)
        title_label.pack()

        search_entry = tk.Entry(filter_d_window, font="25", width=116)
        search_entry.pack()

        s = ttk.Style()
        s.theme_use('default')
        s.configure('Treeview.Heading', font=("Helvetica", 15))

        col = ('Name', 'Country')
        treeview_frame = tk.Frame(filter_d_window, pady=10)
        treeview_frame.pack()

        treeview = ttk.Treeview(treeview_frame, columns=col, show='headings')
        for c in col:
            treeview.column(c, anchor=tk.W, width=int(self.filter_destinations_img_s.width()/2), stretch=tk.NO)
            treeview.heading(c, text=c)
        treeview.grid(row=0, column=0, sticky="nsew")

        vsb = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        treeview.configure(yscrollcommand=vsb.set)

        treeview_frame.grid_rowconfigure(0, weight=1)
        treeview_frame.grid_columnconfigure(0, weight=1)

        if not search_entry.get():
            for d in self.destinations:
                    country = d.country
                    name = d.name
                    details = [name,country]
                    if self.destinations.index(d) % 2 == 0:
                        treeview.insert('', tk.END, values=details, tags=("even_row",))
                    else:
                        treeview.insert('', tk.END, values=details, tags=("odd_row",))
            
            treeview.tag_configure('even_row', background='#e8e6e6')
        treeview.tag_configure('odd_row', background='white')
        
        def update_d_list(event):
            search_for = search_entry.get()
            treeview.delete(*treeview.get_children())

            if search_for:
                for d in self.get_filtered_destinations(search_for):
                    country = d.country
                    name = d.name
                    details = [name,country]
                    if self.destinations.index(d) % 2 == 0:
                        treeview.insert('', tk.END, values=details, tags=("even_row",))
                    else:
                        treeview.insert('', tk.END, values=details, tags=("odd_row",))
                
                treeview.tag_configure('even_row', background='#e8e6e6')
                treeview.tag_configure('odd_row', background='white')
                    
            elif search_for == "":
                for d in self.destinations:
                    country = d.country
                    name = d.name
                    details = [name,country]
                    if self.destinations.index(d) % 2 == 0:
                        treeview.insert('', tk.END, values=details, tags=("even_row",))
                    else:
                        treeview.insert('', tk.END, values=details, tags=("odd_row",))
                
                treeview.tag_configure('even_row', background='#e8e6e6')
                treeview.tag_configure('odd_row', background='white')

        search_entry.bind('<KeyRelease>', update_d_list)

        close_button = tk.Button(filter_d_window, 
                              text="Close",
                              font="15",
                              fg='black',
                              width=105,
                              height=1,
                              command=lambda:self.close_window(filter_d_window))
        close_button.pack()

        close_button.bind("<Enter>", self.on_enter)
        close_button.bind("<Leave>", self.on_leave)
        close_button.configure(relief=tk.FLAT, borderwidth=0)

    def add_destination(self,window):
        button_color = '#3A9AFF'
        add_d_window = tk.Toplevel(window)

        self.add_img = tk.PhotoImage(file=self.destinations_img_path)
        self.add_img = self.add_img.subsample(2)
        self.add_img_label = tk.Label(add_d_window, image=self.add_img)
        self.add_img_label.pack()

        title_label = tk.Label(add_d_window, text="Destinations", font="Helvetica 20 bold", fg=button_color, pady=10)
        title_label.pack()

        entry_frame = tk.Frame(add_d_window, pady=10)
        entry_frame.pack()

        name_label = tk.Label(entry_frame,text="Name:", font="Helvetica 11 bold", fg=button_color)
        name_label.grid(row=0,column=0)

        country_lable = tk.Label(entry_frame,text="Country:", font="Helvetica 11 bold", fg=button_color)
        country_lable.grid(row=1,column=0)

        name_entry = tk.Entry(entry_frame, font="Helvetica 11")
        name_entry.grid(row=0,column=1)
        
        country_entry = tk.Entry(entry_frame, font="Helvetica 11")
        country_entry.grid(row=1,column=1)

        button_frame = tk.Frame(add_d_window)
        button_frame.pack()

        def create_destination():
            name = name_entry.get()
            country = country_entry.get()
            dest = Destination(name,country)
            self.add_destinations(dest)
            self.close_window(add_d_window)

        add_destination_buttonn = tk.Button(button_frame,
                               text="Add destination",
                               fg='black',
                               width=60
                               )
        add_destination_buttonn.grid(row=0,column=0)

        close_button = tk.Button(button_frame, 
                              text="Close",
                              fg='black',
                              width=60,
                              command=lambda:self.close_window(add_d_window)
                              )
        close_button.grid(row=0,column=1)
        
        add_destination_buttonn.configure(relief=tk.FLAT, borderwidth=0)

        close_button.configure(relief=tk.FLAT, borderwidth=0)
        close_button.bind("<Enter>", self.on_enter)
        close_button.bind("<Leave>", self.on_leave)
        
        def update_btn_state(event):
            if country_entry.get() and name_entry.get():
                add_destination_buttonn.config(command=create_destination, bg=button_color,fg='white') #enable
                add_destination_buttonn.bind("<Enter>", self.on_enter)
                add_destination_buttonn.bind("<Leave>", self.on_leave)
            else:
                try:
                    add_destination_buttonn.config(command=None, bg='#7CBCFF',fg='white') #disable
                    add_destination_buttonn.unbind("<Enter>", self.on_enter)
                    add_destination_buttonn.unbind("<Leave>", self.on_leave)
                except TypeError:
                    pass
        
        name_entry.bind("<KeyRelease>", update_btn_state)
        country_entry.bind("<KeyRelease>", update_btn_state)
            
    def remove_destination(self,window):
        color = '#3A9AFF'
        remove_d_window = tk.Toplevel(window)

        self.remove_img = tk.PhotoImage(file=self.destinations_img_path)
        self.remove_img = self.remove_img.subsample(2)

        self.img_label = tk.Label(remove_d_window, image=self.remove_img)
        self.img_label.pack()

        title_label = tk.Label(remove_d_window, text="Remove a destination", font="Helvetica 25 ", fg=color)
        title_label.pack()

        entry_frame = tk.Frame(remove_d_window, pady=10)
        entry_frame.pack()

        name_label = tk.Label(entry_frame,text="Name:", font="Helvetica 15 ", fg=color)
        name_label.grid(row=0,column=0)

        country_label = tk.Label(entry_frame,text="Country:", font="Helvetica 15 ", fg=color)
        country_label.grid(row=1,column=0)

        name_entry = tk.Entry(entry_frame, font="Helvetica 8")
        name_entry.grid(row=0,column=1)
        
        country_entry = tk.Entry(entry_frame, font="Helvetica 8")
        country_entry.grid(row=1,column=1)

        def destroy_destination():
            name = name_entry.get()
            country = country_entry.get()
            if self.has_destination(name,country):
                destination = Destination(name,country)
                self.remove_destination(destination)
                self.close_window(remove_d_window)
            else:
                from A_Exceptions import ItemNotFoundException, ExceptionWindow
                ExceptionWindow("ItemNotFoundException", "This item does not exist!")

        button_frame = tk.Frame(remove_d_window)
        button_frame.pack()

        remove_destination_button = tk.Button(button_frame,
                               text="Remove destination",
                               fg='black',
                               bg='#7CBCFF',
                               width=60,
                               command=destroy_destination,
                               state=tk.DISABLED)
        remove_destination_button.grid(row=0,column=0)
        remove_destination_button.configure(relief=tk.FLAT, borderwidth=0)

        close_button = tk.Button(button_frame, 
                              text="Close",
                              bg=color,
                              fg='black',
                              width=60,
                              command=lambda:self.close_window(remove_d_window))
        close_button.grid(row=0,column=1)

        def update_btn_state(event):
            if country_entry.get() and name_entry.get():
                remove_destination_button.config(command=destroy_destination, bg=color,fg=color,state=tk.NORMAL) #enable
                remove_destination_button.bind("<Enter>", self.on_enter)
                remove_destination_button.bind("<Leave>", self.on_leave)
            else:
                try:
                    remove_destination_button.config(command=None, bg='#7CBCFF',fg=color) #disable
                    remove_destination_button.unbind("<Enter>", self.on_enter)
                    remove_destination_button.unbind("<Leave>", self.on_leave)
                except TypeError:
                    pass
        
        name_entry.bind("<KeyRelease>", update_btn_state)
        country_entry.bind("<KeyRelease>", update_btn_state)

        for button in [close_button]:
            button.bind("<Enter>", self.on_enter)
            button.bind("<Leave>", self.on_leave)
            button.configure(relief=tk.FLAT, borderwidth=0)
        
        

    def on_enter(self,event):
        event.widget.config()
    def on_leave(self,event):
        event.widget.config(bg='#3A9AFF')
    
    def get_filtered_destinations(self,query):
        filtered = [ ]
        for d in self.destinations:
            if query.lower() in d.country.lower():
                filtered.append(d)
        return filtered