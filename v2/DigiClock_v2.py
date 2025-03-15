import tkinter as tk
import time
import os
import json

WINDOW_WIDTH: int
WINDOW_HEIGHT: int

with open("v2\Clock_info.json", 'r') as f:
    data = json.load(f)
    WINDOW_WIDTH = data["window_info"]["window_width"]
    WINDOW_HEIGHT = data["window_info"]["window_height"]
 

window = tk.Tk()

window_screenwidth = window.winfo_screenwidth()
window_screenheight = window.winfo_screenheight()
window_x = int((window_screenwidth/2)-(WINDOW_WIDTH/2))
window_y = int((window_screenheight/2)-(WINDOW_HEIGHT/2))

window.geometry(F"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")

# print(window_height)
print(WINDOW_WIDTH)

# window.geometry(f"{int()}")


tk.mainloop()