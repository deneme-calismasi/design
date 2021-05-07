import datetime
from tkinter import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Animation function
def animate(ax, xList, y1List, y2List):
    time = datetime.datetime.now().strftime("%H:%M:%S")
    lb_Time.config(text=time)
    lb_Time['text'] = time
    xList.append(time)
    #   Replace sample data below my real data...
    y1List.append(np.sin(len(xList)))
    y2List.append(2 * np.sin(len(xList)))
    # Limit x and y lists to 20 items
    xList = xList[-20:]
    y1List = y1List[-20:]
    y2List = y2List[-20:]
    line, = ax.plot_date(mpl.dates.datestr2num(xList), y1List)
    plt.show()
    fenster.after(1000, animate, ax, xList, y1List, y2List)


fenster = Tk()
fenster.title("Monitoring")
fenster.geometry("450x400")
lb_Time = Label(fenster)
exit_button = Button(fenster, text="Beenden", command=fenster.destroy, fg="red")
lb_Time.grid(row=2, column=0, pady=20)

xList = []
y1List = []
y2List = []

fig = plt.Figure(figsize=(2, 2))
canvas = FigureCanvasTkAgg(fig, master=fenster)
canvas.get_tk_widget().grid(row=3, column=1, pady=20)

ax = fig.add_subplot(111)
line, = ax.plot_date(xList, y1List)
animate(ax, xList, y1List, y2List)

fenster.mainloop()
