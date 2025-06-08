
from tkinter import messagebox
from pathlib import Path
import shutil

class Writer: 

    def __init__(self):
        self.parent_deck_directory = Path(f"{Path.cwd()}\\decks") 
        # self.parent_deck_directory = Path(f"{Path.cwd().parent}\\decks") # I dont know why but vs doesnt realize we are in /code
        print(self.parent_deck_directory)

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
                messagebox.showinfo(title="Information", message="Deck Successfully Created")   
                window.destroy()
            except FileExistsError: # Deck folder exist
                if messagebox.askokcancel(title="Information", message="Deck Already Exist! Would you like to overwrite" \
                    " and delete deck?"):
                    try: # Delete existing deck
                        shutil.rmtree(f"{child_deck_directory}") # delete folder
                        try: # Create new directory to replace old
                            Path.mkdir(f"{child_deck_directory}")
                            messagebox.showinfo(title="Information", message="Deck Successfully Created")
                            window.destroy()
                        except: # Error occured in attempting to create new directory
                            messagebox.showinfo(title="Information", message="Failed To Create New Deck")   
                    except OSError: # Error occured in attempting to delete existing folder
                        messagebox.showwarning(title="Information", message="Failed To Delete Deck Folder")   
        else: # only runs if failed to make parent directory
            messagebox.showerror("Failed To Make Deck Directory")
                
               
        
        
        
        

