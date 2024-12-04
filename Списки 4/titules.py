tituls = ''
count = int(input())
c = 0
while count != c:
    line = input()
    if line != '*':
        line = line.split()
        for i in range(len(line)):
            line[i] += '-'
        line = ''.join(line)
        tituls += line
    else:
        c+=1
        tituls += '*'
tituls = tituls.split('*')
out = []
for i in range(len(tituls)-1, -1, -1):
    if tituls[i] == '':
        del tituls[i]
        continue
    if tituls[i][-1] == '-':
        tituls[i] = tituls[i][:-1]  
    if tituls[i][0] == '-':
        tituls[i] = tituls[i][1:]
    out += [tituls[i]]
print(', '.join(out))
