data = []
for i in range(int(input())):
    data += [[i for i in input().split(',')]]
out = []
for i in range(int(input())):
    temps = input().split(',')
    out += [data[int(temps[0])][int(temps[1])]]
for i in out:
    print(i)