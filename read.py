
import os


class Reader:

    def __init__(self):
        pass


    @staticmethod
    def check_main_card_folder_exist() -> bool:
        filepath = os.getcwd() # get current working directory
        try:
            f = open(filepath + "\\cards") # (\\) only works for certain os? May need to change 
            return True # main card folder exist
        except:
            return False # main card folder does not exist

    @staticmethod
    def read_all_folders():
        pass

    @staticmethod
    def read_sub_folder():
        with open("test.txt", "r") as fp:
            for line in fp:
                print(line)
            fp.close()


