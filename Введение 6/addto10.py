n = int(input())
i = 0
sum = False
res = False
while n != 0:
    i += 1
    sum += n
    if sum == 10 and res == False:
        res = i
    n = int(input())
print(res)