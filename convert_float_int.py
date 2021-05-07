import numpy as np

data_bytes = np.array([0xF7, 0xFA, 0xBE, 0x41], dtype=np.uint8)

data_as_float = data_bytes.view(dtype=np.float32)

print(data_bytes)
print(data_as_float)

dec_array = [64247, 16830]

hex_array = [hex(x) for x in dec_array]

print(hex_array)

data_bytes2 = np.array([0xFAF7, 0x41BE], dtype=np.uint16)

data_as_float2 = data_bytes2.view(dtype=np.float32)

print(data_bytes2)
print(data_as_float2)

data_bytes3 = np.array(dec_array, dtype=np.uint16)

data_as_float3 = data_bytes3.view(dtype=np.float32)


print(data_bytes3)
print(data_as_float3)
