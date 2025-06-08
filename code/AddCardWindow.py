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
        self.spec = spec()
        
        self.term_textbox = tk.Text(master=self.window)
        self.definition_textbox = tk.Text(master=self.window)
        self.deck_listbox = tk.Listbox(master=self.window)


    def set_grid(self):
        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure((1,2), weight = 1)
        self.window.rowconfigure((0,1,2), weight = 1)
        self.window.rowconfigure(3, weight = 2)
    
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
        deck_to_add_to_label = ttk.Label(self.window, text="Deck", font=("Helvetica", 14))
        deck_to_add_to_label.grid(row = 0, column = 1, sticky="w")
        term_label = ttk.Label(self.window, text="Term", font=("Helvetica", 14))
        term_label.grid(row = 1, column = 1, sticky="w")
        definition_label = ttk.Label(self.window, text="Definition", font=("Helvetica", 14))
        definition_label.grid(row = 2, column = 1, sticky="w")
        img_label = ttk.Label(self.window, text="image", font=("Helvetica", 14))
        img_label.grid(row = 3, column = 1, sticky="nw")

    def display_deck_listbox(self):
        #listbox
        decks = self.rd.get_deck_names()
        listbox_variable = tk.Variable(value=decks)
        self.deck_listbox.config(listvariable=listbox_variable)
        self.deck_listbox.config(selectmode=tk.SINGLE)
        self.deck_listbox.config(height=3)
        self.deck_listbox.grid(row=0, column=0,sticky="we", padx=20)

        #scroll bar
        vertical_scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.deck_listbox.yview)
        self.deck_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=0, column=0, sticky="e")
    
    def display_term_textbox(self):
        self.term_textbox.config(height=2)
        self.term_textbox.grid(row=1, column=0, sticky="we", padx=20)

    def display_definition_textbox(self):
        self.definition_textbox.config(height=3)
        self.definition_textbox.grid(row=2, column=0, sticky="we", padx=20)

    def display_add_image_button(self):
        add_image_button = ttk.Button(self.window, text="Add")
        add_image_button.grid(row=3, column=0, sticky="ne", padx=20)
        add_image_button.bind("<Button>", self.file_popup)

    def file_popup(self, event):
        print("asdd")

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