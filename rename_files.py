from os import listdir
from os.path import isfile, join

from utilities import app_root

def rename_files():
    app = app_root()
    file_list = listdir(app + '/img')
    print file_list

rename_files()
