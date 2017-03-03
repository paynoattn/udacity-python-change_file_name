from os import listdir, rename, chdir

from utilities import get_app_root, get_img_dir, change_name

def get_files():
    return listdir(get_img_dir())

def rename_files():
    files = get_files()
    app_root = get_app_root()
    chdir(get_img_dir())
    for file in files:
        print 'renaming file ' + file + ' to ' + change_name(file)
        rename(file, change_name(file))
    chdir(app_root)

rename_files()
