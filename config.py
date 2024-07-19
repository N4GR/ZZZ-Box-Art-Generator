import json

class config():
    def __init__(self) -> None:
        with open("config.json") as file:
            self.config = json.load(file)

    def image_directory(self):
        return self.config["images"]
    
    def mods_directory(self):
        return self.config["mods_directory"]
    
    def required_images(self):
        return self.config["required_images"]
    
    def BoxArt1(self):
        return self.config["BoxArt1"]

    def BoxArt2(self):
        return self.config["BoxArt2"]
    
    def BoxArtBigger(self):
        return self.config["BoxArtBigger"]