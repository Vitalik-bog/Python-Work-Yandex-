size = int(input())
data = []
win = '-'
for j in range(size):
    data += [input()]
for d in data:
    if 'xxx' in d:
        win = 'x'
        break
    elif 'ooo' in d:
        win = 'o'
        break

if win == '-':
    temp = []
    string = ''    
    for i in range(size):
        for d in data:
            string += d[i]
        temp += [string]
        string = ''
    for d in temp:
        if 'xxx' in d:
            win = 'x'
            break
        elif 'ooo' in d:
            win = 'o'
            break
print(win)