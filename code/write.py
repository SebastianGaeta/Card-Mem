
from tkinter import messagebox
from pathlib import Path
from PIL import ImageTk, Image
import shutil
from read import Reader as rd

class Writer: 

    def __init__(self):
        self.parent_deck_directory = Path(f"{Path.cwd()}\\decks") 
        # self.parent_deck_directory = Path(f"{Path.cwd().parent}\\decks") # I dont know why but vs doesnt realize we are in /code
        

    def create_parent_deck_directory(self) -> bool:
        if (self.parent_deck_directory.is_dir() == True): # parent directory exist
            return True
        else: # parent directory does not exist
            try:
                Path.mkdir(f"{self.parent_deck_directory}")
                return True # Was Parent created successfully?
            except:
                messagebox.showerror("Failed To Make Deck Folder") 
                return False # Was Parent created successfully?

    def create_deck_folder(self, folder_name: str, window):
        parent_directory_exist = self.create_parent_deck_directory()
    
        if (parent_directory_exist):
            child_deck_directory = f"{self.parent_deck_directory}\\{folder_name}" # child directory
            try: # Attempt to make child deck folder
                Path.mkdir(f"{child_deck_directory}")
                messagebox.showinfo(title="Information", 
                                    message="Deck Successfully Created",
                                    parent=window)   
                window.destroy()
            except FileExistsError: # Deck folder exist
                if messagebox.askokcancel(title="Information", 
                                          message="Deck Already Exist! Would you like to overwrite and delete deck?",
                                          parent=window):
                    try: # Delete existing deck
                        shutil.rmtree(f"{child_deck_directory}") # delete folder
                        try: # Create new directory to replace old
                            Path.mkdir(f"{child_deck_directory}")
                            messagebox.showinfo(title="Information", 
                                                message="Deck Successfully Created",
                                                parent=window)
                            window.destroy()
                        except: # Error occured in attempting to create new directory
                            messagebox.showinfo(title="Information", 
                                                message="Failed To Create New Deck",
                                                parent=window)   
                    except OSError: # Error occured in attempting to delete existing folder
                        messagebox.showwarning(title="Information", 
                                               message="Failed To Delete Deck Folder",
                                               parent=window)   
        else: # only runs if failed to make parent directory
            messagebox.showerror(title="Error", 
                                 message="Failed To Make Deck Directory",
                                 parent=window)
            
    @staticmethod
    def create_card_folder(deck_directory, folder_name, window) -> bool:
        card_folder = f"{deck_directory}\\{folder_name}"
        
        try: # Attempt to make child deck folder
            Path.mkdir(f"{card_folder}")  
        except FileExistsError: # card folder exist
            if messagebox.askokcancel(title="Information",
                                      message="Card Already Exist! Would you like to overwrite and delete Card and it's contents?",
                                      parent=window):
                try: # Delete existing card
                    shutil.rmtree(f"{card_folder}") # delete folder
                    try: # Create new directory to replace old
                        Path.mkdir(f"{card_folder}")
                    except: # Error occured in attempting to create new directory
                            messagebox.showinfo(title="Information",
                                                message="Failed To Create New Card",
                                                parent=window)   
                            return False
                except OSError: # Error occured in attempting to delete existing folder
                        messagebox.showwarning(title="Information", 
                                               message="Failed To Delete Card",
                                               parent=window)   
                        return False
            else:
                return False 
            
        return True

    @staticmethod
    def rename_card_folder(card_directory: str, term: str):
        card_directory = Path(card_directory)
        deck = card_directory.parent
        card_directory.rename(Path(f"{deck}\\{term[0:9].strip()}"))
        

    @staticmethod
    def create_card(card_directory: str, term: str, definition: str):
        with open(f"{card_directory}\\term.txt", "w", encoding="utf-8") as fp:
            for line in term:
                fp.write(line)
        with open(f"{card_directory}\\definition.txt","w", encoding="utf-8") as fp:
            for line in definition:
                fp.write(line)
    
    @staticmethod
    def save_image_to_card_folder(card_directory: str, image_file: str):
        image = Image.open(image_file)
        image.save(f"{card_directory}\\{rd.get_file_name(image_file)}")

    @staticmethod
    def update_term(card_directory: str, term):
        with open(f"{card_directory}\\term.txt", "w", encoding="utf-8") as fp:
            for line in term:
                fp.write(line)

    @staticmethod
    def update_definition(card_directory: str, definition: str):
        with open(f"{card_directory}\\definition.txt", "w", encoding="utf-8") as fp:
            for line in definition:
                fp.write(line)

    def update_image(card_directory: str, image_file: str):
        image = None
        for file in card_directory.iterdir():
            if file.name.endswith(("jpg", "png")): # image
                Path.unlink(file)
                break
       
        Writer.save_image_to_card_folder(card_directory, image_file)

    

