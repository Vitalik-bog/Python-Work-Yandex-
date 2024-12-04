data = [i.lower() for i in input().replace(' ', '')]
res = ['', 0]
for i in data:
    if data.count(i) > res[1]:
        res[0] = i
        res[1] = data.count(i)
    elif data.count(i) == res[1]:
        res += [i, data.count(i)]
letters = res[::2]
counts = res[1::2]
letters.sort()
print(res[res.index(letters[0])])