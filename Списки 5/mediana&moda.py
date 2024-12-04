data = [float(i) for i in input().split()]
res = ['', 0]
for i in data:
    if data.count(i) > res[1]:
        res[0] = i
        res[1] = data.count(i)
    elif data.count(i) == res[1]:
        res += [i, data.count(i)]
letters = res[::2]
moda = res[res.index(letters[0])]
data.sort()

if len(data) % 2 != 0:
    median = float(data[len(data) // 2])
else:
    median = float((data[len(data) // 2 -1] + data[len(data) // 2])/2)
print(round(median), round(moda))
