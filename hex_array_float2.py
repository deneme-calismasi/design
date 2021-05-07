import numpy as np

dec_array = [64247, 16830]

hex_array = [hex(x) for x in dec_array]

print(hex_array)

data_bytes = np.array([0xFAF7, 0x41BE], dtype=np.uint16)
data_bytes2 = np.array(dec_array, dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)
print(data_bytes)
print(data_bytes2)
print(data_as_float)

arr = [format(64247, '#04x'), format(16830, '#04x')]
arr2 = format(dec_array, '#04x')

print(arr)
print(arr2)
