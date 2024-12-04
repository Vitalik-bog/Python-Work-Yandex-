import math
pairs = {}
carts, count = [tuple(input().split()) for _ in range(int(input()))], []
for pair in carts: pairs[pair] = pairs.get(pair, 0)+1
for pair in pairs.items():
    if pair[1] > 1: count += [(math.factorial(pair[1])//len(pair[0])) // (math.factorial(pair[1] - len(pair[0])))]
pairs = list(pairs.items())
for cart in pairs:
    [count.append(element[1]* cart[1]) for element in pairs if cart[0] != element[0] and (element[0][0] in cart[0] or element[0][1] in cart[0])]
    pairs = pairs[1:]
print(sum(count))