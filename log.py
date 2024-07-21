from datetime import datetime

class logging():
    def __init__(self) -> None:
        now = datetime.now()

        self.time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    def note(self, message: str) -> str:
        return f"{self.time} | NOTE  | {message}"

    def error(self, message: str) -> str:
        return f"{self.time} | ERROR | {message}"