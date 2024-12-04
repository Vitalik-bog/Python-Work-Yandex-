from sys import stdin
import numpy as np
names = [''.join(name.split()) for name in stdin]
names = list(set([(name, names.count(name)) for name in names]))
names.sort()
res = sorted(names, key=lambda x: -int(x[1]))[:10]
for r in res:
    print(*r)


