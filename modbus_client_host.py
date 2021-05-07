import random
import string
import numpy as np
from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)

c.open()

regs = c.read_holding_registers(0, 22)
if regs:
    print(regs)
else:
    print("read error")


def get_random_number():
    return random.uniform(1, 160)


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


start = 1
count = 22

value = [[num for num in range(start, start + count)],
         [num for num in range(start, start + count)],
         regs]

data = np.array(value)
print(*data.T)
