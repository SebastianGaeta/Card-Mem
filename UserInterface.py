import tkinter as tk
from tkinter import ttk 


class UserInterface:
    
    def __init__(self): 
        self.root = tk.Tk() # create root
        self.set_root_title() # set root title
        self.set_root_geometry()
        self.display_home_text()
        self.display_home_options_frame()
        self.root.mainloop()

    
    def get_screen_dimensions(self): 
        return self.root.winfo_screenwidth(), self.root.winfo_screenheight() # return tuple in form (width, height)

    def sub_window_geometry(self):
        screen_width, screen_height = self.get_screen_dimensions()
        return screen_width // 4, screen_height // 4  # return tuple in form (width, height)
        
    def set_root_title(self): 
        self.root.title("Card memory game")

    def set_root_geometry(self):
        screen_width, screen_height = self.get_screen_dimensions()
        window_width = screen_width // 2 # window width
        window_height = screen_height // 2 # window height
        center_x = int(screen_width/2 - window_width/2) # x center screen
        center_y = int(screen_height/2 - window_height/2) # y center screen
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}") # set root geometry

    def display_home_text(self):
        message = ttk.Label(self.root)
        message.config(text="Card Memory game")
        message.config(font=("Arial", 18))
        message.pack()
    
    def display_home_options_frame(self):
        frame = ttk.Frame(self.root)
        frame.config(relief="solid")
        frame.pack(side="left")
        self.display_home_add_card_option(frame)
        
    def display_home_add_card_option(self, frame):
        add_button_card = ttk.Button(frame)
        add_button_card.config(text="Add Card")
        add_button_card.pack(padx=50, pady=50) # padding will look different for different resolutions 
        add_button_card.bind("<Button>", self.display_add_card_window)

    def display_add_card_window(self, event):
        sub_window_width, sub_window_height = self.sub_window_geometry()
        add_card_window = tk.Toplevel()
        add_card_window.geometry(f"{sub_window_width}x{sub_window_height}")
        entry_box = ttk.Entry(add_card_window)
        entry_box.pack()
