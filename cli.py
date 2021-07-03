import os
import sys


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


def text_color(color):
    print(color, end='')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def file_from_arg():
    file_name = sys.argv[1]
    if os.path.isfile(file_name):
        return open(file_name, "r")
    raise SystemExit(f"Usage: {sys.argv[0]} <path to log file>")
