rows = int(input())
cols = int(input())
data = []
for i in range(rows*cols):
    data += [input()]
for i in range(len(data)):
    if i % cols == 0 and i != 0:
        print()
    print(data[i], '\t', sep='', end='')