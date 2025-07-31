

import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

from read import Reader as rd
from write import Writer as wr
from ApplicationSpecs import Specs as spec
from pathlib import Path



class DeleteDeck:

    def __init__(self):
        self.window = tk.Toplevel()
        self.x_buffer, self.y_buffer = spec.get_std_xy_pad()

        self.deck_frame = ttk.Frame(master=self.window)
        self.config_deck_frame()

        self.deck_listbox = tk.Listbox(master=self.deck_frame, exportselection=False)

        


    def set_geometry(self):
        window_width, window_height = spec.get_small_window_geometry()
        self.window.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}")
    
    def set_grid(self):
        self.window.columnconfigure(0, weight = 3)
        self.window.columnconfigure(1, weight = 1)
        self.window.rowconfigure(0, weight = 1)

#### frames ####

    def config_deck_frame(self):
        self.deck_frame.grid(row=0, column=0, sticky="nwse", padx=self.x_buffer, pady=self.y_buffer)
        self.deck_frame.columnconfigure(0, weight=1)
        self.deck_frame.rowconfigure(0, weight=1)
        self.deck_frame.grid_propagate(False)

################

    def display_deck_listbox(self):
        decks = rd.get_deck_names()
        listbox_variable = tk.Variable(value=decks)
        self.deck_listbox.config(listvariable=listbox_variable)
        self.deck_listbox.config(selectmode=tk.SINGLE)
        self.deck_listbox.config(height=12)
        self.deck_listbox.grid(row=0, column=0, sticky="nswe")

    def display_deck_listbox_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self.deck_frame, orient=tk.VERTICAL, command=self.deck_listbox.yview)
        self.deck_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=0, column=0, sticky="nse")

    def display_remove_deck_button(self):
        delete_button = ttk.Button(self.window, text = "Delete")
        delete_button.grid(row = 0, column = 1, sticky = "se", padx=self.x_buffer, pady=self.y_buffer)
        delete_button.bind("<Button>", self.delete_deck)
    
    def delete_deck(self, event):
        try:
            deck = self.deck_listbox.get(self.deck_listbox.curselection())
            deck_directory = Path(f"{rd.get_deck_directory()}\\{deck}")
            if (rd.delete_deck(deck_directory)):
                messagebox.showinfo(title="Information", 
                                    message="Deck Successfully Deleted",
                                    parent=self.window)
            else:
                messagebox.showerror(title="Error",
                                    message="Deck was Unable to be Deleted",
                                    parent=self.window)
            
            self.display_deck_listbox() # update current state
            self.display_deck_listbox_scrollbar() # update current state
        except:
            pass