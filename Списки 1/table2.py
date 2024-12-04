rows = int(input())
cols = int(input())
data = []
d = []
for x in range(1, 3):
    if x == 2:
        print('\n')
        cols, rows = rows, cols
        for z in range(0, rows):
            for y in range(z, len(data), rows):
                d += [data[y]]
        data = d
    else:
        for i in range(rows*cols):
            data += [input()]
    for i in range(len(data)):
        if i % cols == 0 and i != 0:
            print()
        print(data[i], '\t', sep='', end='')