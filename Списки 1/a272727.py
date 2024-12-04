order = [0]
order_inverse = [0]
count = 0
n = int(input())
for i in range(n):
    print(order[i])
    for j in range(len(order)-1, -1, -1):
        order_inverse += [order[j]]
    for x in range(len(order)):
        if order[x] == order_inverse[x]:
            count += 1
    order += [count]
    count = 0
    order_inverse = []
