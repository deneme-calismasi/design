class Window(Frame):
    def __init__(self, figure, master, SerialReference):
        Frame.__init__(self, master)
        self.entry = None
        self.setPoint = None
        self.master = master  # a reference to the master window
        self.serialReference = SerialReference  # keep a reference to our serial connection so that we can use it for bi-directional communicate from this class
        self.initWindow(figure)  # initialize the window with our settings

    def initWindow(self, figure):
        self.master.title("Real Time Plot")
        canvas = FigureCanvasTkAgg(figure, master=self.master)
        toolbar = NavigationToolbar2TkAgg(canvas, self.master)
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        # create out widgets in the master frame
        lbl1 = Tk.Label(self.master, text="Scaling Factor")
        lbl1.pack(padx=5, pady=5)
        self.entry = Tk.Entry(self.master)
        self.entry.insert(0, '1.0')  # (index, string)
        self.entry.pack(padx=5)
        SendButton = Tk.Button(self.master, text='Send', command=self.sendFactorToMCU)
        SendButton.pack(padx=5)

    def sendFactorToMCU(self):
        self.serialReference.sendSerialData(self.entry.get() + '%')  # '%' is our ending marker
