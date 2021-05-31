from pyModbusTCP.client import ModbusClient


class Modbus():
    def __init__(self, host, port, unit_id):
        self.host = host
        self.port = port
        self.unit_id = unit_id

    def modbus_func(self):
        sensor_no = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)
        sensor_no.open()
        regs = sensor_no.read_holding_registers(0, 100)

        if regs:
            print(regs)
        else:
            print("read error")
