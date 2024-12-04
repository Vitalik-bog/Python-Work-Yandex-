count = int(input())
line = False
cat = False
for i in range(count):
    line = input()
    if 'кот' in line or 'Кот' in line:
        cat = True
    elif 'пёс' in line or 'Пёс' in line:
        cat = False
if cat:
    print('МЯУ')
else:
    print('НЕТ')