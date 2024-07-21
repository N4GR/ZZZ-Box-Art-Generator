from generate import generate
from os import path

def startChecks() -> bool:
    # Generate necessary folders if they don't exist.
    dir_names = ["mods", "images"]
    for dir_name in dir_names:
        if not path.isdir(dir_name): generate.directory(name = dir_name)

    config_name = "config"
    if not path.isfile(f"{config_name}.json"): generate.config(file_name = "config")

    return True