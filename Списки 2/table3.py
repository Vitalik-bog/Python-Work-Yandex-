rows = int(input())
cols = int(input())
data = []
for i in range(rows*cols):
    data += [input()]
j = 0
for i in data:
    if j % cols == 0 and j != 0:
        print()
    print(i, '\t', sep='', end='')
    j+=1