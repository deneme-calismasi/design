from serial import *
from tkinter import *
import time

root = Tk()
root.geometry("1280x800")
root.attributes('-fullscreen', True)
bg = PhotoImage(file="C:/Users/halilerhan.orun/IdeaProjects/calisma1/animation.gif")

canvas = Canvas(root, width=1280, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

serialPort = "/dev/ttyUSB0"
ser = Serial(serialPort, 9600, timeout=0)
ser.flush()


def split_coords(astring):
    a, b = astring.split(';')
    a = int(a)
    b = int(b)

    return (a, b)


def paintRectangle1():
    canvas.create_rectangle(200, 120, 400, 220, fill='red')
    time.sleep(0.3)


def paintRectangle2():
    canvas.create_rectangle(600, 120, 800, 220, fill='red')
    time.sleep(0.3)


def paintRectangle3():
    canvas.create_rectangle(200, 260, 400, 360, fill='red')
    time.sleep(0.3)


def paintRectangle4():
    canvas.create_rectangle(600, 260, 800, 360, fill='red')
    time.sleep(0.3)


root.mainloop()

while True:

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        x, y = split_coords(line)
        print("x:", x, "- y:", y)

        if (19 < x < 60) and (20 < y < 40):
            print("OK button1")
            paintRectangle1()
        if (68 < x < 110) and (20 < y < 40):
            print("OK button2")
            paintRectangle2()
        if (19 < x < 60) and (45 < y < 80):
            print("OK button3")
            paintRectangle3()
        if (68 < x < 110) and (45 < y < 80):
            print("OK button4")
            paintRectangle4()

        # else:
        # paint the backgrand image again after the 0.3 seconds defined into the paintRectangle function
