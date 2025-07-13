import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox
from tkinter import filedialog

from ApplicationSpecs import Specs as spec
from read import Reader as rd
from PIL import ImageTk, Image

class AddCard():
    
    def __init__(self):

        self.x_buffer, self.y_buffer = spec.get_std_xy_pad()       
        self.font = ("Helvetica", 14)
        self.sample_image_file = rd.get_assets_directory().joinpath("CardPreviewSample.jpg")

        self.window = tk.Toplevel() 
        self.set_grid()
        self.set_geometry()

        self.image_frame = ttk.Frame(master=self.window)
        self.config_image_frame() 
        self.deck_frame = ttk.Frame(master=self.window)
        self.config_deck_frame() 
        self.term_frame = ttk.Frame(master=self.window)
        self.config_term_frame() 
        self.definition_frame = ttk.Frame(master=self.window)
        self.config_definition_frame() 
        self.add_remove_image_frame = ttk.Frame(master=self.window)
        self.config_add_remove_image_frame() 
        self.add_button_frame = ttk.Frame(master=self.window)
        self.config_add_button_frame() 
        self.labels_frame = ttk.Frame(master=self.window)
        self.config_labels_frame() 
        
        
        self.deck_listbox = tk.Listbox(master=self.deck_frame, exportselection=False)
        self.term_textbox = tk.Text(master=self.term_frame)
        self.definition_textbox = tk.Text(master=self.definition_frame)
        self.remove_image_button = ttk.Button(master=self.add_remove_image_frame)
        self.current_image = None
        self.current_image_file = None
        
      


    def set_grid(self):
        self.window.columnconfigure(0, weight = 2)
        self.window.columnconfigure(1, weight = 1)
        self.window.columnconfigure(2, weight = 2)
        self.window.rowconfigure((0,1,2,3), weight = 1)
    
    def set_geometry(self):
        window_width, window_height = spec.get_screen_dimensions()
        self.window.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}")
        
#### frames
    
    def config_deck_frame(self):
        self.deck_frame.grid(row=0, column=0, sticky="nwse", padx=self.x_buffer, pady=self.y_buffer * 2)
        self.deck_frame.columnconfigure(0, weight=1)
        self.deck_frame.rowconfigure(0, weight=1)
        self.deck_frame.grid_propagate(False)

    def config_term_frame(self):
        self.term_frame.grid(row=1, column=0, sticky="nwse", padx=self.x_buffer, pady=self.y_buffer * 2)
        self.term_frame.columnconfigure(0, weight=1)
        self.term_frame.rowconfigure(0, weight=1)
        self.term_frame.grid_propagate(False)
    
    def config_definition_frame(self):
        self.definition_frame.grid(row=2, column=0, sticky="nwse", padx=self.x_buffer, pady=self.y_buffer * 2)
        self.definition_frame.columnconfigure(0, weight=1)
        self.definition_frame.rowconfigure(0, weight=1)
        self.definition_frame.grid_propagate(False)

    def config_add_remove_image_frame(self):
        self.add_remove_image_frame.grid(row=3, column=0, sticky="nwse", padx=self.x_buffer, pady=self.y_buffer * 2)
        self.add_remove_image_frame.columnconfigure((0,1,2,3), weight=1)
        self.add_remove_image_frame.rowconfigure(0, weight=1)
        self.add_remove_image_frame.grid_propagate(False)
    
    def config_add_button_frame(self):
        self.add_button_frame.grid(row=3, column=2, sticky="nwse", padx=self.x_buffer, pady=self.y_buffer * 2)
        self.add_button_frame.columnconfigure((0,1,2,3), weight=1)
        self.add_button_frame.rowconfigure(0, weight=1)
        self.add_button_frame.grid_propagate(False)

    def config_labels_frame(self):
        self.labels_frame.grid(row=0, column=1, sticky="nwse", padx=self.x_buffer, pady=self.y_buffer * 2,
                                         rowspan=4)
        self.labels_frame.columnconfigure(0, weight=1)
        self.labels_frame.rowconfigure((0,1,2,3), weight=1)
        self.labels_frame.grid_propagate(False)

    def config_image_frame(self):
        self.image_frame.grid(row=0, column=2, sticky="nwse", rowspan=3, padx=self.x_buffer * 4, pady=self.y_buffer)
        self.image_frame.columnconfigure(0, weight=1)
        self.image_frame.rowconfigure(0, weight=1)
        self.image_frame.grid_propagate(False)


####

    def display_labels(self):
        deck_to_add_to_label = ttk.Label(self.labels_frame, text="Deck")
        deck_to_add_to_label.grid(row = 0, column = 0, sticky="w")
        term_label = ttk.Label(self.labels_frame, text="Term")
        term_label.grid(row = 1, column = 0, sticky="w")
        definition_label = ttk.Label(self.labels_frame, text="Definition")
        definition_label.grid(row = 2, column = 0, sticky="w")

    def display_sample_image(self):
        self.current_image_file = self.sample_image_file # update current image file 
        row_width = self.image_frame.winfo_width() 
        column_width = self.image_frame.winfo_height() 
        if (row_width <= 1 and column_width <= 1): # ensure image frame has time to configure
            self.window.after(10, self.display_sample_image)
        else:
            image_width, image_height = spec.get_resize_image_geometry(self.sample_image_file, row_width, column_width)
            sample_image = Image.open(self.sample_image_file)
            sample_image = sample_image.resize((image_width, image_height))
            self.current_image = ImageTk.PhotoImage(sample_image)
            image_label = ttk.Label(master=self.image_frame, 
                                            image=self.current_image)
            image_label.grid(row=0, column=0, sticky="nwse")   

    def display_custom_image(self, image_file): 
        # update current image file
        self.current_image_file = image_file
        row_width = self.image_frame.winfo_width() 
        column_width = self.image_frame.winfo_height() 
        image_width, image_height = spec.get_resize_image_geometry(image_file, row_width, column_width)
        custom_image = Image.open(image_file)
        custom_image = custom_image.resize((image_width, image_height))
        self.current_image = ImageTk.PhotoImage(custom_image)

        image_label = ttk.Label(master=self.image_frame, 
                                        image=self.current_image)
        image_label.grid(row=0, column=0, sticky="nwse")

    def display_deck_listbox(self):
        decks = rd.get_deck_names()
        listbox_variable = tk.Variable(value=decks)
        self.deck_listbox.config(listvariable=listbox_variable)
        self.deck_listbox.config(selectmode=tk.SINGLE)
        self.deck_listbox.config(height=5)
        self.deck_listbox.grid(row=0, column=0, sticky="nwse")

    def display_deck_listbox_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self.deck_frame, orient=tk.VERTICAL, command=self.deck_listbox.yview)
        self.deck_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=0, column=0, sticky="nse")
    
    def display_term_textbox(self):
        self.term_textbox.config(height=5)
        self.term_textbox.grid(row=0, column=0, sticky="nwse")

    def display_definition_textbox(self):
        self.definition_textbox.config(height=5)
        self.definition_textbox.grid(row=0, column=0, sticky="nwse")   

    def display_add_image_button(self):
        add_image_button = ttk.Button(master=self.add_remove_image_frame, text="Add Image")
        add_image_button.grid(row=0, column=3, sticky="ne")
        add_image_button.bind("<Button>", self.get_image_file)

    def display_remove_image_button(self):
        self.remove_image_button.config(text="Remove Image")
        self.remove_image_button.grid(row=0, column=3, sticky="n")
        self.remove_image_button.bind("<Button>", self.hide_remove_image_button)

    def hide_remove_image_button(self, event):
        self.display_sample_image()
        self.remove_image_button.grid_forget()


    def get_image_file(self, event):
        image_file = rd.file_popup(self.window)

        if image_file: # valid file
            self.display_custom_image(image_file)
            self.display_remove_image_button()

    def display_add_card_button(self):
        add_card = ttk.Button(master=self.add_button_frame, text="Add card")
        add_card.grid(row=0, column=3)
        add_card.bind("<Button>", self.add_card)

    def add_card(self, event):
        try: # determine deck to save card to
            deck = rd.convert_to_path(self.deck_listbox.get(self.deck_listbox.curselection()))
            term = self.term_textbox.get("1.0", tk.END)

            if (term != "\n"): # check if valid term was entered
                term = term.strip()
                definition = self.definition_textbox.get("1.0", tk.END).strip()
                deck_directory = rd.get_deck_directory()
                
                if (wr.create_card_folder(f"{deck_directory}\\{deck}", rd.convert_to_path(term[0:9].strip()), self.window)): # create card folder
                    
                    card_directory = rd.convert_to_path(f"{deck_directory}\\{deck}\\{term[0:9]}")

                    if (self.current_image_file != self.sample_image_file): # user selected a custom image
                        try:
                            wr.save_image_to_card_folder(card_directory, self.current_image_file)
                            # image = Image.open(self.current_image_file)
                            # image.save(f"{card_directory}\\{rd.get_file_name(self.current_image_file)}")
                        except:
                            messagebox.showerror(title="Image Error",
                                        message="Failed to save image",
                                        parent=self.window)
                    
                    wr.create_card(card_directory, term, definition) 

                    self.window.destroy()

            else: # No term provided
                messagebox.showinfo(title="Invalid Term",
                                message="Please Enter a Term for the Card",
                                parent=self.window)
        except: # user failed to specify deck
            messagebox.showinfo(title="Invalid Deck",
                                message="Select a Deck to Save Card to",
                                parent=self.window)
            