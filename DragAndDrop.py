from tkinter import *
from tkinter import ttk


def downwars_shift(event):
    tv = event.widget
    select = [tv.index(s) for s in tv.selection()]
    select.append(tv.index(tv.identify_row(event.y)))
    select.sort()
    for i in range(select[0], select[-1] + 1, 1):
        tv.selection_add(tv.get_children()[i])


def move_down(event):
    tv = event.widget
    if tv.identify_row(event.y) not in tv.selection():
        tv.selection_set(tv.identify_row(event.y))


def move_up(event):
    tv = event.widget
    if tv.identify_row(event.y) in tv.selection():
        tv.selection_set(tv.identify_row(event.y))


def upward_shift(event):
    pass


def Movement(event):
    tv = event.widget
    moveto = tv.index(tv.identify_row(event.y))
    for s in tv.selection():
        tv.move(s, '', moveto)


ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#037272')

tv = ttk.Treeview(ws)
tv['columns'] = ('Eid', 'Name', 'Department')
tv.column('#0', width=0, stretch=NO)
tv.column('Eid', anchor=CENTER, width=80)
tv.column('Name', anchor=CENTER, width=80)
tv.column('Department', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Eid', text='Id', anchor=CENTER)
tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Department', text='Department', anchor=CENTER)

tv.insert(parent='', index=0, iid=0, text='', values=('E01', 'Vineet', 'Cisco'))
tv.insert(parent='', index=1, iid=1, text='', values=('E02', 'Anil', 'Design'))
tv.insert(parent='', index=2, iid=2, text='', values=('E03', 'Vaishali', 'IT/Security'))
tv.insert(parent='', index=3, iid=3, text='', values=('E04', 'Vimal', 'Support'))
tv.insert(parent='', index=4, iid=4, text='', values=('E05', 'Ankita', 'HR'))
tv.pack(pady=20)

tv.bind("<ButtonPress-1>", move_down)
tv.bind("<ButtonRelease-1>", move_up, add='+')
tv.bind("<B1-Motion>", Movement, add='+')
tv.bind("<Shift-ButtonPress-1>", downwars_shift, add='+')
tv.bind("<Shift-ButtonRelease-1>", upward_shift, add='+')

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
ws.mainloop()
