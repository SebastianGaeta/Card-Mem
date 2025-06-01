
from tkinter import messagebox
from pathlib import Path
import shutil

class Writer: 

    def __init__(self):
        pass
    
    @staticmethod
    def create_deck_folder(folder_name: str, window):
        cwd = Path.cwd()
        try: # Attempt to make deck folder
            Path.mkdir(f"{cwd}\\{folder_name}")
            messagebox.showinfo(title="Information", message="Deck Successfully Created")   
            window.destroy()
        except FileExistsError: # Deck folder exist
            if messagebox.askokcancel(title="Information", message="Deck Already Exist! Would you like to overwrite" \
                " and delete deck?"):
                try: # Delete existing deck
                    shutil.rmtree(f"{cwd}\\{folder_name}") # delete folder
                    try: # Create new directory to replace old
                        Path.mkdir(f"{cwd}\\{folder_name}")
                        messagebox.showinfo(title="Information", message="Deck Successfully Created")
                        window.destroy()
                    except: # Error occured in attempting to create new directory
                        messagebox.showinfo(title="Information", message="Failed To Create New Deck")   
                except OSError: # Error occured in attempting to delete existing folder
                    messagebox.showwarning(title="Information", message="Failed To Delete Deck Folder")   
            
                
               
        
        
        
        

