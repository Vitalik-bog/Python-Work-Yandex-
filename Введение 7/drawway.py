way = input()
c=0
z = 0
brush = way[0]
print(brush, end='', sep='')
for i in range(1, len(way)):
    if way[i] == '>':
        print(brush, end='')
    if way[i] == '<':
        print(brush, end='', sep='')
        c += 1
    if way[i] == 'V':
        c += 1
        y = i+1
        print()
        if i+1 != len(way) and way[i+1] == '<':
            while y != len(way) and way[y] == '<':
                z += 1 
                y += 1
        print(' '*(i-c-z), brush, sep = '', end='')
        