import numpy as np
x, y = [int(i) for i in input().split()]
a = np.array(range(1, x*y+1)).reshape(x,y)
for i in range(len(a)):
    if i % 2 != 0:
        a[i] = list(reversed(a[i]))
print(a)

