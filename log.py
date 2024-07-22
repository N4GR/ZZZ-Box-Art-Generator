from datetime import datetime

MAGENTA = '\033[35m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_BLUE = '\033[94m'

RESET = '\033[0m'

class logging():
    def __init__(self) -> None:
        now = datetime.now()

        self.time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    def note(self, message: str) -> str:
        return f"{MAGENTA}{self.time}{RESET} |  {BRIGHT_BLUE}STATE{RESET}  | {message}"

    def success(self, message: str) -> str:
        return f"{MAGENTA}{self.time}{RESET} | {BRIGHT_GREEN}SUCCESS{RESET} | {message}"
    
    def error(self, message: str) -> str:
        return f"{MAGENTA}{self.time}{RESET} |  {BRIGHT_RED}ERROR{RESET}  | {message}"