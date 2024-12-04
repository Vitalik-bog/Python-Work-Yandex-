number = int(input())
i = 0
while number % 2 == 0:
    number = number / 2
    i += 1
if number == 1:
    print(i)
else:
    print('НЕТ')