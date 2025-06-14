import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox
from tkinter import filedialog

from ApplicationSpecs import Specs as spec
from read import Reader as rd

class AddCard():

    def __init__(self):
        self.rd = rd() # reader object
        self.window = tk.Toplevel()
        self.frame = ttk.Frame(master=self.window)
        
        self.xpad, self.ypad = spec.get_std_xpad_ypad()
        self.portion_width, self.portion_height = spec.get_portion_dimensions_large_window_geomtry()
        
        self.deck_listbox = tk.Listbox(master=self.frame)
        self.term_entrybox = ttk.Entry(master=self.frame)
        self.definition_entrybox = ttk.Entry(master=self.frame)
        

    def set_grid(self):
        self.window.columnconfigure((0,1,2,3), weight = 1)
        self.window.rowconfigure((0,1,2,3), weight = 1)
    
    def set_frame_grid(self):
        self.frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=self.xpad)
        self.frame.columnconfigure(0, weight=2)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure((0,1,2), weight=1)


    def set_geometry(self):
        window_width, window_height = spec.get_large_window_geometry()
        self.window.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}")

    # def add_card_window_set_up(self, event):
    #     sub_window_width, sub_window_height = self.get_large_window_geometry()
    #     add_card_window = tk.Toplevel()
    #     add_card_window.geometry(self.spec.get_geometry_tuple(sub_window_width, sub_window_height))
    #     self.set_add_card_window_grid(add_card_window)
    #     self.display_add_card_window_ui(add_card_window)

    def display_labels(self):
        deck_to_add_to_label = ttk.Label(self.frame, text="Deck", font=("Helvetica", 14))
        deck_to_add_to_label.grid(row = 0, column = 1)
        term_label = ttk.Label(self.frame, text="Term", font=("Helvetica", 14))
        term_label.grid(row = 1, column = 1)
        definition_label = ttk.Label(self.frame, text="Definition", font=("Helvetica", 14))
        definition_label.grid(row = 2, column = 1)
        img_label = ttk.Label(self.window, text="image", font=("Helvetica", 14))
        img_label.grid(row = 3, column = 0, sticky="n")

    def display_deck_listbox(self):
        #listbox
        decks = self.rd.get_deck_names()
        listbox_variable = tk.Variable(value=decks)
        self.deck_listbox.config(listvariable=listbox_variable, selectmode=tk.SINGLE, height=3)
        self.deck_listbox.grid(row=0, column=0, sticky="we")

        #scroll bar
        vertical_scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.deck_listbox.yview)
        self.deck_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=0, column=1, sticky="w")
    
    def display_term_entrybox(self):
        self.term_entrybox.grid(row=1, column=0, sticky="we")

    def display_definition_entrybox(self):
        self.definition_entrybox.grid(row=2, column=0, sticky="we")

    def display_add_image_button(self):
        add_image_button = ttk.Button(self.window, text="Add")
        add_image_button.grid(row=3, column=0, sticky="ne", padx=20)
        add_image_button.bind("<Button>", self.file_manager_popup)

    def file_manager_popup(self, event):
        pass

    def display_add_card_button(self):
        add_card = ttk.Button(master=self.window, text="Add card")
        add_card.grid(row=3, column=2)
        add_card.bind("<Button>", self.add_card)

    def add_card(self, event):
        try: # determine deck to save card to
            deck_to_save_to = self.deck_listbox.get(self.deck_listbox.curselection())
        except: # user failed to specify deck
            ### message box to select a deck 
            pass
        try: # get term entry
            pass
        except:
            pass