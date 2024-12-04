In, numbers, array, s, n = input(), [], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 0, ''
while s < len(In):
    if In[s] != ' ':
        n += In[s]
    if In[s] == ' ' or s == len(In) - 1:
        numbers.append(int(n))
        n = ''
        while s+1 != len(In) and In[s+1] == ' ':
            s+=1
    s += 1
data, price_res, count, numbers, s, n = [], numbers[1], numbers[0], [], 0, ''
prices = []
counts = []
sums = []
for i in range(count):
    In = input()
    price = In[:7]
    count = In[8:12]
    summa = In[13:] 
    for j in range(len(price)-1, -1, -1):
        if price[j] == ' ':
            price = price[:j]
    for j in range(len(count)-1, -1, -1):
        if count[j] == ' ':
            count = count[:j]
    for j in range(len(summa)-1, -1, -1):
        if summa[j] == ' ':
            summa = summa[:j]
    prices += [price]
    counts += [count]
    sums += [summa]
res = 0
result = 0
errors = []
for j in range(len(sums)):
    res += int(sums[j])
if res == price_res:
    print(res - price_res)
else:
    for j in range(len(prices)):
        result += int(prices[j]) * int(counts[j])
        if int(prices[j]) * int(counts[j]) != int(sums[j]):
            errors += [j+1]
    print(price_res - result)
    for x in errors:
        print(x, end = ' ')    