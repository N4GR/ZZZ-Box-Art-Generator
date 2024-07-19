from generate import generate
import os
import json

def startChecks():
    # Mods Folder
    dir_names = ["mods", "images"]
    for dir_name in dir_names:
        if not os.path.isdir(dir_name): generate.directory(name = dir_name)

def getLocale(id: str):
    locale_dir = "localisation"
    if not os.path.isfile(f"{locale_dir}/{id}.json"):
        print("Locale ID not recognised, defaulting to English.")

        with open(f"{locale_dir}/en.json") as file:
            return json.load(file)
    else:
        with open(f"{locale_dir}/{id}.json") as file:
            return json.load(file)
    
startChecks()