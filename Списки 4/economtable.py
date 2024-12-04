area = int(input())
data = [input().split() for i in range(area - 1)]
datatable = []
for i in range(area):
    datatable += [[]]
    for j in range(area):
        if i == j:
            datatable[i] += [0]
        elif i > j:
            datatable[i] += [int(data[i - 1][j])]
        elif i < j:
            datatable[i] += [int(data[j - 1][i])]
prices, objects = [], [] 
first, last= [int(i) for i in input().split()]
for i in range(area):
    if i != first and i != last:
        objects += [i]
        prices += [datatable[first][i] + datatable[i][last]]
if not prices or datatable[first][last] <= min(prices):
    print(first)
else:
    value = 0
    row = []
    for i in range(len(prices)):
        if prices[i] == min(prices):
            row += [objects[i]]
            value += 1
    if value == 1:
        print(row[0])
    else:
        print(row[row.index(min(row))])