count = int(input())
isset = False
for i in range(count):
    line = input()
    if 'кот' in line or 'Кот' in line:
        isset = True
if isset:
    print('МЯУ')
else:
    print('НЕТ')