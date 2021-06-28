from tkinter import *

root = Tk()


def doSomething():
    x = int(l["text"])
    l["text"] = x + 1
    if int(l["text"]) < 50:  # Only repeat this function as long as this condition is met
        l.after(2000, doSomething)


root.geometry("300x300")
l = Label(root, text="0")
l.pack()

doSomething()

root.mainloop()
