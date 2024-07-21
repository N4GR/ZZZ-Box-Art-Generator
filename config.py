from json import load

class config():
    def __init__(self) -> None:
        with open("config.json") as file:
            self.config = load(file)
    
    def BoxArt1(self):
        test = "here"
        return self.config["BoxArt1"]

    def BoxArt2(self):
        return self.config["BoxArt2"]
    
    def BoxArtBigger(self):
        return self.config["BoxArtBigger"]