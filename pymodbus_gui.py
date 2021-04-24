from pymodbus.client.sync import ModbusTcpClient
import struct
import sys
from PyQt5 import QtCore, QtGui, uic

form_class = uic.loadUiType("C:\Users\David\.PyCharm30\VC-22D Modbus TCP\UI Design\Modbus-     MainScreen.ui")[0]
form_class2 = uic.loadUiType("C:\Users\David\.PyCharm30\VC-22D Modbus TCP\UI Design\Modbus- ConnectMenu.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(1500, 1200)
        self.dial.valueChanged.connect(self.dialValueChanged)
        self.pushButton_Connect.clicked.connect(self.modbusConnect)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowIcon(QtGui.QIcon("C:\Users\David\.PyCharm30\VC-22D Modbus TCP\UI  Design\Cla-Val_30px.png"))

    def modbusConnect(self):
        # modbus connection
        ipaddress = str(self.lineEdit_IP.text())
        client = ModbusTcpClient(ipaddress)
        testconnection = client.connect()
        if testconnection == True:
            print("Connection Successful")
        else:
            print("Connection Not Successful")
            print(self.lineEdit_IP.text())
            exit()

    def dialValueChanged(self):
        setvalue = float(self.label.text())
        if setvalue == 0:
            setvalueint = 0
        else:
            setvaluehex = str(hex(struct.unpack('<I', struct.pack('<f', setvalue))[0]))
            setvaluehexstr = setvaluehex[:-4]
            setvalueint = int(setvaluehexstr, 16)


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
