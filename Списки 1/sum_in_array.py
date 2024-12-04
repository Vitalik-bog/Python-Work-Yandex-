numbers = []
final = []
count = int(input())
for i in range(count):
    numbers.append(int(input()))
for j in range(1, len(numbers)):
    final.append(numbers[j] + numbers[j-1])
for x in range(len(final)):
    print(final[x])