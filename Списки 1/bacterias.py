size = int(input())
bctrs = []
for j in range(size):
    bctrs += [[]]
j = 0
for i in range(size ** 2):
    if i % size == 0 and i != 0:
        j += 1 
    bctrs[j] += [int(input())]
k = int(input())
for i in range(k):
    x = int(input())
    y = int(input())
    bctrs[y][x] -= 8
    if x == 0 and y == 0:
        bctrs[y][x+1] -= 4
        bctrs[y+1][x] -= 4
        bctrs[y+1][x+1] -= 4
    elif x == size-1 and y == 0:
        bctrs[y][x-1] -= 4
        bctrs[y+1][size-1] -= 4
        bctrs[y+1][size-2] -= 4
    elif x == 0 and y == size-1:
        bctrs[y-1][0] -= 4
        bctrs[y-1][1] -= 4
        bctrs[y][1] -= 4
    elif x == size-1 and y == size-1:
        bctrs[y-1][-1] -= 4
        bctrs[y-1][-2] -= 4
        bctrs[y][-2] -= 4
    elif x == 0 and not y in [0, size-1]:
        bctrs[y-1][1] -= 4
        bctrs[y-1][0] -= 4
        bctrs[y+1][0] -= 4
        bctrs[y+1][1] -= 4
        bctrs[y][x+1] -= 4
    elif y == 0 and not x in [0, size-1]:
        bctrs[y][x-1] -= 4
        bctrs[y+1][x-1] -= 4
        bctrs[y+1][x] -= 4
        bctrs[y+1][x+1] -= 4
        bctrs[y][x+1] -= 4
    elif x == size-1 and not y in [0, size-1]:
        bctrs[y][x-1] -= 4
        bctrs[y+1][x-1] -= 4
        bctrs[y+1][x] -= 4
        bctrs[y-1][x] -= 4
        bctrs[y-1][x-1] -= 4
    elif y == size-1 and not x in [0, size-1]:
        bctrs[y][x-1] -= 4
        bctrs[y][x+1] -= 4
        bctrs[y-1][x] -= 4
        bctrs[y-1][x+1] -= 4
        bctrs[y-1][x-1] -= 4
    else:
        bctrs[y][x-1] -= 4
        bctrs[y][x+1] -= 4
        bctrs[y-1][x] -= 4
        bctrs[y+1][x+1] -= 4
        bctrs[y+1][x-1] -= 4
        bctrs[y+1][x] -= 4
        bctrs[y-1][x-1] -= 4        
        bctrs[y-1][x+1] -= 4
for i in range(len(bctrs)):
    for j in range(len(bctrs[i])):
        if bctrs[i][j] < 0:
            bctrs[i][j] = 0
        print(bctrs[i][j], end = ' ')
    print()