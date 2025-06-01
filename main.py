
# import read as rd -> import a file (module) as allias rd 
from read import Reader as rd # import read (module) from module import Reader (class) as allias rd
from UserInterface import UserInterface as ui





if __name__ == "__main__":
    user_interface = ui()


    if (rd.check_main_card_folder_exist()):
        pass
    else:
        pass