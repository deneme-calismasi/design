import tkinter as tk


def flash():
    root.after(2000, lambda: label.configure(background="white"))
    root.after(4000, lambda: label.configure(background="yellow"))


root = tk.Tk()
label = tk.Label(root, text="Hello", background="yellow")
button = tk.Button(root, text="Flash!", command=flash)
label.pack(side="top", fill="x")
button.pack(side="bottom", padx=20, pady=20)

root.mainloop()
