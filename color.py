import time

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

def printS(text, delay=0.1, color=""):
    for char in text:
        print(f"{color}{char}{Colors.RESET}", end='', flush=True)
        time.sleep(delay)
    print()
