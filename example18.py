import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [-1, -2, -3, -4, -5, -6, -7], [11, 12, 13, 14, 15, 16, 17]])
print(*a)

print(*a.T)

start = 1
count = 3
possible = [[num for num in range(start, start + count)], [num for num in range(start, start + count)],
            [num for num in range(start, start + count)]]
print(possible)
b = np.array(possible)
print(*b.T)
