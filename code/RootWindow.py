
import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox

from ApplicationSpecs import Specs as spec
from read import Reader as rd
from write import Writer as wr
from AddCardWindow import AddCard
from CreateDeckWindow import CreateDeck 
from EditDeckWindow import EditDeck
from StudyWindow import Study
from DeleteDeckWindow import DeleteDeck

class Root:

    def __init__(self):
        self.root = tk.Tk()
        self.xpad, self.ypad = spec.get_std_xy_pad()
        self.font = ("Helvetica", 14)

        self.option_frame = ttk.Frame(master=self.root)
        self.config_option_frame()
        self.play_frame = ttk.Frame(master=self.root)
        self.config_play_frame()

        self.deck_listbox = tk.Listbox(master=self.play_frame, exportselection=False)
        self.display_deck_listbox()
        self.display_deck_listbox_scrollbar()

        self.create_deck_option(self.option_frame)
        self.add_card_option(self.option_frame)
        self.edit_deck_option(self.option_frame)
        self.delete_deck_option(self.option_frame)

        self.set_title()
        self.set_geometry()
        self.set_grid()
        self.main_label()
        self.play_label()

        self.check_deck_selection()
        
        self.root.mainloop()
        
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
        label = ttk.Label(self.root, text="StudyIT", font=("Arial", 18))
        label.grid(row = 0, column = 1, sticky = "n", padx=self.xpad, pady=self.ypad)
    
    def play_label(self):
        label = ttk.Label(self.play_frame, text="Select a Deck To Study OR Create a New One", font=self.font)
        label.grid(row = 0, column = 0)

    #frame
    def config_option_frame(self):
        self.option_frame.config(relief="solid")
        self.option_frame.grid(row = 0, column = 0, sticky="nsew", rowspan=3, padx=self.xpad, pady=self.ypad)
        self.option_frame.columnconfigure(0, weight = 1)
        self.option_frame.rowconfigure((0,1,2,3), weight = 1)
        self.option_frame.grid_propagate(False)
    
    def config_play_frame(self):
        self.play_frame.grid(row = 1, column = 1, sticky="nsew", rowspan=2, columnspan=2,
                             padx=self.xpad, pady=self.ypad)
        self.play_frame.columnconfigure(0, weight = 1)
        self.play_frame.rowconfigure(0, weight = 1)
        self.play_frame.rowconfigure(1, weight = 5)
        self.play_frame.grid_propagate(False)

####
    
    def display_deck_listbox(self):
        decks = rd.get_deck_names()
        listbox_variable = tk.Variable(value=decks)
        self.deck_listbox.config(listvariable=listbox_variable)
        self.deck_listbox.config(selectmode=tk.SINGLE)
        self.deck_listbox.config(height=5)
        self.deck_listbox.grid(row=1, column=0, sticky="nwse")

    def display_deck_listbox_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self.play_frame, orient=tk.VERTICAL, command=self.deck_listbox.yview)
        self.deck_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=1, column=0, sticky="nse")

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
        edit_deck_button.bind("<Button>", self.display_edit_deck_window)
    
    def delete_deck_option(self, frame):
        statistics_button = ttk.Button(frame)
        statistics_button.grid(row=3, column=0, sticky="nwse")
        statistics_button.config(text="Delete Deck")
        statistics_button.bind("<Button>", self.delete_deck_window)

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
        AddCardUI.display_sample_image()
        AddCardUI.display_labels()
        AddCardUI.display_deck_listbox()
        AddCardUI.display_deck_listbox_scrollbar()
        AddCardUI.display_term_textbox()
        AddCardUI.display_definition_textbox()
        AddCardUI.display_add_card_button()
        AddCardUI.display_add_image_button()
        
        
    def display_edit_deck_window(self, event):
        EditDeckUI = EditDeck()
        EditDeckUI.set_grid()
        EditDeckUI.set_root_geometry()
        EditDeckUI.display_deck_listbox()
        EditDeckUI.display_deck_listbox_scrollbar()
        EditDeckUI.display_card_listbox()
        EditDeckUI.display_card_listbox_scrollbar()
        EditDeckUI.check_selections()

    def delete_deck_window(self, event):
        DeleteDeckUI = DeleteDeck()
        DeleteDeckUI.set_grid()
        DeleteDeckUI.set_geometry()
        DeleteDeckUI.display_deck_listbox()
        DeleteDeckUI.display_deck_listbox_scrollbar()
        DeleteDeckUI.display_remove_deck_button()

    def display_study_window(self, deck):
        StudyUI = Study(deck)
        StudyUI.set_grid()
        StudyUI.set_geometry()
        StudyUI.display_card_select_listbox()
        StudyUI.display_card_select_scrollbar()
        StudyUI.display_prompt()
        StudyUI.display_buttons()

####

    def check_deck_selection(self):
        try: # user has selected a deck 
            deck = self.deck_listbox.get(self.deck_listbox.curselection())
            self.root.after(100, lambda: self.display_study_window(deck))
            self.deck_listbox.selection_clear(0, tk.END)
            self.root.after(100, self.check_deck_selection)
        except: # user has not selected a deck 
            self.display_deck_listbox()
            self.display_deck_listbox_scrollbar()

            self.root.after(100, self.check_deck_selection)