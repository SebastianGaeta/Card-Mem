import tkinter as tk
from tkinter import ttk 
from write import Writer as wr
from tkinter import messagebox
from tkinter import filedialog

from ApplicationSpecs import Specs as spec
from read import Reader as rd
from PIL import ImageTk, Image

class AddCard():
    #"assets/CardPreviewSample.jpg"
    def __init__(self):
        self.rd = rd() # reader object
        self.window = tk.Toplevel() 
        self.x_pad, self.y_pad = spec.get_std_xy_pad()       
    
        self.term_textbox = tk.Text(master=self.window)
        self.definition_textbox = tk.Text(master=self.window)
        self.deck_listbox = tk.Listbox(master=self.window)
        self.remove_image_button = ttk.Button(master=self.window)
        self.image_file = None
        self.image = None
        self.preview_image_filename = "CardPreviewSample.jpg"
        self.preview_image_filepath = rd.get_assets_directory().joinpath(rd.convert_to_path(self.preview_image_filename))


    def set_grid(self):
        self.window.columnconfigure((0,1,2), weight = 1)
        self.window.rowconfigure((0,1,2,3), weight = 1)
    
    def set_geometry(self):
        window_width, window_height = spec.get_screen_dimensions()
        self.window.geometry(f"{spec.get_geometry_tuple(window_width, window_height)}")
        
    def display_labels(self):
        deck_to_add_to_label = ttk.Label(self.window, text="Deck", font=("Helvetica", 14))
        deck_to_add_to_label.grid(row = 0, column = 1, sticky="w")
        term_label = ttk.Label(self.window, text="Term", font=("Helvetica", 14))
        term_label.grid(row = 1, column = 1, sticky="w")
        definition_label = ttk.Label(self.window, text="Definition", font=("Helvetica", 14))
        definition_label.grid(row = 2, column = 1, sticky="w")
        img_label = ttk.Label(self.window, text="Image", font=("Helvetica", 14))
        img_label.grid(row = 3, column = 1, sticky="nw")
        # img_preview_label = ttk.Label(self.window, text="Image preview",font=("Helvetica", 14))
        # img_preview_label.grid(row=2, column=2)


    def display_sample_image(self):
        self.image_file = self.preview_image_filepath
        self.resize_image()

        image_width, image_height = spec.get_image_geometry(self.preview_image_filepath)
        image_frame = tk.Frame(self.window, width = image_width + image_width * 0.1, height=image_height + image_height * 0.1)
        image_frame.grid(row=1, column=2, sticky="w")
        image_frame.grid_propagate(False)

        image_label = ttk.Label(image_frame, 
                                image=self.image, 
                                text="Image preview", compound=tk.TOP,
                                font=("Helvetica", 14))
        image_label.grid(sticky="nwse")


    def display_custom_image(self): 
        self.resize_image()
        
        image_width, image_height = spec.get_image_geometry(self.preview_image_filepath)
        image_frame = tk.Frame(self.window, width = image_width + image_width * 0.1, height=image_height + image_height * 0.1)
        image_frame.grid(row=1, column=2, sticky="w")
        image_frame.grid_propagate(False)

        image_label = ttk.Label(image_frame, 
                                image=self.image, 
                                text="Image preview", compound=tk.TOP,
                                font=("Helvetica", 14))
        image_label.grid(sticky="nwse")

    def resize_image(self):
        image_width, image_height = spec.get_image_geometry(self.image_file)
        image = Image.open(self.image_file)
        image = image.resize((image_width, image_height))
        self.image = ImageTk.PhotoImage(image)

    def display_deck_listbox(self):
        decks = self.rd.get_deck_names()
        listbox_variable = tk.Variable(value=decks)
        self.deck_listbox.config(listvariable=listbox_variable)
        self.deck_listbox.config(selectmode=tk.SINGLE)
        self.deck_listbox.config(height=3)
        self.deck_listbox.grid(row=0, column=0,sticky="we", padx=self.x_pad)

    def display_deck_listbox_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.deck_listbox.yview)
        self.deck_listbox["yscrollcommand"] = vertical_scrollbar.set
        vertical_scrollbar.grid(row=0, column=0, sticky="e")
    
    def display_term_textbox(self):
        self.term_textbox.config(height=5)
        self.term_textbox.grid(row=1, column=0, sticky="we", padx=self.x_pad)

    def display_definition_textbox(self):
        self.definition_textbox.config(height=5)
        self.definition_textbox.grid(row=2, column=0, sticky="we", padx=self.x_pad)

    def display_add_image_button(self):
        add_image_button = ttk.Button(self.window, text="Add", command=self.file_popup)
        add_image_button.grid(row=3, column=0, sticky="ne", padx=self.x_pad)

    def display_remove_image_button(self):
        self.remove_image_button.config(text="Remove",command=self.hide_remove_image_button)
        self.remove_image_button.grid(row=3, column=0, sticky="e", padx=self.x_pad)

    def hide_remove_image_button(self):
        self.display_sample_image()
        self.remove_image_button.grid_forget()

    def file_popup(self):
        temp_image_file  = filedialog.askopenfilename(initialdir="C:\\", title="Select file", 
                                          filetypes=(("PNG", "*.png"), ("JPG", "*.jpg")), 
                                          parent=self.window)
        if temp_image_file: # valid file
            self.image_file = temp_image_file
            self.display_custom_image()
            self.display_remove_image_button()

    def display_add_card_button(self):
        add_card = ttk.Button(master=self.window, text="Add card")
        add_card.grid(row=3, column=2, ipadx=self.x_pad, ipady=self.y_pad)
        add_card.bind("<Button>", self.add_card)

    def add_card(self, event):
        try: # determine deck to save card to
            deck_to_save_to = rd.convert_to_path(self.deck_listbox.get(self.deck_listbox.curselection()))
            term = self.term_textbox.get("1.0", tk.END).strip()

            if (term != "\n"): # check if valid term was entered
                definition = self.definition_textbox.get("1.0", tk.END).strip()
                deck_directory = rd.get_deck_directory()
                if (wr.create_card_folder(f"{deck_directory}\\{deck_to_save_to}", rd.convert_to_path(term[0:9]), self.window)): # create card folder
        
                    card_directory = f"{deck_directory}\\{deck_to_save_to}\\{rd.convert_to_path(term[0:9])}"
                    
                    if (self.image_file != self.preview_image_filepath): # user selected a custom image
                        try:
                            image = Image.open(self.image_file)
                            image.save(f"{card_directory}\\{rd.get_file_name(self.image_file)}")
                        except:
                            messagebox.showerror(title="Image Error",
                                        message="Failed to save image",
                                        parent=self.window)
                    with open(f"{card_directory}\\term.txt", "w", encoding="utf-8") as fp:
                        for line in term:
                            fp.write(line)
                    with open(f"{card_directory}\\definition.txt","w", encoding="utf-8") as fp:
                        for line in definition:
                            fp.write(line)
                            
                    self.window.destroy()

            else: # No term provided
                messagebox.showinfo(title="Invalid Term",
                                message="Please Enter a Term for the Card",
                                parent=self.window)
        except: # user failed to specify deck
            messagebox.showinfo(title="Invalid Deck",
                                message="Select a Deck to Save Card to",
                                parent=self.window)
            