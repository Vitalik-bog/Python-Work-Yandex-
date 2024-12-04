import numpy as np
def makefield(size):
    a = np.ones(size*size, dtype=np.int8).reshape(size,size)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j % 2 == 0: a[i][j] = 0
        if i % 2 == 0:
            a[i] = [int(not x) for x in a[i]]
    return a

