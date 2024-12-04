n = int(input())
d = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i, end = ' ')
        d += 1
if d != 2:
    print('\nНЕТ')
else:
    print('\nПРОСТОЕ')