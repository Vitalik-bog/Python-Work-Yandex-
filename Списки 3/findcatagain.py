count = int(input())
data = []
for i in range(count):
    line = input()
    if 'кот' in line:
        for j in range(len(line)):
            if line[j] == 'т' and line[j-1] == 'о' and line[j-2] == 'к':
                data += [str(i+1) + ' ' + str(j - 1)]
                break
for i in data:
    print(i)