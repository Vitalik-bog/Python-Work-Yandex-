n = int(input())
out = ''
data = [input() for i in range(n)]
for i in data:
    if not 'лук' in i:
        if i != data[-1]:
            out += i +', '
        else:
            out += i
    elif i == data[-1]:
        out = out[:-2]
print(out)
        