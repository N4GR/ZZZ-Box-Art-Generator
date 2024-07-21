from os import path
from json import load

def getLocale(id: str):
    # Obtains relevant locale.
    locale_dir = "localisation"
    if not path.isfile(f"{locale_dir}/{id}.json"):
        print("Locale ID not recognised, defaulting to English.")

        with open(f"{locale_dir}/en.json") as file:
            return load(file)
    else:
        with open(f"{locale_dir}/{id}.json") as file:
            return load(file)