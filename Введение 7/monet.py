string, res, data = input(), 0, 0
for i in range(len(string)):
    if string[i] == 'о':
        res += 1
        if res > data:
            data = res
        continue
    res = 0
print(data)