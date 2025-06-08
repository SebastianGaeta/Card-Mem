
import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox

from read import Reader as rd
from write import Writer as wr
from AddCardWindow import AddCard
from ApplicationSpecs import Specs as spec
from CreateDeckWindow import CreateDeck 


class Root:

    def __init__(self):
        self.root = tk.Tk()
        self.xpad, self.ypad = spec.get_std_xpad_ypad()
        self.set_title()
        self.set_geometry()
        self.set_grid()
        self.main_label()
        self.set_option_frame()
        self.root.mainloop()

    def run(self):
        pass
        
    def set_title(self): 
        self.root.title("StudyIT")

    def set_geometry(self):
        window_width, window_height = spec.get_large_window_geometry()
        center_x, center_y = spec.get_centered_window(window_width, window_height)
        self.root.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}+{center_x}+{center_y}") # set root geometry

    def set_grid(self):
        self.root.columnconfigure((0,1,2), weight = 1) 
        self.root.rowconfigure((0,1,2), weight = 1) 

    def main_label(self):
        label = ttk.Label(self.root, text="Card Memory Game", font=("Arial", 18))
        label.grid(row = 0, column = 1, sticky = "n", padx=self.xpad, pady=self.ypad)
    
    #frame
    def set_option_frame(self):
        frame = ttk.Frame(self.root)
        frame.grid(row = 0, column = 0, sticky="nsew", rowspan=3, padx=self.xpad, pady=self.ypad)
        frame.config(relief="solid")
        self.set_option_frame_grid(frame) 
        self.create_deck_option(frame)
        self.add_card_option(frame)
        self.add_card_option(frame)
        self.statistics_option(frame)

    def set_option_frame_grid(self, frame):
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure((0,1,2,3), weight = 1)

    #buttons
    def create_deck_option(self, frame):
        create_deck_button = ttk.Button(frame)
        create_deck_button.grid(row=0, column=0, sticky="nswe")
        create_deck_button.config(text="Create Deck")
        create_deck_button.bind("<Button>", self.display_create_deck_window)

    def add_card_option(self, frame):
        add_card_button = ttk.Button(frame)
        add_card_button.grid(row = 1, column = 0, sticky="nswe")
        add_card_button.config(text = "Add Card")
        add_card_button.bind("<Button>", self.display_add_card_window)

    def edit_deck_option(self, frame):
        edit_deck_button = ttk.Button(frame)
        edit_deck_button.grid(row=2, column=0, sticky="nswe")
        edit_deck_button.config(text="Edit Deck")
        edit_deck_button.bind("<Button>", self.dummy)
    
    def statistics_option(self, frame):
        statistics_button = ttk.Button(frame)
        statistics_button.grid(row=3, column=0, sticky="nswe")
        statistics_button.config(text="Statistics")
        statistics_button.bind("<Button>", self.dummy)

    ############### sub windows ###############
    def display_create_deck_window(self, event):
        CreateDeckUI = CreateDeck()
        CreateDeckUI.set_geometry()
        CreateDeckUI.set_grid()
        CreateDeckUI.set_prompt()
        CreateDeckUI.set_button()
        CreateDeckUI.set_entry()

    def display_add_card_window(self, event):
        AddCardUI = AddCard()
        AddCardUI.set_grid()
        AddCardUI.set_geometry()
        AddCardUI.display_labels()
        AddCardUI.display_deck_listbox()
        AddCardUI.display_term_textbox()
        AddCardUI.display_definition_textbox()
        AddCardUI.display_add_card_button()
        AddCardUI.display_add_image_button()

    def dummy(self, event):
        pass