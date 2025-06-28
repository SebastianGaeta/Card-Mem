
from pathlib import Path
import os



class Reader:

    def __init__(self):
        self.parent_deck_directory = Path(f"{Path.cwd()}\\decks")

    def check_main_deck_directory_exist(self) -> bool:
        filepath = os.getcwd() # get current working directory
        try:
            f = open(filepath + "\\cards") # (\\) only works for certain os? May need to change 
            return True # main card folder exist
        except:
            return False # main card folder does not exist
        
    @staticmethod
    def get_deck_directory():
        return Path(f"{Path.cwd()}\\decks")
    
    @staticmethod
    def get_file_name(file):
        return Path(file).name
    
    @staticmethod
    def convert_to_path(filename):
        return Path(filename)

    def get_deck_names(self) -> tuple[str]: # WAI
        deck_names = ()
        for child_directory in self.parent_deck_directory.iterdir():
            deck_names += (child_directory.stem,) # (*,*) need comma to tell python this is a tuple
        return deck_names

    @staticmethod
    def get_assets_directory():
        return Path(f"{Path.cwd()}\\assets")

    @staticmethod
    def read_sub_folder():
        with open("test.txt", "r") as fp:
            for line in fp:
                print(line)
            fp.close()


