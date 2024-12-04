line = input()
line = line.split()
c = 0
for i in range(len(line)):
    c+=1
    if c == 3: 
        print(line[i], end = ' ')
        c = 0