from generate import generate
from log import logging
import os
import requests
import time
from json import load

def checks():
    version_check()
    if folders() is False: return False

    image_list = imageListCount()
    if image_list is False: return False
    else: return image_list[1]

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
    image_list = generate.image_list()
    image_count = len(image_list)
    if image_count < 53:
        print(logging().error(f"53 Images required, you only have {image_count}"))
        return False
    return True, image_list

def version_check():
    response = requests.get("https://api.github.com/repos/N4GR/ZZZ-Box-Art-Generator/releases/latest")

    with open("version.json") as file:
        version_data = load(file)

    current_version = version_data["version"]
    newest_version = response.json()["tag_name"]

    if current_version != newest_version:
        print(logging().error(f"Tool out of date... Your version: {current_version}, latest version: {newest_version}"))
        print(logging().note("Continuing..."))
        time.sleep(2)
        return False

    return True