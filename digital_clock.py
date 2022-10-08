#!/usr/bin/env python

import sys
from tkinter import *
import time


# display the current time
def Clock():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(100, Clock)


# Let's Make Window for Clock
window = Tk()
window.title('Digital Clock')
message = Label(window, font=("times", 100, "bold"), text="Time", fg="black")
message.grid(row=0, column=0)
clock = Label(window, font=("times", 150, "bold"), fg="white", bg="blue")
clock.grid(row=1, column=0)
Clock()

mainloop()
