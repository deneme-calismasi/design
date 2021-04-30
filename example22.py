import numpy as np

dec_array = [64247, 16830]

hex_array = [hex(x) for x in dec_array]

data_bytes = np.array(dec_array, dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)
print(data_bytes)
print(data_as_float)
