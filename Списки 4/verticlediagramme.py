In = [int(i) for i in input().split()]
height = max(In) + 1
data = []
print('*' *(len(In)+2))
for i in In:
    string = ' '*(height - i) + '*'*i
    data += [string]
for j in range(height):
    string = ''
    for i in range(len(data)):
        string += data[i][j]
    print('*', string ,'*', sep='')