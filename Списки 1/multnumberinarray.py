count = int(input())
numbers = []
for i in range(count):
    numbers += [int(input())]
n = int(input())
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] * numbers[j] == n:
            print('ДА')
            exit()
print('НЕТ')
