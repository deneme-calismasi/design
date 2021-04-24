"""from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.config()
ws.geometry('200x300')

ws.maxsize(500, 500)

Label(
    ws,
    text="Life means lot more \n than you know",
    font=('Times', 20),
    bg = '#156475',
    fg = '#fff'
).pack(fill=BOTH, expand=True)

ws.mainloop()
"""

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x300')
ws.config(bg='#345')

canvas = Canvas(
    ws,
    height=200,
    width=200,
    bg="#fff"
)

canvas.pack()

canvas.create_rectangle(
    30, 30, 180, 120,
    outline="#fb0",
    fill="#fb0")

ws.mainloop()
