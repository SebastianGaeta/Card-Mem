import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox



class UserInterface:
    
    def __init__(self): 
        self.root = tk.Tk() # create root
        self.set_root_title() # set root title
        self.set_root_geometry() # set geometry
        self.set_root_grid() # set grid for root
        self.display_root_UI() # display all UI relating to root
        self.root.mainloop()

    # screen dimenion getters 
    def get_screen_dimensions(self): 
        return self.root.winfo_screenwidth(), self.root.winfo_screenheight() # return tuple in form (width, height)

    def get_root_dimensions(self):
        screen_width, screen_height = self.get_screen_dimensions()
        window_width = screen_width // 2 # window width
        window_height = screen_height // 2 # window height
        return window_width, window_height # returns tuple (width, height)

    def get_root_centered_dimensions(self):
        screen_width, screen_height = self.get_screen_dimensions()
        window_width = screen_width // 2 # window width
        window_height = screen_height // 2 # window height
        center_x = int(screen_width/2 - window_width/2) # x center screen
        center_y = int(screen_height/2 - window_height/2) # y center screen
        return center_x, center_y # returns tuple (width, height)

    def get_sub_window_geometry(self):
        screen_width, screen_height = self.get_screen_dimensions()
        return screen_width // 4, screen_height // 4  # return tuple in form (width, height)
    
    def get_geometry_tuple(self, width, height):
        return f"{width}x{height}"
    
    # root config stuff
    def set_root_title(self): 
        self.root.title("Card memory game")

    def set_root_geometry(self):
        window_width, window_height = self.get_root_dimensions()
        center_x, center_y = self.get_root_centered_dimensions()
        self.root.geometry(f"{self.get_geometry_tuple(window_width, window_height)}+{center_x}+{center_y}") # set root geometry

    def set_root_grid(self):
        self.root.columnconfigure((0,1,2), weight = 1) # 3 columns
        self.root.rowconfigure((0,1,2), weight = 1) # 3 rows
        
    def set_root_option_frame_grid(self, frame):
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure((0,1,2,3), weight = 1)

    # root UI
    def display_root_UI(self):
        self.root_main_label()
        self.root_options_frame()

    def root_main_label(self):
        message = ttk.Label(self.root)
        message.config(text="Card Memory Game")
        message.config(font=("Arial", 18))
        message.grid(row = 0, column = 1, sticky = "n")
    
    def root_options_frame(self):
        frame = ttk.Frame(self.root)
        frame.grid(row = 0, column = 0, sticky="nsew", rowspan=3, padx= 20, pady = 20) #pad is skewing center
        frame.config(relief="solid")
        self.set_root_option_frame_grid(frame) # set grid system for frame
        self.root_create_deck_option(frame)
        self.root_edit_deck_option(frame)
        self.root_statistics_option(frame)


    
    def root_statistics_option(self, frame):
        statistics_button = ttk.Button(frame)
        statistics_button.grid(row=3, column=0, sticky="nswe")
        statistics_button.config(text="Statistics")
        statistics_button.bind("<Button>", self.open_statistics_window)

    def open_statistics_window(self, event):
        sub_window_width, sub_window_height = self.get_sub_window_geometry()
        statistics_window = tk.Toplevel()
        statistics_window.geometry(self.get_geometry_tuple(sub_window_width, sub_window_height))


    # edit_deck window methods
    def root_edit_deck_option(self, frame):
        edit_deck_button = ttk.Button(frame)
        edit_deck_button.grid(row=2, column=0, sticky="nswe")
        edit_deck_button.config(text="Edit Deck")
        edit_deck_button.bind("<Button>", self.open_edit_deck_window)

    def open_edit_deck_window(self, event):
        sub_window_width, sub_window_height = self.get_sub_window_geometry()
        edit_deck_window = tk.Toplevel()
        edit_deck_window.geometry(self.get_geometry_tuple(sub_window_width, sub_window_height))

    # create-deck window methods 
    def root_create_deck_option(self, frame):
        create_deck_button = ttk.Button(frame)
        create_deck_button.grid(row=0, column=0, sticky="nswe")
        create_deck_button.config(text="Create Deck")
        create_deck_button.bind("<Button>", self.open_create_deck_window)

    def open_create_deck_window(self, event):
        sub_window_width, sub_window_height = self.get_sub_window_geometry()
        create_deck_window = tk.Toplevel()
        create_deck_window.geometry(self.get_geometry_tuple(sub_window_width, sub_window_height))
        self.set_create_deck_window_grid(create_deck_window)
        self.create_deck_window_label(create_deck_window)
        self.create_deck_window_entry(create_deck_window)

    def set_create_deck_window_grid(self, window):
        window.columnconfigure(0, weight = 1)
        window.columnconfigure(1, weight = 3)
        window.rowconfigure((0,1), weight = 1)

    def create_deck_window_label(self, window):
        prompt = ttk.Label(window, text = "Deck Name:", font=("Helvetica", 15))
        prompt.grid(row = 0, column = 0)
    
    def create_deck_window_entry(self, window):
        name_entry = ttk.Entry(window)
        enter_button = ttk.Button(window, text = "Enter")
        name_entry.grid(row = 0, column = 1, sticky = "we",padx = 30)
        enter_button.grid(row = 1, column = 1, sticky = "e", padx = 30)
        enter_button.config(command = lambda: self.create_deck_window_button_command(name_entry, window))
        
    def create_deck_window_button_command(self, entry, window):
        deck_name = entry.get()
        if deck_name != "": # check for valid name
            wr.create_deck_folder(deck_name, window)
        else: # no name was given -> reprompt
            messagebox.showinfo(title="information", message="Enter a Name")
        
        