from pyModbusTCP.client import ModbusClient
import time
from pyModbusTCP import utils

try:
    c = ModbusClient(host="localhost", port=502)
except ValueError:
    print("Error with host or port params")

c = ModbusClient(host="localhost", auto_open=True)

if c.open():
    regs_list_1 = c.read_holding_registers(0, 10)
    regs_list_2 = c.read_holding_registers(55, 10)
    c.close()

while True:
    if c.is_open():
        regs_list_1 = c.read_holding_registers(0, 10)
        regs_list_2 = c.read_holding_registers(55, 10)
    else:
        c.open()
    time.sleep(1)



list_16_bits = [0x0123, 0x4567, 0x89ab, 0xcdef]

# big endian sample (default)
list_32_bits = utils.word_list_to_long(list_16_bits)
# display "['0x1234567', '0x89abcdef']"
print([hex(i) for i in list_32_bits])

# little endian sample
list_32_bits = utils.word_list_to_long(list_16_bits, big_endian=False)
# display "['0x45670123', '0xcdef89ab']"
print([hex(i) for i in list_32_bits])
