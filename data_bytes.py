import numpy as np

data_bytes = np.array([0xF7, 0xFA, 0xBE, 0x41], dtype=np.uint8)
data_as_float = data_bytes.view(dtype=np.float32)
print(data_as_float)
