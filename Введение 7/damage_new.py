count, t, d, damage = int(input()), 0, 0, [0, 0]
for i in range(count):
    t = int(input())
    d = int(input())
    if i == 0:
        damage[0] = t
        damage[1] = d
    else:
        damage[0] = damage[0] * d + damage[1] * t
        damage[1] = damage[1] * d
nod = damage[0]
nod_2 = damage[1]
while nod!=0 and nod_2!=0:
    if nod > nod_2:
        nod = nod % nod_2
    else:
        nod_2 = nod_2 % nod
if nod != 0:
    print(damage[0]//nod, '/', damage[1]//nod, sep='')
elif nod_2 != 0:
    print(damage[0]//nod_2, '/', damage[1]//nod_2, sep='')