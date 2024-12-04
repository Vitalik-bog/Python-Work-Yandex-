import numpy as np
def supersort(n, m):
    a = np.array([np.random.randint(1, 100) for _ in range(n*m)]).reshape(n,m)
    b = a.copy()
    b = b.transpose()
    [b[i].sort() for i in range(len(b)) if i % 2 == 0]
    for i in range(len(b)):
        if i % 2 != 0: b[i] = sorted(b[i], reverse=True)
    b = b.transpose()
    return (a,b)
