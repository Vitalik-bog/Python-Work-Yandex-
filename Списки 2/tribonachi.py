ordint = ''
data = []
s, n = 0, ''
c = int(input())
for i in range(1, c+1):
    if i <= 3:
        ordint += '1 '
        print('1', end=' ')
    else:
        while s < len(ordint):
            if ordint[s] != ' ':
                n += ordint[s]
            if ordint[s] == ' ' or s == len(ordint) - 1:
                data += [int(n)]
                n = ''
            s += 1
        res = str(data[-1] + data[-2] + data[-3])
        ordint += res
        print(res, end=' ')