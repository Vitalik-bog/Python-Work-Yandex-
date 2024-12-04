In = [input().split() for i in range(int(input()))]
alls = []
medians = []
mods = []
#
for d in In:
    for i in d:
        d[d.index(i)] = float(i)
        alls += [float(i)]
for data in In:
    res = ['', 0]
    for i in data:
        if data.count(i) > res[1]:
            res[0] = i
            res[1] = data.count(i)
        elif data.count(i) == res[1]:
            res += [i, data.count(i)]
    letters = res[::2]
    mods += [res[res.index(letters[0])]]
    data.sort()
    
    if len(data) % 2 != 0:
        medians += [round(float(data[len(data) // 2]))]
    else:
        medians += [round(float((data[len(data) // 2 -1] + data[len(data) // 2])/2))]
        
for i in range(len(medians)):
    print(medians[i], end = ' ')
print()
for i in range(len(mods)):
    print(round(mods[i]), end = ' ')
    
medians.sort()
print()

if len(medians) % 2 != 0:
    print(round(float(medians[len(medians) // 2])))
else:
    print(round(float((medians[len(medians) // 2 -1] + medians[len(medians) // 2])/2)))
    
res = ['', 0]
for i in mods:
    if mods.count(i) > res[1]:
        res[0] = i
        res[1] = mods.count(i)
    elif mods.count(i) == res[1]:
        res += [i, mods.count(i)]
letters = res[::2]
print(round(res[res.index(letters[0])]))

alls.sort()

if len(alls) % 2 != 0:
    print(round(float(alls[len(alls) // 2])))
else:
    print(round(float((alls[len(alls) // 2 -1] + alls[len(alls) // 2])/2)))
    
res = ['', 0]
for i in alls:
    if alls.count(i) > res[1]:
        res[0] = i
        res[1] = alls.count(i)
    elif alls.count(i) == res[1]:
        res += [i, alls.count(i)]
letters = res[::2]
print(round(res[res.index(letters[0])]))
