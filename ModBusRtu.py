import tkinter as tk
from tkinter import *
from tkinter import ttk
from time import time
import minimalmodbus
import serial

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.gas = minimalmodbus.Instrument('COM3', 1)
        self.gas.serial.baudrate = 9600
        self.gas.serial.bytesize = 8
        self.gas.serial.parity = serial.PARITY_NONE
        self.gas.serial.stopbits = 1
        self.gas.serial.timeout = 0.25
        self.gas.mode = minimalmodbus.MODE_RTU

        self.value_display = tk.Label(self, text='value', width=10)
        self.value_display.pack(side="top")

        self.unit_display = tk.Label(self, text='unit', width=10)
        self.unit_display.pack(side="top")

        self.gas_display = tk.Label(self, text='temp', width=10)
        self.gas_display.pack(side="top")

        self.status_display = tk.Label(self, text='status', width=10)
        self.status_display.pack(side="top")

        self.command_display = tk.Label(self, text='command', width=10)
        self.command_display.pack(side="top")

        self.pressure_display = tk.Label(self, text='pressure', width=10)
        self.pressure_display.pack(side="top")

        self.timer_button = tk.Button(self, text='Start', command=self.toggle)
        self.timer_display = tk.Label(self, text='00:00', width=10)
        self.timer_button.pack(side="top")
        self.timer_display.pack(side="top")
        self.paused = True

    def gas_meth(self):
        try:
            gas_value = self.gas.read_registers(0, 42)

            self.value_display.config(text=gas_value[0])
            self.unit_display.config(text=gas_value[1])
            self.gas_display.config(text=gas_value[2])
            self.status_display.config(text=gas_value[3])
            self.command_display.config(text=gas_value[4])
            self.pressure_display.config(text=gas_value[5])

        except IOError:
            self.gas_display.config(text="Lost con.")
        except ValueError:
            self.gas_display.config(text="RTU error")
        self.gas_display.after(1000, self.gas_meth)

    def toggle(self):
        if self.paused:
            self.paused = False
            self.timer_button.config(text='Stop')
            self.oldtime = time()
            self.run_timer()
            self.gas_meth()
        else:
            self.paused = True
            self.oldtime = time()
            self.timer_button.config(text='Start')

    def run_timer(self):
        if self.paused:
            return
        delta = int(time() - self.oldtime)
        timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
        self.timer_display.config(text=timestr)
        self.timer_display.after(500, self.run_timer)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b1.pack(side="left")
        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x600")
    root.mainloop()
