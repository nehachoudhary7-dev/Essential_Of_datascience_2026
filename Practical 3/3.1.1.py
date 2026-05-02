import numpy as np
import numpy as np

r, c = map(int, input().split())
elements = []

for _ in range(r):
    elements.extend(list(map(int, input().split())))

arr = np.array(elements).reshape(r, c)

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
