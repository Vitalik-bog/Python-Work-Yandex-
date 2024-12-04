rows = int(input())
cols = int(input())
data = []
for i in range(rows*cols):
    data += [input()]
if rows > 1:
    first = data[:cols]
    last = data[-cols:]
    data = data[cols:-cols]
    j = 0
    temp = []
    newdata = []
    for i in data:
        if j % cols == 0 and j != 0:
            temp.sort()
            newdata += temp
            temp = []
            temp+=[i]
        else:
            temp += [i]
        j+=1
    temp.sort()
    newdata += temp
    data = newdata
    j = 0
    for i in first:
        print(i, '\t', sep='', end='')
        j+=1
    print()
j = 0
if data != []:
    for i in data:
        if j % cols == 0 and j != 0:
            print()
        print(i, '\t', sep='', end='')
        j+=1
    j = 0
    print()
if rows > 1:
    for i in last:
        print(i, '\t', sep='', end='')
        j+=1