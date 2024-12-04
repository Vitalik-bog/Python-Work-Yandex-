number = int(input())
i = 0;
while number != 1:
    i += 1;
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
print(i)