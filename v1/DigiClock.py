from colorama import Fore
from random import randint
from time import strftime, sleep
from os import system

ALL_CHAR = '!@#$%^&*()+=}{/?<>QWERTYUIOP{}LKJHGFDSAZXCVBNM'
OUT = [[],[],[],[],[]]
BACKGROUND_COLOR = 'GREEN'
NUMBERS_COLOR = 'LIGHTMAGENTA'

line_true_false = {
    'empty': [(1,0,0,0), (1,0,0,0), (1,0,0,0), (1,0,0,0), (1,0,0,0)],
    ':': [(0,0,6,0), (2,2,2,0), (0,0,6,0), (2,2,2,0), (0,0,6,0)],
    '0': [(0,0,0,6), (0,2,2,2), (0,2,2,2), (0,2,2,2), (0,0,0,6)],
    '1': [(0,0,4,2), (0,0,2,4), (0,2,2,2), (0,0,4,2), (0,0,4,2)],
    '2': [(0,4,2,0), (0,0,4,2), (2,2,2,0), (0,2,4,0), (0,0,0,6)],
    '3': [(0,0,0,6), (0,0,4,2), (0,0,0,6), (0,0,4,2), (0,0,0,6)],
    '4': [(0,2,2,2), (0,2,2,2), (0,0,0,6), (0,0,4,2), (0,0,4,2)],
    '5': [(0,0,0,6), (0,2,4,0), (0,4,2,0), (0,0,4,2), (0,4,2,0)],
    '6': [(0,0,0,6), (0,2,4,0), (0,0,0,6), (0,2,2,2), (0,0,0,6)],
    '7': [(0,0,0,6), (0,0,4,2), (2,2,2,0), (2,2,2,0), (2,2,2,0)],
    '8': [(0,0,0,6), (0,2,2,2), (0,0,0,6), (0,2,2,2), (0,0,0,6)],
    '9': [(0,0,0,6), (0,2,2,2), (0,0,0,6), (0,0,4,2), (0,0,0,6)]
}

def sprint(text = '\n', color = "WHITE"):
    color = color.upper()
    if color == "RED":
        Color = Fore.RED
    elif color == "GREEN":
        Color = Fore.GREEN
    elif color == "BLUE":
        Color = Fore.BLUE
    elif color == "CYAN":
        Color = Fore.CYAN
    elif color == "LIGHTMAGENTA":
        Color = Fore.LIGHTMAGENTA_EX
    elif color == "LIGHTYELLOW":
        Color = Fore.LIGHTYELLOW_EX
    elif color == "LIGHTBLUE":
        Color = Fore.LIGHTBLUE_EX
    else:
        Color = Fore.WHITE
    print(Color, text, sep='', end='')
    
def number (number):
    counter = 0
    for line in line_true_false[number]:
            for _ in range(line[0]):
                OUT[counter].append(False)
            for _ in range(line[1]):
                OUT[counter].append(True)
            for _ in range(line[2]):
                OUT[counter].append(False)
            for _ in range(line[3]):
                OUT[counter].append(True)
            counter += 1

def print_OUT ():
    for i in range(5):
        for j in OUT[i]:
            if j == False:
                sprint(ALL_CHAR[randint(0,45)], BACKGROUND_COLOR)
            else:
                sprint(ALL_CHAR[randint(0,45)], NUMBERS_COLOR)
        print()

def print_color():
    print('1) RED')
    print('2) GREEN')
    print('3) BLUE')
    print('4) CYAN')
    print('5) LIGHTMAGENTA')
    print('6) LIGHTYELLOW')
    print('7) LIGHTBLUE')

def set_color(number):
    if number == 1:
        return 'RED'
    elif number == 2:
        return 'GREEN'
    elif number == 3:
        return 'BLUE'
    elif number == 4:
        return 'CYAN'
    elif number == 5:
        return 'LIGHTMAGENTA'
    elif number == 6:
        return 'LIGHTYELLOW'
    else:
        return 'LIGHTBLUE'
    
if __name__ == '__main__':
    print_color()
    BACKGROUND_COLOR = set_color(int(input('Choose a background color: ')))
    NUMBERS_COLOR = set_color(int(input('Choose a numbers color: ')))
    
    while(True):
        time = strftime("%H:%M:%S")

        for one_number in time:
            if one_number == ':':
                number('empty')
                number(one_number)
                number('empty')
            else:
                number(one_number)
                number('empty')
        print_OUT()
        OUT = [[],[],[],[],[]]
        sleep(1)
        system('cls')
