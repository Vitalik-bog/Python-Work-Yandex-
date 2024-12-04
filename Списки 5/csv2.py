data = []
out = []
changed = False
for i in range(int(input())):
    line = input()
    row = ''
    for j in range(len(line)):
        if changed == False:
            if line[j] == '\\':
                if j+1 == len(line) or line[j+1] != ',':
                    row += line[j]
                elif j+1 != len(line) and line[j+1] == ',':
                    row += ','
                    changed = True
                    continue
                elif j+1 != len(line) and line[j+1] == 'n':
                    row += '\n'
                    changed = True
                    continue                    
            elif line[j] ==',':
                data += [row]
                row = ''
            else:
                row += line[j]
        changed = False
        
    if row:
        data += [row]
    out += [data]
    data = []
echo = []
for i in range(int(input())):
    query = input().split(',')
    echo += [out[int(query[0])][int(query[1])].replace('\\n', '\n')]
for i in echo:
    print(i)