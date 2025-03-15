import tkinter as tk
from time import strftime
import json

WINDOW_WIDTH: int
WINDOW_HEIGHT: int
BACKGROUND_COLOR: str
NUMBER: dict
CLOCK_X: int
CLOCK_Y: int
CLOCK_COLOR: str
NUMBER_SPACING: int
PIXEL_SIZE: int

def get_base_data():
    with open("v2\Clock_info.json", 'r') as f:
        global WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR, NUMBER, CLOCK_X, CLOCK_Y, CLOCK_COLOR, NUMBER_SPACING, PIXEL_SIZE 
        data = json.load(f)
        WINDOW_WIDTH = data["window_info"]["window_width"]
        WINDOW_HEIGHT = data["window_info"]["window_height"]
        PIXEL_SIZE = data["window_info"]["pixel_size"]
        BACKGROUND_COLOR = data["canvas_info"]["background_color"]
        CLOCK_X = data["Clock_info"]["x"]
        CLOCK_Y = data["Clock_info"]["y"]
        CLOCK_COLOR = data["Clock_info"]["clock_color"]
        NUMBER_SPACING = data["Clock_info"]["number_spacing"]
        NUMBER = data["number"]

def set_window(window):
    window: tk.Tk
    window_screenwidth = window.winfo_screenwidth()
    window_screenheight = window.winfo_screenheight()
    window_x = int((window_screenwidth/2)-(WINDOW_WIDTH/2))
    window_y = int((window_screenheight/2)-(WINDOW_HEIGHT/2))
    window.geometry(F"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")
    
def update_clock(canvas):
    canvas.delete("all")
    newtime = strftime("%H:%M:%S")
    pixel_time = list()
    for number in newtime:
        pixel_time.append(NUMBER[str(number)])
    x = CLOCK_X
    y = CLOCK_Y
    for number in pixel_time:
        for row in number:
            for pixel in row:
                if pixel == 1:
                    canvas.create_rectangle(x,y, x+PIXEL_SIZE, y+PIXEL_SIZE, fill=CLOCK_COLOR)
                x += PIXEL_SIZE
            x -= PIXEL_SIZE*len(row)
            y += PIXEL_SIZE
        y -= PIXEL_SIZE*len(number)
        x += (PIXEL_SIZE*len(number[0])) + NUMBER_SPACING
    canvas.pack()
    canvas.after(1000, update_clock, canvas)
    

def main():
    get_base_data()
    window = tk.Tk()
    window.title("Digiclock v2")
    set_window(window)
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
    update_clock(canvas)
    
    tk.mainloop()
    
main()