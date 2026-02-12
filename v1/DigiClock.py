from colorama import Fore, init, Style
from random import randint
from time import strftime, sleep
import sys
import os

# مقداردهی اولیه برای پشتیبانی از کدهای ANSI در ویندوز
init(autoreset=True)

ALL_CHAR = '!@#$%^&*()+=}{/?<>QWERTYUIOP{}LKJHGFDSAZXCVBNM'
OUT = [[],[],[],[],[]]

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

COLOR_MAP = {
    1: Fore.RED, 2: Fore.GREEN, 3: Fore.BLUE, 
    4: Fore.CYAN, 5: Fore.LIGHTMAGENTA_EX, 
    6: Fore.LIGHTYELLOW_EX, 7: Fore.LIGHTBLUE_EX
}

def get_color_code(number):
    return COLOR_MAP.get(number, Fore.WHITE)

def add_number_to_out(num_char):
    counter = 0
    if num_char not in line_true_false: return
    for line in line_true_false[num_char]:
        for _ in range(line[0]): OUT[counter].append(False)
        for _ in range(line[1]): OUT[counter].append(True)
        for _ in range(line[2]): OUT[counter].append(False)
        for _ in range(line[3]): OUT[counter].append(True)
        counter += 1

def build_frame(bg_color, num_color):
    # کد \033[H مکان‌نما را به سطر اول و ستون اول می‌برد
    buffer = "\033[H" 
    for i in range(5):
        line_content = ""
        for is_num in OUT[i]:
            char = ALL_CHAR[randint(0, len(ALL_CHAR)-1)]
            color = num_color if is_num else bg_color
            line_content += f"{color}{char}"
        # کد \033[K محتویات باقی‌مانده از خط قبلی را پاک می‌کند تا بهم‌ریختگی ایجاد نشود
        buffer += line_content + "\033[K\n"
    return buffer

if __name__ == '__main__':
    # پاک کردن اولیه صفحه
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('--- Color Options ---')
    print('1) RED  2) GREEN  3) BLUE  4) CYAN\n5) MAGENTA  6) YELLOW  7) LIGHTBLUE')
    
    try:
        bg_choice = int(input('\nChoose background color (1-7): '))
        nm_choice = int(input('Choose numbers color (1-7): '))
        
        bg_color = get_color_code(bg_choice)
        nm_color = get_color_code(nm_choice)

        # مخفی کردن مکان‌نما برای زیبایی بیشتر (در برخی ترمینال‌ها کار می‌کند)
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

        while True:
            current_time = strftime("%H:%M:%S")
            OUT = [[],[],[],[],[]]
            
            for char in current_time:
                if char == ':':
                    add_number_to_out('empty')
                    add_number_to_out(char)
                    add_number_to_out('empty')
                else:
                    add_number_to_out(char)
                    add_number_to_out('empty')
            
            # چاپ فریم نهایی
            sys.stdout.write(build_frame(bg_color, nm_color))
            sys.stdout.flush()
            
            sleep(1)
            
    except KeyboardInterrupt:
        # نشان دادن دوباره مکان‌نما موقع خروج
        sys.stdout.write("\033[?25h" + Style.RESET_ALL)
        print("\nStopped by user.")
    except Exception as e:
        sys.stdout.write("\033[?25h" + Style.RESET_ALL)
        print(f"\nAn error occurred: {e}")