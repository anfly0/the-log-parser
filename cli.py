import os


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
