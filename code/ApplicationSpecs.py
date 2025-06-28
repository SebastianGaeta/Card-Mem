import tkinter as tk
from tkinter import ttk 
from PIL import Image


# from tkinter import messagebox
# from write import Writer as wr
# from read import Reader as rd
# from write import Writer as wr


class Specs:
    
    def __init__(self): 
        pass

    # screen dimenion getters 
    @staticmethod
    def get_screen_dimensions(): 
        window = tk.Tk()
        screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
        window.destroy()
        return screen_width, screen_height # return tuple in form (width, height)
    
    @staticmethod
    def get_screen_width():
        window = tk.Tk()
        screen_width = window.winfo_screenwidth()
        window.destroy()
        return screen_width

    @staticmethod
    def get_screen_height():
        window = tk.Tk()
        screen_height = window.winfo_screenheight
        window.destroy()
        return screen_height


    @staticmethod
    def get_centered_window(screen_width, screen_height):
        window_width = screen_width // 2 # window width
        window_height = screen_height // 2 # window height
        center_x = int(screen_width/2 - window_width/2) # x center screen
        center_y = int(screen_height/2 - window_height/2) # y center screen
        return center_x, center_y # returns tuple (width, height)

    @staticmethod
    def get_small_window_geometry():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width // 4, screen_height // 4  # return tuple in form (width, height)

    @staticmethod
    def get_medium_window_geometry():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width // 3, screen_height // 3  # return tuple in form (width, height)
   
    @staticmethod
    def get_large_window_geometry():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width // 2, screen_height // 2  # return tuple in form (width, height)
    
    @staticmethod
    def get_std_xy_pad():
        screen_width, screen_height = Specs.get_screen_dimensions()
        return screen_width * 0.007, screen_height * 0.007
    
    def get_std_x_pad():
        screen_width = Specs.get_screen_width()
        return screen_width * 0.007
    
    def get_std_y_pad():
        screen_height = Specs.get_screen_height()
        return screen_height * 0.007

    @staticmethod
    def get_geometry_tuple(width, height):
        return f"{width}x{height}"
    
    @staticmethod
    def get_image_geometry(file):
        screen_width = Specs.get_screen_width()
        max_image_square_dimension = screen_width * 0.175 # assign max image dimensions
        image = Image.open(file) 
        image_width, image_height = image.size
        if (image_width <= max_image_square_dimension and image_height <= max_image_square_dimension):
            return int(image_width), int(image_height) # image was within acceptable dimesions 
        else:
            if (image_width >= image_height): # image width is greater than height or it is a square image
                image_resizer = max_image_square_dimension / image_width 
                image_width *= image_resizer
                image_height *= image_resizer
            else: # image height is greater
                image_resizer = max_image_square_dimension / image_height 
                image_width *= image_resizer
                image_height *= image_resizer
        return int(image_width), int(image_height)