import Modbus_PLC as md
from tkinter import *
import tkinter.messagebox as ms
import sys
from pyModbusTCP.client import ModbusClient

c = ModbusClient(port=502, auto_open=True)


# read descrete inputs:
def rd_dig_in(address, value):
    dig_in = c.read_discrete_inputs(address, value)


# A class created for Digital input readings and functions
# that used in the main GUI page:
class DigitalInputLamp():

    def __init__(self, label, img1, img2):
        self.images = [img1, img2]
        self.label = label
        self.state = 0
        self.label.config(image=self.images[self.state])

    def show_state(self, state):
        if state != self.state:
            self.state = state
            self.label.config(image=self.images[self.state])


def update_dig_in(lamps, period, canvas, func, gen_alarm, img1, img2):
    # reading the digital input registers:
    digital_inputs = md.c.read_discrete_inputs(0, len(lamps))
    for i, lamp in enumerate(lamps):
        # lamp is a class object element and it uses its class internal function show_state
        lamp.show_state(digital_inputs[i])
    canvas.after(period, func)


######################################################################################################
# First GUI page after running the program,
# the program asks the user for the PLC IP address and then a button to submit and destroy the window:
def Main_Page():
    global root1
    try:
        root1 = Tk()
        root1.title("GUI App")
        canvas44 = Canvas(root1, height=512, width=898, bg='#b8b8b9')
        canvas44.pack()
        ####here some codes for adding more widgets and frames  ####
        img_led8 = PhotoImage(file='C:\\Users\\Omer\\Desktop\\Green_led1.png')
        img_led9 = PhotoImage(file='C:\\Users\\Omer\\Desktop\\Red_led1.png')
        #### Here some code for creating the labels and placing them in the main GUI page  ####
        label_list = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12,
                      label13, label14, label15, label16, label17, label18, label19, label20, label21, label22, label23,
                      label24, label25, label26, label27, label28]

        # Using the class DigitalInputLamps in order to read the digital inputs and
        # presents them as the images img_led8 and img_led9:
        def func():
            lamps = [DigitalInputLamp(label_list[i], img_led8, img_led9) for i in range(28)]
            update_dig_in(lamps, 700, canvas44, func, General_alarm, img_gen_arm_on, img_gen_arm_off)

        func()
    except TypeError or AttributeError:
        ms.showerror(title="Error! No Connection!",
                     message="No Connection Has Been Found\nPlease Re-Type the IP address.")
        root1.quit()
    finally:
        def X_button_clicked():
            sys.exit()

        root1.protocol("WM_DELETE_WINDOW", X_button_clicked)
        answer = ms.askquestion(title="Retry App", message="Would you like to Retry the application?")
        if answer == 'yes':
            root1.destroy()
            IP_add_page()
        else:
            sys.exit("Exitting Program!")


def IP_add_page():
    root4 = Tk()
    root4.title("IP Address")

    canvas5 = Canvas(root4, height=120, width=250, bg='#b8b8b9')
    canvas5.pack()
    ip_var = StringVar()

    def submit():
        x = str(entry_ip.get())
        ip_var.set("")
        md.c.host(x)

    def close_IP_window():
        root4.destroy()
        print("closing windows")

    entry_ip = Entry(canvas5, textvariable=ip_var, font='Arial 15 bold')
    entry_ip.place(x=15, y=45)
    entry_ip.focus_force()
    button44 = Button(canvas5, font='Arial 10 bold', text='SUBMIT',
                      command=lambda: [submit(), close_IP_window(), Progress_bar()], relief=GROOVE)
    button44.place(x=5, y=91)
    label_ip1 = Label(canvas5, font='Arial 12 bold', text="Enter the PLC IP address: ", bg='#b8b8b9', fg='black')
    label_ip1.place(x=5, y=10)
    root4.resizable(False, False)

    root4.mainloop()


# The main GUI page which presents the digital input indications using picture of lamps (red for on , green for off)
if __name__ == '__main__':
    IP_add_page()
