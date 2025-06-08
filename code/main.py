
# import read as rd -> import a file (module) as allias rd 
from read import Reader as rd # import read (module) from module import Reader (class) as allias rd
from RootWindow import Root as root
from write import Writer as wr
from ApplicationSpecs import Specs as spec



if __name__ == "__main__":
    r = rd()
    main_window = root()
    main_window.run()
    

    if (r.check_main_deck_directory_exist()):
        pass
    else:
        pass