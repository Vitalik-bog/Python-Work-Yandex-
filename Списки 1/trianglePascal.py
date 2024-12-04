number, s, n = int(input()), 0, ''
row = '1'
data = []
for i in range(number):
    print(row)
    if i == 0:
        row += ' 1'
        continue
    else:
        s = 0
        while s < len(row):
            if row[s] != ' ':
                n += row[s]
            if row[s] == ' ' or s == len(row) - 1:
                data += [int(n)]
                n = ''
            s += 1
        row = '1 '
        for j in range(1, len(data)):
            row += str(int(data[j])+int(data[j-1])) + ' '
        row += '1'
        data = []
