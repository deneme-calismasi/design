import random
from tkinter.ttk import Label
from table_and_graph import frame
import tkinter as tk
from tkinter import *

tiles_letter = ['a', 'b', 'c', 'd', 'e']

root = tk.Tk()
root.title("Sensor's Temperatures °C")
root.geometry("480x630")
root.grid()


def add_letter():
    rand = random.choice(tiles_letter)
    tile_frame = Label(frame, text=rand)
    tile_frame.pack()
    root.after(5, add_letter)
    tiles_letter.remove(rand)  # remove that tile from list of tiles


root.after(0, add_letter)  # add_letter will run as soon as the mainloop starts.
root.mainloop()
