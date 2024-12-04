from random import randint
numbers = []
while len(numbers) < 25:
    if len(numbers) == 12: numbers.append(0); continue
    number = randint(1, 75)
    if not number in numbers: numbers.append(number)
for i in range(len(numbers)):
    if i % 5 == 0: print()
    print(numbers[i], end=' ')