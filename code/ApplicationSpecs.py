import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox

from read import Reader as rd
from write import Writer as wr


class Specs:
    
    def __init__(self): 
        pass

    # screen dimenion getters 
    @staticmethod
    def get_screen_dimensions(): 
        window = tk.Tk()
        screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
        window.destroy()
        return screen_width, screen_height # return tuple in form (width, height)

    @staticmethod
    def get_centered_window(screen_width, screen_height):
        window_width = screen_width // 2 # window width
        window_height = screen_height // 2 # window height
        center_x = int(screen_width/2 - window_width/2) # x center screen
        center_y = int(screen_height/2 - window_height/2) # y center screen
        return center_x, center_y # returns tuple (width, height)

    @staticmethod
    def get_small_window_geometry():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width // 4, screen_height // 4  # return tuple in form (width, height)

    @staticmethod
    def get_medium_window_geometry():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width // 3, screen_height // 3  # return tuple in form (width, height)
   
    @staticmethod
    def get_large_window_geometry():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width // 2, screen_height // 2  # return tuple in form (width, height)
    
    @staticmethod
    def get_std_xpad_ypad():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width * 0.005, screen_height * 0.005
    
    @staticmethod
    def get_geometry_tuple(width, height):
        return f"{width}x{height}"



##########################################################################
    # root frame add card option

    
    # def set_term_entry_box(self, window):
    #     entry_box = ttk.Entry(window)
    #     entry_box.grid(row=1, column=0, sticky="we", padx=20)


##########################################################################

    # # statistics option
    # def root_statistics_option(self, frame):
    #     statistics_button = ttk.Button(frame)
    #     statistics_button.grid(row=3, column=0, sticky="nswe")
    #     statistics_button.config(text="Statistics")
    #     statistics_button.bind("<Button>", self.open_statistics_window)

    # def open_statistics_window(self, event):
    #     sub_window_width, sub_window_height = self.get_small_window_geometry()
    #     statistics_window = tk.Toplevel()
    #     statistics_window.geometry(self.get_geometry_tuple(sub_window_width, sub_window_height))


    # # edit_deck window methods
    # def root_edit_deck_option(self, frame):
    #     edit_deck_button = ttk.Button(frame)
    #     edit_deck_button.grid(row=2, column=0, sticky="nswe")
    #     edit_deck_button.config(text="Edit Deck")
    #     edit_deck_button.bind("<Button>", self.open_edit_deck_window)

    # def open_edit_deck_window(self, event):
    #     sub_window_width, sub_window_height = self.get_small_window_geometry()
    #     edit_deck_window = tk.Toplevel()
    #     edit_deck_window.geometry(self.get_geometry_tuple(sub_window_width, sub_window_height))

    # create-deck window methods 

    
    # def root_create_deck_option(self, frame):
    #     create_deck_button = ttk.Button(frame)
    #     create_deck_button.grid(row=0, column=0, sticky="nswe")
    #     create_deck_button.config(text="Create Deck")
    #     create_deck_button.bind("<Button>", self.open_create_deck_window)

    # def open_create_deck_window(self, event):
    #     sub_window_width, sub_window_height = self.get_small_window_geometry()
    #     create_deck_window = tk.Toplevel()
    #     create_deck_window.geometry(self.get_geometry_tuple(sub_window_width, sub_window_height))
    #     self.set_create_deck_window_grid(create_deck_window)
    #     self.create_deck_window_label(create_deck_window)
    #     self.create_deck_window_entry(create_deck_window)

    # def set_create_deck_window_grid(self, window):
    #     window.columnconfigure(0, weight = 1)
    #     window.columnconfigure(1, weight = 3)
    #     window.rowconfigure((0,1), weight = 1)

    # def create_deck_window_label(self, window):
    #     prompt = ttk.Label(window, text = "Deck Name:", font=("Helvetica", 15))
    #     prompt.grid(row = 0, column = 0)
    
    # def create_deck_window_entry(self, window):
    #     name_entry = ttk.Entry(window)
    #     enter_button = ttk.Button(window, text = "Enter")
    #     name_entry.grid(row = 0, column = 1, sticky = "we",padx = 30)
    #     enter_button.grid(row = 1, column = 1, sticky = "e", padx = 30)
    #     enter_button.config(command = lambda: self.create_deck_window_button_command(name_entry, window))
        
    # def create_deck_window_button_command(self, name_entry, window):
    #     deck_name = name_entry.get()
    #     if deck_name != "": # check for valid name
    #         writer = wr()
    #         writer.create_parent_deck_directory()
    #         writer.create_deck_folder(deck_name, window)
    #     else: # no name was given -> reprompt
    #         messagebox.showinfo(title="information", message="Enter a Name")
        
        