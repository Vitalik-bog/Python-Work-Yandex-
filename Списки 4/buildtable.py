n = int(input())
data = [input().split() for i in range(n-1)]
temp = data[:]
for i in range(len(temp)):
    string = ''
    for j in range(len(temp[i])):
        string += temp[i][j] + ' '
    temp[i] = string
data_inv = []
for j in range(len(max(data, key=len))):
    string = ''
    for i in data:
        if len(i) >= 1:
            string += ' ' + i[0]
            del i[0]
    data_inv +=[string]

data = temp
print()
for i in range(n):
    line = ['0']
    if i != len(data_inv)-list(line).count(' '):
        line += [data_inv[i]]
    if len(line)-list(line).count(' ') < n and i !=0:
        line.insert(0, data[i-1])
    print(''.join(line))