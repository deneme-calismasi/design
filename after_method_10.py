from tkinter import *
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

master = Tk()
tframe = Frame(master)
tframe.pack(fill='both')
data = {'1': {'Klasa': '6A', 'E Hene': 1, 'E Marte': 2, 'E Merkurre': 3, 'E Enjte': 4, 'E Premte': 5},
        '2': {'Klasa': '', 'E Hene': 1, 'E Marte': 2, 'E Merkurre': 3, 'E Enjte': 4, 'E Premte': 5}}
model = TableModel()
table = TableCanvas(tframe, model=model)
table.createTableFrame()
model = table.model
model.importDict(data)  # can import from a dictionary to populate model


def update_data(event=None):
    global data
    global model
    nk = "3"
    print("update_data \n")
    model.addRow(key=nk, Klasa="333")
    table.redraw()


master.after(5000, update_data)
master.mainloop()
