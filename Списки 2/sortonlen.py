count = int(input())
data = []
for i in range(count):
    data += [input()]
for i in range(count - 1):
    for j in range(count - 1 - i):
        if len(data[j]) > len(data[j + 1]):
            data[j], data[j + 1] = data[j + 1], data[j]
        elif len(data[j]) == len(data[j + 1]):
            temp = [data[j], data[j+1]]
            temp.sort()
            data[j] = temp[0]
            data[j+1] = temp[1]
for el in data:
    print(el)
