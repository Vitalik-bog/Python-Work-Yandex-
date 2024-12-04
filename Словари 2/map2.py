coords = {}
for i in range(int(input())):
    point = tuple([c[:-1].ljust(1, '0') for c in input().split()])
    coords[point] = coords.get(point, 0)+1
print(max(coords.items(), key=lambda element: element[1])[1])