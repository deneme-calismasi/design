from tkinter import *


class SimpleTableInput(Frame):
    def __init__(self, parent, rows, columns):
        Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                if column == 3:
                    e = Entry(self, validate="key", validatecommand=vcmd)
                else:
                    e = Entry(self)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e

        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)

        ##      Lookup table:
        self.LookUpList = [
            ['a', 'Black skirt', 'PP', '2000'],
            ['b', 'Pink T-shirt', 'PP', '1000'],
            ['c', 'Yellow skirt', 'Marela', '1500'],
            ['d', 'White trousers', 'PP', '2000']]

        ## Bind the Return/Enter key to populate the entries
        for row in range(self.rows):
            self._entry[row, 0].bind("<Return>", self.autofill)

    def in_list(self, list_of_lists, item):
        if not list_of_lists:
            return None
        if item in list_of_lists[0]:
            return list_of_lists[0]
        return self.in_list(list_of_lists[1:], item)

    ## The method that will be called to populate the entries
    def autofill(self, event):
        row = int(event.widget.grid_info()['row'])
        auto_list = self.in_list(self.LookUpList, self._entry[row, 0].get())
        self._entry[row, 1].delete(0, 'end')
        self._entry[row, 1].insert(0, auto_list[1])

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):

        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        names = ["Cislo produktu",
                 "Popis produktu",
                 "Znacka",
                 "Mnozstvi",
                 "Jednotkova cena",
                 "Prodejna",
                 "Celkova cena"]
        frame = Frame(self)
        frame.pack(side="top", fill="both")
        for i, title in enumerate(names):
            l = Label(frame, text=title)
            l.grid(row=0, column=i)
            frame.grid_columnconfigure(i, weight=1)
        self.EmptySpace = Label(self)
        self.table = SimpleTableInput(self, 30, 7)
        self.table.pack(side="top", fill="both")
        self.EmptySpace.pack(side="top", fill="both")

    ##        frame1 = Frame(self)
    ##        frame1.pack(side="left",fill="both")
    ##        self.SubButton = Button(self, text="Ulozit a zavrit", command=self.on_ulozit)
    ##        self.StornoButton = Button(self, text="Stornovat nakup", command=self.on_storno)
    ##        self.SubButton.pack(side="left", fill="both", expand=True)
    ##        self.StornoButton.pack(side="left", fill="both", expand=True)

    def on_ulozit(self):

        data = self.table.get()
        data1 = [list(filter(None, lst)) for lst in data]
        data2 = list(filter(None, data1))
        for item in data2:
            item.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        ##            look up property
        with open('C:\\Users\\chroustovskyj\\Desktop\\Dev_py\\App\\Data_Storage\\Data_Storage.csv', 'a',
                  newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data2)
        root.destroy()

    def on_storno(self):
        print("This is storno.")


if __name__ == '__main__':
    root = Tk()
    root.wm_title("Formular")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    Example(root).pack(side="top", fill="both", expand=False)
    root.mainloop()
