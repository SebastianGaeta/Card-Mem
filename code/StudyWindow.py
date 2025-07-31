


import tkinter as tk
from tkinter import ttk 
from read import Reader as rd
from write import Writer as wr
from ApplicationSpecs import Specs as spec
import random
from PIL import ImageTk, Image



class Study:


    def __init__(self, deck: str) -> None:
        self.window = tk.Toplevel()
        self.window.bind("<Key-space>", self.on_space_bar)
        
        self.x_buffer, self.y_buffer = spec.get_std_xy_pad()
        self.font = ("Arial", 14)
        self.all_selected = False
       
        self.deck = deck
        self.cards = []
        self.card_index = 0
        
        self.current_image_file = None
        self.image_label = ttk.Label() 
        self.image = None


        self.options_frame = ttk.Frame(master=self.window)
        self.config_options_frame()

        self.card_select_frame = ttk.Frame(master=self.options_frame)
        self.config_card_select_frame()
        self.prompt_frame = ttk.Frame(master=self.options_frame)
        self.config_prompt_frame()
        self.button_frame = ttk.Frame(master=self.options_frame)
        self.config_button_frame()

        self.term_frame = ttk.Frame(master=self.window)
        self.defintion_frame = ttk.Frame(master=self.window)
        self.image_frame = ttk.Frame(master=self.defintion_frame)
        self.end_frame = ttk.Frame(master=self.window)

        self.card_listbox = tk.Listbox(master=self.card_select_frame, exportselection=False)


        self.transition = False
        self.options_frame_up = False
        self.term_frame_up = False
        self.defintion_frame_up = False

    def set_grid(self):
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

    def set_geometry(self):
        window_width, window_height = spec.get_large_window_geometry()
        self.window.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}")
    
#### frames ####

    def config_options_frame(self):
        self.options_frame.grid(row=0, column=0, sticky="nwse")
        self.options_frame.columnconfigure((0,1), weight = 1)
        self.options_frame.rowconfigure(0, weight=7)
        self.options_frame.rowconfigure(1, weight=1)
        self.options_frame.tkraise()

        self.options_frame_up = True

    def config_end_frame(self):
        self.end_frame.grid(row=0, column=0, sticky="nwse")
        self.end_frame.columnconfigure(0, weight = 1)
        self.end_frame.rowconfigure(0, weight=1)
        self.end_frame.tkraise()
        end_message = ttk.Label(master=self.end_frame, 
                                text="Session Complete!", 
                                font=self.font)
        end_message.grid(row=0, column=0)

    def config_term_frame(self):
        self.term_frame.grid(row=0, column=0, sticky="nwse")
        self.term_frame.columnconfigure(0, weight = 1)
        self.term_frame.rowconfigure(0, weight=5)
        self.term_frame.rowconfigure(1, weight=1)
        self.term_frame.tkraise()

        self.term_frame_up = True
        self.options_frame_up = False
        self.defintion_frame_up = False

    def config_defintion_frame(self):
        self.defintion_frame.grid(row=0, column=0, sticky="nwse")
        self.defintion_frame.columnconfigure(0, weight = 1)
        self.defintion_frame.rowconfigure(0, weight=5)
        self.defintion_frame.rowconfigure((1,2), weight=1)
        self.defintion_frame.tkraise()

        self.term_frame_up = False
        self.options_frame_up = False
        self.defintion_frame_up = True

    def config_image_frame(self):
        self.image_frame.grid(row=0, column=0, sticky="nwse")
        self.image_frame.columnconfigure(0, weight = 1)
        self.image_frame.rowconfigure(0, weight=1)
        self.image_frame.grid_propagate(False)

    def config_card_select_frame(self):
        self.card_select_frame.grid(row=0, column=0, sticky="nwse", padx=self.x_buffer)
        self.card_select_frame.columnconfigure(0, weight=1)
        self.card_select_frame.rowconfigure(0, weight=1)
        self.card_select_frame.grid_propagate(False)
        
    def config_prompt_frame(self):
        self.prompt_frame.grid(row=0, column=1, sticky="nwse", padx=self.x_buffer)
        self.prompt_frame.columnconfigure(0, weight=1)
        self.prompt_frame.rowconfigure(0, weight=1)
        self.prompt_frame.grid_propagate(False) 

    def config_button_frame(self):
        self.button_frame.grid(row=1, column=0, sticky="nwse", padx=self.x_buffer, columnspan=2)
        self.button_frame.columnconfigure((0,1), weight=1)
        self.button_frame.rowconfigure(0, weight=1)
        self.button_frame.grid_propagate(False) 
    
#### widgets ####

    def display_card_select_listbox(self):
        cards = rd.get_card_names(self.deck)
        listbox_variable = tk.Variable(value=cards)
        self.card_listbox.config(listvariable=listbox_variable)
        self.card_listbox.config(selectmode=tk.MULTIPLE) ####
        self.card_listbox.config(height=12)
        self.card_listbox.grid(row=0, column=0, sticky="nswe")
    
    def display_card_select_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self.card_select_frame, orient=tk.VERTICAL, command=self.card_listbox.yview)
        self.card_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=0, column=0, sticky="nse")

    def display_prompt(self):
        prompt = ttk.Label(master = self.prompt_frame, 
                           text="Select Cards To Study Or Press Select All to Study all Cards",
                           font=self.font)
        prompt.grid(row=0, column=0)

    def display_buttons(self):
        select_all = ttk.Button(master=self.button_frame, text="Select All")
        select_all.grid(row=0, column=0, sticky="e")
        select_all.bind("<Button>", self.select_all)

        confirm_selection = ttk.Button(master=self.button_frame, text="Ok")
        confirm_selection.grid(row=0, column=1, sticky="e")
        confirm_selection.bind("<Button>", self.get_cards)


#### functionality ####

    def select_all(self, event): # W
        if (self.all_selected == False):
            self.card_listbox.selection_set(0, tk.END)
            self.all_selected = True
        else:
            self.card_listbox.select_clear(0, tk.END)
            self.all_selected = False

    def get_cards(self, event):
        cards = self.card_listbox.curselection()
        if (len(cards) != 0):
            for card in cards:
                self.cards.append(self.card_listbox.get(card))
            self.shuffle_cards(self.cards)
            self.config_term_frame()
            self.display_card_term()
        

    def display_card_term(self):
        term_label = ttk.Label(master=self.term_frame, 
                               text=self.cards[self.card_index],
                               font=self.font)
        term_label.grid(row=0, column=0)
        self.check_for_transition()

    def display_card_defintion(self):
        term, definiton, image_file = rd.get_card_details(deck=self.deck, card=self.cards[self.card_index])
        card_shown = False
        if (image_file != None): # there is an image to displays
            self.config_image_frame()
            row_width = self.image_frame.winfo_width() 
            column_width = self.image_frame.winfo_height() 
            if (row_width <= 1 and column_width <= 1): # ensure image frame has time to configure
                self.window.after(10, self.display_card_defintion)
            else: # image frame has configured 
                image_width, image_height = spec.get_resize_image_geometry(image_file, row_width, column_width)
                image = Image.open(image_file)
                image = image.resize((image_width, image_height))
                self.image = ImageTk.PhotoImage(image)
                self.image_label = ttk.Label(master=self.image_frame, 
                                                image=self.image)
                self.image_label.grid(row=0, column=0)
                self.current_image_file = image_file # update current image       

                defintion_label = ttk.Label(master=self.defintion_frame,
                                            text=definiton,
                                            font=self.font)
                defintion_label.grid(row=1, column=0)
                prompt_label = ttk.Label(master=self.defintion_frame,
                                            text="Press Space to Continue",
                                            font=self.font)
                prompt_label.grid(row=2, column=0)
                
                card_shown = True
                
        else: # no image to display
            defintion_label = ttk.Label(master=self.defintion_frame,
                                            text=definiton,
                                            font=self.font)
            defintion_label.grid(row=0, column=0)
            prompt_label = ttk.Label(master=self.defintion_frame,
                                            text="Press Space to Continue",
                                            font=self.font)
            prompt_label.grid(row=2, column=0)
            
            card_shown = True
        
        if (card_shown):
            self.card_index += 1
            self.check_for_transition()


    def check_for_transition(self):
        if (self.term_frame_up == True and self.transition == True):
            self.transition = False
        
            self.config_defintion_frame()
            self.display_card_defintion()
            self.clear_frame(self.term_frame)


        elif (self.defintion_frame_up == True and self.transition == True):
            self.transition = False
        
            if (self.card_index != len(self.cards)):
                self.config_term_frame()
                self.display_card_term()
                self.clear_frame(self.defintion_frame)
            else:
                self.config_end_frame()
        else:
            self.window.after(100, self.check_for_transition)
           

    def on_space_bar(self, event):
        if (self.term_frame_up == True):
            self.transition = True
        elif (self.defintion_frame_up == True):
            self.transition = True

#### Helper ####

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.grid_remove()
        
    def shuffle_cards(self, cards: tuple) -> list[str]:
        return random.shuffle(cards)