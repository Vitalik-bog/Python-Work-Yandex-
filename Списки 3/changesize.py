height = int(input())
width = int(input())
data = []
for i in range(height):
    data += [input()]
for el in range(len(data)):
    data[el] = data[el][::2]
for el in data[::2]:
    print(el)