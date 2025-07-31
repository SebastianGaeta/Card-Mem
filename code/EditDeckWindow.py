import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox


from ApplicationSpecs import Specs as spec
from read import Reader as rd
from PIL import ImageTk, Image

class EditDeck():
    
    def __init__(self):
        self.window = tk.Toplevel() 
        self.x_buffer, self.y_buffer = spec.get_std_xy_pad()    
        self.current_card = None # keep track of selected deck
        self.current_deck = None # keep track of selected card
        self.current_image_file = None
        self.image_label = ttk.Label() 
        self.image = None
        
        self.font = ("Arial", 14)

        self.deck_frame = ttk.Frame(master=self.window)
        self.config_deck_frame()
        self.card_frame = ttk.Frame(master=self.window)
        self.config_card_frame()         
        self.card_term_frame = ttk.Frame(master=self.window)
        self.config_card_term_frame()
        self.card_defintion_frame = ttk.Frame(master=self.window)
        self.config_card_defintion_frame()
        self.button_frame = ttk.Frame(master=self.window)
        self.card_details_frame = ttk.Frame(master=self.window)
        self.image_frame = ttk.Frame(master=self.window)
        self.deck_to_save_to_frame = ttk.Frame(master=self.window)

        self.config_image_frame() # enable image frame
        self.config_card_details_frame() # enable details frame
        self.config_deck_to_save_to_frame() # enable deck to save to frame
        
        self.deck_listbox = tk.Listbox(master=self.deck_frame, exportselection=False) # export selection keeps widget focused
        self.card_listbox = tk.Listbox(master=self.card_frame, exportselection=False)
        self.deck_to_save_to_listbox = tk.Listbox(master=self.deck_to_save_to_frame, exportselection=False)
        self.deck_to_save_to_scrollbar = ttk.Scrollbar(self.deck_to_save_to_frame)
        self.card_term_textbox = tk.Text(master=self.card_term_frame)
        self.card_defintion_textbox = tk.Text(master=self.card_defintion_frame)

    def check_selections(self):
        try: # user has selected a deck 
            deck = self.deck_listbox.get(self.deck_listbox.curselection())
            self.window.after(100, lambda: self.display_card_listbox(deck))
            try: # user has selected a card 
                card = self.card_listbox.get(self.card_listbox.curselection())
                # self.window.after(100, lambda: self.display_card_info(deck, card))
                if (self.current_card != card or self.current_deck != deck): 
                    #check if a new card / first card has been selected
                    self.display_card_info(deck, card)
            except: # user has not selected a card 
                self.deck_to_save_to_listbox.grid_remove()
                self.deck_to_save_to_scrollbar.grid_remove()
                self.card_term_textbox.grid_remove()
                self.card_defintion_textbox.grid_remove()
                self.image_label.grid_remove()
                self.button_frame.grid_remove()
               

        except: # user has not selected a deck 
            self.window.after(100, lambda: self.display_card_listbox())
    
    def display_card_info(self, deck: str, card: str):
        
        self.display_deck_to_save_to_listbox() # enable widget
        self.display_deck_to_save_to_scrollbar() # enable widget
        self.config_button_frame() # enable buttons frame
        self.display_buttons() # enable widgets
        
        term, definition, image_file = rd.get_card_details(deck, card)
        self.display_card_term_textbox(term, card) # enable widget
        self.display_card_defintion_textbox(definition, card) # enable widget
       
        if (image_file != None): 
            # there is (an) image to display
            self.display_card_image(image_file)
        else:
            if (self.current_image_file != None):
                # an image has already been displayed, but user has selected a new card without image
                self.image_label.grid_forget()
                self.current_image_file = None

        self.current_card = card
        self.current_deck = deck


    def set_grid(self):
        self.window.columnconfigure((0,1,3), weight = 5) 
        self.window.columnconfigure(2, weight=1) # make label column smaller
        self.window.rowconfigure((0,1,2,3,4,5,6,7), weight = 1)

    def set_root_geometry(self):
        window_width, window_height = spec.get_screen_dimensions()
        self.window.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}")
    

#################################### Frames #######################################

    def config_deck_frame(self):
        self.deck_frame.grid(row=1, column=0, sticky="nwse", padx=self.x_buffer, rowspan=2)
        self.deck_frame.columnconfigure(0, weight=1)
        self.deck_frame.rowconfigure(0, weight=1)
        self.deck_frame.grid_propagate(False)

    def config_card_frame(self):
        self.card_frame.grid(row=4, column=0, sticky="nwse", padx=self.x_buffer, rowspan=3)
        self.card_frame.columnconfigure(0, weight=1)
        self.card_frame.rowconfigure(0, weight=1)
        self.card_frame.grid_propagate(False)

    def config_deck_to_save_to_frame(self):
        self.deck_to_save_to_frame.grid(row=1, column=1, sticky="nwse", padx=self.x_buffer)
        self.deck_to_save_to_frame.columnconfigure(0, weight=1)
        self.deck_to_save_to_frame.rowconfigure(0, weight=1)
        self.deck_to_save_to_frame.grid_propagate(False)

    def config_card_term_frame(self):
        self.card_term_frame.grid(row=3, column=1, sticky="nwse", padx=self.x_buffer)
        self.card_term_frame.columnconfigure(0, weight=1)
        self.card_term_frame.rowconfigure(0, weight=1)
        self.card_term_frame.grid_propagate(False)

    def config_card_defintion_frame(self):
        self.card_defintion_frame.grid(row=5, column=1, sticky="nwse", padx=self.x_buffer)
        self.card_defintion_frame.columnconfigure(0, weight=1)
        self.card_defintion_frame.rowconfigure(0, weight=1)
        self.card_defintion_frame.grid_propagate(False)
    
    def config_button_frame(self):
        self.button_frame.grid(row=7, column=2, sticky="nwse", padx=self.x_buffer, columnspan=2)
        self.button_frame.columnconfigure((0,1,2,3), weight=1)
        self.button_frame.rowconfigure(0, weight=1)
        self.button_frame.grid_propagate(False)

    def config_card_details_frame(self):
        self.card_details_frame.grid(row=1, column=2, sticky="nwse", rowspan=5, padx=self.x_buffer)
        self.card_details_frame.rowconfigure((0,1,2,3,4), weight=1)
        self.card_details_frame.columnconfigure(0, weight=1)
        self.card_details_frame.grid_propagate(False)

    def config_image_frame(self):
        self.image_frame.grid(row=1, column=3, rowspan=5, sticky="nwse", padx=self.x_buffer*3)
        self.image_frame.rowconfigure(0, weight=1)
        self.image_frame.columnconfigure(0, weight=1)
        self.image_frame.grid_propagate(False)

###################################################################################

    def display_card_detail_labels(self):
        deck_to_save_to = ttk.Label(master=self.card_details_frame, text="Deck to Save to", font=self.font)
        deck_to_save_to.grid(row=0, column=0, sticky="w")   
        term = ttk.Label(master=self.card_details_frame, text="Term", font=self.font)
        term.grid(row=2, column=0, sticky="w")   
        definition = ttk.Label(master=self.card_details_frame, text="Defintion", font=self.font)
        definition.grid(row=4, column=0, sticky="w")   

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

    def display_card_listbox(self, deck="Default"):
        cards = rd.get_card_names(deck)
        listbox_variable = tk.Variable(value=cards)
        self.card_listbox.config(listvariable=listbox_variable)
        self.card_listbox.config(selectmode=tk.SINGLE)
        self.card_listbox.config(height=12)
        self.card_listbox.grid(row=0, column=0, sticky="nswe")
        self.check_selections() # update current deck

    def display_card_listbox_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self.card_frame, orient=tk.VERTICAL, command=self.card_listbox.yview)
        self.card_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=0, column=0, sticky="nse")

####
    def display_deck_to_save_to_listbox(self):
        decks = rd.get_deck_names()
        listbox_variable = tk.Variable(value=decks)
        self.deck_to_save_to_listbox.config(listvariable=listbox_variable)
        self.deck_to_save_to_listbox.config(selectmode=tk.SINGLE)
        self.deck_to_save_to_listbox.config(height=12)
        self.deck_to_save_to_listbox.grid(row=0, column=0, sticky="nswe")
        
    def display_deck_to_save_to_scrollbar(self):
        self.deck_to_save_to_scrollbar.config(orient=tk.VERTICAL, 
                                              command=self.deck_listbox.yview)
        self.deck_listbox["yscrollcommand"] = self.deck_to_save_to_scrollbar.set
        self.deck_to_save_to_scrollbar.grid(row=0, column=0, sticky="nse")
#### 
    def display_card_term_textbox(self, term, card):
        self.card_term_textbox.config(height=6)
        self.card_term_textbox.grid(row=0, column=0, sticky="nwse")
        if (self.current_card != card): # display card details only once or if different card has been selected
            self.card_term_textbox.delete(index1="1.0", index2="end")
            self.card_term_textbox.insert(index="1.0", chars=term)
#### 
    def display_card_defintion_textbox(self, defintion, card):
        self.card_defintion_textbox.config(height=6)
        self.card_defintion_textbox.grid(row=0, column=0, sticky="nwse")
        if (self.current_card != card): # display card details only once or if different card has been selected
            self.card_defintion_textbox.delete(index1="1.0", index2="end")
            self.card_defintion_textbox.insert(index="1.0", chars=defintion)
####
    def display_card_image(self, image_file):
        row_width = self.image_frame.winfo_width() 
        column_width = self.image_frame.winfo_height() 
        image_width, image_height = spec.get_resize_image_geometry(image_file, row_width, column_width)
        image = Image.open(image_file)
        image = image.resize((image_width, image_height))
        self.image = ImageTk.PhotoImage(image)
        self.image_label = ttk.Label(self.image_frame, 
                                        image=self.image)
        self.image_label.grid(row=0, column=0, sticky="nwse")
        self.current_image_file = image_file # update current image
####
    def display_buttons(self):
        remove_image = ttk.Button(master=self.button_frame, text="Remove Image")
        remove_image.grid(row=0, column=0)    
        remove_image.bind("<Button>", self.remove_image)
        add_image = ttk.Button(master=self.button_frame, text="Add Image")  
        add_image.grid(row=0, column=1)    
        add_image.bind("<Button>", self.add_image)
        delete_card = ttk.Button(master=self.button_frame, text="Delete Card")
        delete_card.grid(row=0, column=2)     
        delete_card.bind("<Button>", self.delete_card)
        # delete_deck = ttk.Button(master=self.button_frame, text="Delete Deck")
        # delete_deck.grid(row=0, column=0)   
        # delete_deck.bind("<Button>", self.delete_deck)
        update_card = ttk.Button(master=self.button_frame, text="Update Card")
        update_card.grid(row=0, column=3)    
        update_card.bind("<Button>", self.update_card)

    def update_card(self, event):
        orig_term, orig_definition, orig_image = rd.get_card_details(self.current_deck, self.current_card)
        current_term = self.card_term_textbox.get("1.0", tk.END)
        
        if (current_term != "\n"): 
            card_directory = rd.convert_to_path(f"{rd.get_deck_directory()}\\{self.current_deck}\\{self.current_card}")
            current_term = current_term.strip()
            current_definition = self.card_defintion_textbox.get("1.0", tk.END).strip()
            current_image = self.current_image_file
            if (current_definition != orig_definition):
                wr.update_definition(card_directory, current_definition)
            if (current_image != orig_image):
                wr.update_image(card_directory, current_image)
            if (current_term != orig_term):
                wr.update_term(card_directory, current_term)
                wr.rename_card_folder(card_directory, current_term)
        else:
            messagebox.showinfo(title="Invalid Term",
                                message="Please Enter a Term for the Card",
                                parent=self.window)
        


    def add_image(self, event): # WAI BUT LOOK FOR POTENTIAL BUGS
        image_file = rd.file_popup(self.window)
        self.display_card_image(image_file)

    def remove_image(self, event): # WAI
        self.image_label.grid_remove()
        self.current_image_file = None

    def delete_card(self, event): # WAI
        card_directory = rd.get_deck_card_directory(self.current_deck, self.current_card)
        if (rd.delete_card(card_directory)):
            messagebox.showinfo(title="Information", 
                                message="Card Successfully Deleted",
                                parent=self.window)
        else:
            messagebox.showerror(title="Error",
                                message="Card was Unable to be Deleted",
                                parent=self.window)

    # def delete_deck(self, event):
    #     deck_directory = Path(f"{rd.get_deck_directory()}\\{self.current_deck}")
    #     if (rd.delete_deck(deck_directory)):
    #         messagebox.showinfo(title="Information", 
    #                             message="Deck Successfully Deleted",
    #                             parent=self.window)
    #     else:
    #         messagebox.showerror(title="Error",
    #                             message="Deck was Unable to be Deleted",
    #                             parent=self.window)