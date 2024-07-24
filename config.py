from json import load

class config():
    def __init__(self) -> None:
        with open("config.json") as file:
            self.config = load(file)
    
    def BoxArt1(self):
        return self.config["BoxArt1"]

    def BoxArt2(self):
        return self.config["BoxArt2"]
    
    def BoxArtBig(self):
        return self.config["BoxArtBig"]

class versioning():
    def __init__(self) -> None:
        with open("version.json") as file:
            self.data = load(file)
    
    def getVersion(self) -> str:
        return self.data["version"]

    def getCreator(self) -> str:
        return self.data["creator"]
    
    def getProfile(self) -> str:
        return self.data["profile"]
    
    def getRepo(self) -> str:
        return self.data["repo"]