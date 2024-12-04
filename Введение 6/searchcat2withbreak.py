finded = -1
line = False
i = 1
while line != 'СТОП':
    line = input()
    if ('кот' in line or 'Кот' in line) and finded == -1:
        finded = i
        break
    i+=1
print(finded)