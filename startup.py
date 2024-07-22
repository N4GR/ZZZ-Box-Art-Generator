from generate import generate
from log import logging
import os

def checks():
    if folders() is False: return False
    elif imageListCount() is False: return False
    else: return True

def folders():
    # Generate necessary folders if they don't exist.
    dir_names = ["mods", "images"]
    for dir_name in dir_names:
        if not os.path.isdir(dir_name):
            try:
                generate.directory(name = dir_name)
            except Exception as error:
                print(logging().error(f"Couldn't generate directory: {dir_name}"))
                print(logging().error(error))
                return False
    

    config_name = "config"
    if not os.path.isfile(f"{config_name}.json"):
        try:
            generate.config(file_name = "config")
        except Exception as error:
            print(logging().error(f"Couldn't generate config.json"))
            print(logging().error(error))
            return False
    
    return True

def imageListCount():
    image_count = len(generate.image_list())
    if image_count < 53:
        print(logging().error(f"53 Images required, you only have {image_count}"))
        return False
    return True