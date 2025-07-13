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
    def get_resize_image_geometry(image_file, width, height):
        
        image = Image.open(image_file) 
        image_width, image_height = image.size
        image_resizer = None
        # print(width, height, "accepted")
        # print(image_width, image_height, "actual")
        if (image_width <= width and image_height <= height): # image was within acceptable dimensions 
            return int(image_width), int(image_height) 
        else:
            if (image_width > width and image_height > height): # image width and height are greater then accepted
                if (width < height): # width was greater
                    image_ratio = image_height / image_width
                    image_resizer = width / image_width
                    image_width *= image_resizer
                    image_height =  image_width * image_ratio
                elif (height <= width): # height was greater or potential square image
                    image_ratio = image_width / image_height
                    image_resizer = height / image_height
                    image_height *= image_resizer
                    image_width = image_height * image_ratio
                # print(image_width, image_height)
                return int(image_width), int(image_height)
            elif (image_height > height): # image height is greater than allowed height
                image_resizer = height / image_height 
            else: # image width is greater than allowed width
                image_resizer = width / image_width 
        image_width *= image_resizer
        image_height *= image_resizer
        return int(image_width), int(image_height)