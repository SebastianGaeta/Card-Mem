
import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox

from read import Reader as rd
from write import Writer as wr
from ApplicationSpecs import Specs as spec


class CreateDeck:


    def __init__(self):
        self.window = tk.Toplevel()
        self.entry = ttk.Entry(self.window)

    def set_geometry(self):
        window_width, window_height = spec.get_small_window_geometry()
        self.window.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}")
    
    def set_grid(self):
        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(1, weight = 3)
        self.window.rowconfigure((0,1), weight = 1)

    def set_prompt(self):
        prompt = ttk.Label(self.window, text = "Deck Name:", font=("Helvetica", 15))
        prompt.grid(row = 0, column = 0, sticky="e")
    
    def set_entry(self):
        self.entry.grid(row = 0, column = 1, sticky = "we", padx = 30)

    def set_button(self):
        enter_button = ttk.Button(self.window, text = "Enter")
        enter_button.grid(row = 1, column = 1, sticky = "e", padx = 30)
        enter_button.bind("<Button>", self.create_deck_command)
        
    def create_deck_command(self, event):
        deck_name = self.entry.get()
        if deck_name != "": # check for valid name
            writer = wr()
            writer.create_parent_deck_directory()
            writer.create_deck_folder(deck_name, self.window)
        else: # no name was given -> reprompt
            messagebox.showinfo(title="information", message="Enter a Name")
