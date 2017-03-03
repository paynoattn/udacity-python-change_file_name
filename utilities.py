from os import path

def app_root():
    return path.dirname(path.realpath(__file__))
