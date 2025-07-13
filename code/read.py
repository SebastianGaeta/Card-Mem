
from pathlib import Path
import os
import shutil
from tkinter import filedialog


class Reader:

    def __init__(self):
        self.parent_deck_directory = Path(f"{Path.cwd().parent}\\decks")

    def check_main_deck_directory_exist(self) -> bool:
        filepath = os.getcwd() # get current working directory
        try:
            f = open(filepath + "\\cards") # (\\) only works for certain os? May need to change 
            return True # main card folder exist
        except:
            return False # main card folder does not exist
        
    @staticmethod
    def get_base_directory():
        return Path(f"{Path.cwd().parent}")

    @staticmethod
    def get_deck_directory():
        return Path(f"{Reader.get_base_directory()}\\decks")
    
    @staticmethod
    def get_deck_card_directory(deck: str, card: str) -> str:
        return Path(f"{Reader.get_base_directory()}\\decks\\{deck}\\{card}")
    
    @staticmethod
    def get_file_name(file):
        return Path(file).name
    
    @staticmethod
    def convert_to_path(filename: str):
        return Path(filename.strip())

    @staticmethod
    def get_deck_names() -> tuple[str]: # WAI
        deck_directory = Path(f"{Reader.get_base_directory()}\\decks")
        deck_names = ()
        for deck in deck_directory.iterdir():
            deck_names += (deck.stem,) # (*,*) need comma to tell python this is a tuple
        return deck_names
    
    @staticmethod
    def get_card_names(deck) -> tuple[str]: # WAI
        deck = Path(f"{Reader.get_base_directory()}\\decks\\{deck}")
        cards = ()
        if (Path.is_dir(deck)):
            for card in deck.iterdir():
                cards += (card.stem,) # (*,*) need comma to tell python this is a tuple
            return cards
        else:
            return cards 


    @staticmethod 
    def get_card_details(deck, card):
        #TODO want to make it so .(extension) is not needed
        card_directory = Path(f"{Reader.get_base_directory()}\\decks\\{deck}\\{card}")
        if (Path.is_dir(card_directory)):
            term = ""
            definition = ""
            image = None
            for file in card_directory.iterdir():
                if file.name == "term.txt":
                    with open(Path(f"{card_directory}\\{file.name}"), "r", encoding="utf-8") as fp: # term
                        for line in fp:
                            term += line  
                if file.name == "definition.txt":
                    with open(Path(f"{card_directory}\\{file.name}"), "r", encoding="utf-8") as fp: # defintion
                        for line in fp:
                            definition += line 
                if file.name.endswith(("jpg", "png")): # image
                    image = file 
            return term, definition, image
        else:
            return None
        
    @staticmethod
    def get_assets_directory():
        return Path(f"{Reader.get_base_directory()}\\assets")

    @staticmethod
    def read_sub_folder():
        with open("test.txt", "r") as fp:
            for line in fp:
                print(line)
            fp.close()

    @staticmethod
    def delete_card(card_directory: str) -> bool:
        if Path.is_dir(card_directory):
            shutil.rmtree(card_directory)
            return True
        else:
            return False
            
    @staticmethod
    def file_popup(window) -> str:
        image_file  = filedialog.askopenfilename(initialdir="C:\\", title="Select Image", 
                                          filetypes=(("PNG", "*.png"), ("JPG", "*.jpg")), 
                                          parent=window)
        return image_file
            # self.display_custom_image(image_file)
            # self.display_remove_image_button()