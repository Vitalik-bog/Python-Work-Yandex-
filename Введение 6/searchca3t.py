count = 0
first = 0
word = input()
line = 0
while word != 'СТОП':
    line += 1
    if 'кот' in word or 'Кот' in word:
        count +=1
        if not first:
            first = line
    word = input()
if count != 0:
    print(count, first)
else:
    print(count, -1)