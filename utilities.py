from os import path, getcwd
from string import translate

def get_app_root():
    return getcwd()

def get_img_dir():
    return get_app_root() + '/img'

def change_name(input):
    return translate(input, None, '0123456789')
