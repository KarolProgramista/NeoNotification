import tkinter as tk
import time
from Config import *

class Notification():
    def __init__(self, title, text):
        self.time = Time
        self.title = title
        self.text = text
        self.width = Width
        self.height = Height
        self.y_offset = Yoffset
        self.x_offset = Xoffset
        self.bg = Bg
        self.fg = Fg
        self.title_size = TitleSize
        self.text_size = TextSize

    def show(self):
        start_time = time.time()
        root = tk.Tk() # create a Tk root window
        root.resizable(False, False)
        root.overrideredirect(True)
        root.title(self.title)

        # get screen width and height
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        if (self.x_offset < 0):
            x = ws-self.width-2
        else:
            x = self.x_offset

        if(self.y_offset < 0):
            y = hs-self.height-2
        else:
            y = self.y_offset

        # set the dimensions of the screen 
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

        main_frame = tk.Frame(root, bg=self.bg)
        main_frame.place(relwidth=1, relheight=1)

        title = tk.Label(main_frame, text=self.title, bg=self.bg, fg=self.fg, anchor='w', font=("Monospace", self.title_size))
        title.place(relwidth=1, relheight=0.2)

        dsc = tk.Label(main_frame, text=self.text, anchor='nw', bg=self.bg, fg=self.fg, font=("Monospace", self.text_size))
        dsc.place(rely=0.25, relwidth=1, relheight=0.75)

        while True:
            if time.time() - start_time >= self.time:
                root.destroy()
                break
            try: 
                root.update()
            except:
                exit()
