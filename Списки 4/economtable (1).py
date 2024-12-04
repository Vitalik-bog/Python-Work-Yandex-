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
for i in range(area):
    for j in range(i + 1, area):
        prices = []
        for value in range(area):
            if value != i and value != j:
                prices += [datatable[i][value] + datatable[value][j]]
        if len(prices) != 0 and datatable[i][j] > min(prices):
            print(i, j)