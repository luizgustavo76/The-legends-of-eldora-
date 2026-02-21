import os
import time
ANSI_256 = {
    i: f"\033[38;5;{i}m"
    for i in range(256)
}

ANSI_RESET = "\033[0m"
while True:
    for i in range(256):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ANSI_256[i] + "hello world gamer" + ANSI_RESET)
        time.sleep(0.1)
